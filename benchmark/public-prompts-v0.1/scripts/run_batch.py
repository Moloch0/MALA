#!/usr/bin/env python3
"""
Batch runner for the MALA public-prompts-v0.1 release benchmark.

This script uses an OpenAI-compatible chat-completions endpoint and supports:
- baseline runs: raw prompt only
- treatment runs: inline the exact skill file contents, then apply it to the raw prompt

Environment variables:
- OPENAI_API_KEY: required unless --api-key is passed
- OPENAI_BASE_URL: optional, defaults to https://api.openai.com/v1
- EVAL_MODEL: optional default model
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any


DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = os.environ.get("EVAL_MODEL", "gpt-4.1")
DEFAULT_ENCODING = "utf-8"


@dataclass
class Task:
    id: str
    raw_prompt: str
    depth_bucket: str
    task_type: str
    headline_bucket: bool
    payload: dict[str, Any]


def build_parser() -> argparse.ArgumentParser:
    benchmark_root = Path(__file__).resolve().parents[1]
    repo_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description="Run MALA benchmark generations in parallel.")
    parser.add_argument("--mode", choices=["baseline", "treatment", "all"], default="all")
    parser.add_argument("--tasks", type=Path, default=benchmark_root / "tasks.jsonl")
    parser.add_argument("--runs-dir", type=Path, default=benchmark_root / "runs")
    parser.add_argument("--skill-path", type=Path, default=repo_root / "en" / "skill" / "SKILL.md")
    parser.add_argument(
        "--transport",
        choices=["chat_completions", "codex_exec"],
        default="chat_completions",
        help="How to execute benchmark prompts.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--max-retries", type=int, default=4)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--case", action="append", default=[], help="Run only specific case IDs")
    parser.add_argument("--bucket", action="append", default=[], help="Run only specific depth buckets")
    parser.add_argument("--max-cases", type=int)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--codex-cd", type=Path, default=repo_root)
    parser.add_argument("--codex-sandbox", choices=["read-only", "workspace-write", "danger-full-access"], default="read-only")
    return parser


def load_tasks(path: Path) -> list[Task]:
    tasks: list[Task] = []
    with path.open("r", encoding=DEFAULT_ENCODING) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            payload = json.loads(line)
            tasks.append(
                Task(
                    id=payload["id"],
                    raw_prompt=payload["raw_prompt"],
                    depth_bucket=payload["depth_bucket"],
                    task_type=payload["task_type"],
                    headline_bucket=bool(payload["headline_bucket"]),
                    payload=payload,
                )
            )
    return tasks


def filter_tasks(tasks: list[Task], args: argparse.Namespace) -> list[Task]:
    selected = tasks
    if args.case:
        keep = set(args.case)
        selected = [task for task in selected if task.id in keep]
    if args.bucket:
        keep = set(args.bucket)
        selected = [task for task in selected if task.depth_bucket in keep]
    if args.max_cases is not None:
        selected = selected[: args.max_cases]
    return selected


def baseline_prompt(task: Task) -> str:
    return task.raw_prompt


def treatment_prompt(task: Task, skill_path: Path, skill_text: str) -> str:
    return (
        "Read and apply this skill exactly as written:\n"
        f"{skill_path}\n\n"
        "Exact file contents:\n"
        f"{skill_text}\n\n"
        "Now apply it to this input:\n\n"
        f"{task.raw_prompt}"
    )


def post_chat_completion(
    *,
    base_url: str,
    api_key: str,
    model: str,
    temperature: float,
    prompt: str,
    timeout: float,
    max_retries: int,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    endpoint = base_url.rstrip("/") + "/chat/completions"
    body = json.dumps(payload).encode(DEFAULT_ENCODING)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        request = urllib.request.Request(endpoint, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode(DEFAULT_ENCODING))
        except urllib.error.HTTPError as error:
            last_error = error
            if error.code not in {408, 409, 429, 500, 502, 503, 504} or attempt == max_retries:
                raise
        except urllib.error.URLError as error:
            last_error = error
            if attempt == max_retries:
                raise
        time.sleep(min(2**attempt, 10))
    assert last_error is not None
    raise last_error


def extract_text(response: dict[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        return "".join(parts)
    return str(content)


def run_codex_exec(*, codex_bin: str, cd: Path, sandbox: str, model: str, prompt: str) -> dict[str, Any]:
    with NamedTemporaryFile("w", encoding=DEFAULT_ENCODING, delete=False, suffix=".txt") as handle:
        output_path = Path(handle.name)
    command = [
        codex_bin,
        "exec",
        "-C",
        str(cd),
        "--output-last-message",
        str(output_path),
        "--sandbox",
        sandbox,
        "--model",
        model,
        prompt,
    ]
    completed = subprocess.run(command, capture_output=True, text=True, encoding=DEFAULT_ENCODING, errors="replace")
    response_text = output_path.read_text(encoding=DEFAULT_ENCODING) if output_path.exists() else ""
    if output_path.exists():
        output_path.unlink()
    if completed.returncode != 0:
        raise RuntimeError(
            f"codex exec failed with exit code {completed.returncode}\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    return {
        "transport": "codex_exec",
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "response_text": response_text,
    }


def run_one(
    *,
    task: Task,
    run_type: str,
    prompt: str,
    output_path: Path,
    args: argparse.Namespace,
    print_lock: threading.Lock,
) -> None:
    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if args.transport == "chat_completions":
        response = post_chat_completion(
            base_url=args.base_url,
            api_key=args.api_key,
            model=args.model,
            temperature=args.temperature,
            prompt=prompt,
            timeout=args.timeout,
            max_retries=args.max_retries,
        )
        response_text = extract_text(response)
    else:
        response = run_codex_exec(
            codex_bin=args.codex_bin,
            cd=args.codex_cd,
            sandbox=args.codex_sandbox,
            model=args.model,
            prompt=prompt,
        )
        response_text = response["response_text"]
    completed_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    result = {
        "case_id": task.id,
        "run_type": run_type,
        "transport": args.transport,
        "model": args.model,
        "temperature": args.temperature,
        "started_at": started_at,
        "completed_at": completed_at,
        "depth_bucket": task.depth_bucket,
        "task_type": task.task_type,
        "headline_bucket": task.headline_bucket,
        "raw_prompt": task.raw_prompt,
        "prompt_sent": prompt,
        "response_text": response_text,
        "raw_response": response,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding=DEFAULT_ENCODING) as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with print_lock:
        print(f"[ok] {run_type} {task.id} -> {output_path}")


def iter_jobs(tasks: list[Task], args: argparse.Namespace, skill_text: str) -> list[tuple[Task, str, str, Path]]:
    jobs: list[tuple[Task, str, str, Path]] = []
    modes = ["baseline", "treatment"] if args.mode == "all" else [args.mode]
    for task in tasks:
        for run_type in modes:
            prompt = (
                baseline_prompt(task)
                if run_type == "baseline"
                else treatment_prompt(task, args.skill_path, skill_text)
            )
            output_path = args.runs_dir / run_type / f"{task.id}.json"
            if output_path.exists() and not args.overwrite:
                continue
            jobs.append((task, run_type, prompt, output_path))
    return jobs


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.transport == "chat_completions" and not args.api_key:
        parser.error("OPENAI_API_KEY is required unless --api-key is passed.")

    tasks = filter_tasks(load_tasks(args.tasks), args)
    skill_text = args.skill_path.read_text(encoding=DEFAULT_ENCODING).strip()
    jobs = iter_jobs(tasks, args, skill_text)
    if not jobs:
        print("No jobs to run.")
        return 0

    print_lock = threading.Lock()
    failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        future_map = {
            pool.submit(
                run_one,
                task=task,
                run_type=run_type,
                prompt=prompt,
                output_path=output_path,
                args=args,
                print_lock=print_lock,
            ): (run_type, task.id)
            for task, run_type, prompt, output_path in jobs
        }
        for future in concurrent.futures.as_completed(future_map):
            run_type, case_id = future_map[future]
            try:
                future.result()
            except Exception as error:  # noqa: BLE001
                failures += 1
                with print_lock:
                    print(f"[error] {run_type} {case_id}: {error}", file=sys.stderr)
    if failures:
        print(f"Completed with {failures} failed jobs.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
