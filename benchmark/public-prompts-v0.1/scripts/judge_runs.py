#!/usr/bin/env python3
"""
Judge baseline/treatment runs with an OpenAI-compatible chat-completions endpoint.

Outputs one JSON judgment per case under benchmark/public-prompts-v0.1/judgments/.
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
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any


DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = os.environ.get("EVAL_MODEL", "gpt-4.1")
DEFAULT_ENCODING = "utf-8"


def build_parser() -> argparse.ArgumentParser:
    benchmark_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Judge MALA benchmark runs in parallel.")
    parser.add_argument("--tasks", type=Path, default=benchmark_root / "tasks.jsonl")
    parser.add_argument("--results", type=Path, default=benchmark_root / "results.csv")
    parser.add_argument("--runs-dir", type=Path, default=benchmark_root / "runs")
    parser.add_argument("--judgments-dir", type=Path, default=benchmark_root / "judgments")
    parser.add_argument("--rubric", type=Path, default=benchmark_root / "rubric.md")
    parser.add_argument(
        "--transport",
        choices=["chat_completions", "codex_exec"],
        default="chat_completions",
        help="How to execute judge prompts.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--max-retries", type=int, default=4)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--bucket", action="append", default=[])
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--codex-cd", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--codex-sandbox", choices=["read-only", "workspace-write", "danger-full-access"], default="read-only")
    return parser


def load_tasks(path: Path) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    with path.open("r", encoding=DEFAULT_ENCODING) as handle:
        for line in handle:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def filter_tasks(tasks: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected = tasks
    if args.case:
        keep = set(args.case)
        selected = [task for task in selected if task["id"] in keep]
    if args.bucket:
        keep = set(args.bucket)
        selected = [task for task in selected if task["depth_bucket"] in keep]
    return selected


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
        "response_format": {"type": "json_object"},
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


def build_judge_prompt(task: dict[str, Any], baseline_text: str, treatment_text: str, rubric: str) -> str:
    return f"""You are scoring a MALA benchmark case. Use the rubric exactly as written below.

Rubric:
{rubric}

Task metadata:
{json.dumps(task, ensure_ascii=False, indent=2)}

Baseline output:
{baseline_text}

Treatment output:
{treatment_text}

Return strict JSON with this schema:
{{
  "case_id": "{task["id"]}",
  "baseline_failure_type": "premature_commitment | mixed_goals | missing_criterion | missing_context | shallow_but_ok | not_applicable",
  "baseline_ambiguity_handling_score": 0,
  "baseline_answer_adequacy_score": 0,
  "baseline_total": 0,
  "treatment_diagnosis_score": 0,
  "treatment_repair_score": 0,
  "treatment_answer_discipline_score": 0,
  "treatment_intervention_fit_score": 0,
  "treatment_total": 0,
  "review_note": "one or two short sentences",
  "reasoning_bucket_fit": "deep | medium | negative_control"
}}

The baseline total must equal the sum of the two baseline scores.
The treatment total must equal the sum of the four treatment scores.
Score conservatively.
For baseline ambiguity handling, give `2` only when the baseline explicitly surfaces ambiguity or missing constraints and then actively bounds, branches, or reformulates the answer around them. Generic hedging or conditional advice is usually only `1`.
For treatment intervention fit, reward proportionality:
- `2`: MALA-level repair is clearly justified and materially improves the task
- `1`: useful, but somewhat heavier than needed
- `0`: over-structured for the task; a direct answer would usually have been the better move
In `negative_control`, intervention-fit `2` should be rare.
Return JSON only. Do not add markdown fences or any commentary outside the JSON object.
"""


def judge_one(
    *,
    task: dict[str, Any],
    args: argparse.Namespace,
    rubric: str,
    print_lock: threading.Lock,
) -> None:
    baseline_path = args.runs_dir / "baseline" / f"{task['id']}.json"
    treatment_path = args.runs_dir / "treatment" / f"{task['id']}.json"
    output_path = args.judgments_dir / f"{task['id']}.json"
    if output_path.exists() and not args.overwrite:
        return
    baseline = json.loads(baseline_path.read_text(encoding=DEFAULT_ENCODING))
    treatment = json.loads(treatment_path.read_text(encoding=DEFAULT_ENCODING))
    prompt = build_judge_prompt(task, baseline["response_text"], treatment["response_text"], rubric)
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
        judgment_text = extract_text(response)
    else:
        response = run_codex_exec(
            codex_bin=args.codex_bin,
            cd=args.codex_cd,
            sandbox=args.codex_sandbox,
            model=args.model,
            prompt=prompt,
        )
        judgment_text = response["response_text"]
    judgment = json.loads(judgment_text)
    judgment["_meta"] = {
        "judged_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "judge_model": args.model,
        "transport": args.transport,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(judgment, ensure_ascii=False, indent=2) + "\n", encoding=DEFAULT_ENCODING)
    with print_lock:
        print(f"[ok] judged {task['id']} -> {output_path}")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.transport == "chat_completions" and not args.api_key:
        parser.error("OPENAI_API_KEY is required unless --api-key is passed.")

    rubric = args.rubric.read_text(encoding=DEFAULT_ENCODING).strip()
    tasks = filter_tasks(load_tasks(args.tasks), args)
    print_lock = threading.Lock()
    failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        future_map = {
            pool.submit(judge_one, task=task, args=args, rubric=rubric, print_lock=print_lock): task["id"]
            for task in tasks
            if (args.runs_dir / "baseline" / f"{task['id']}.json").exists()
            and (args.runs_dir / "treatment" / f"{task['id']}.json").exists()
        }
        for future in concurrent.futures.as_completed(future_map):
            case_id = future_map[future]
            try:
                future.result()
            except Exception as error:  # noqa: BLE001
                failures += 1
                with print_lock:
                    print(f"[error] judge {case_id}: {error}", file=sys.stderr)
    if failures:
        print(f"Completed with {failures} failed judgments.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
