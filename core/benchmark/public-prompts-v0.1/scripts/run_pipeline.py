#!/usr/bin/env python3
"""
Run the end-to-end MALA release-eval workflow:
1. generate baseline/treatment runs
2. judge runs
3. refresh results and summary
4. generate case-study markdown pages
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    scripts_root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Run the full MALA release benchmark workflow.")
    parser.add_argument("--transport", choices=["chat_completions", "codex_exec"], default="codex_exec")
    parser.add_argument("--model", default=os.environ.get("EVAL_MODEL", "gpt-4.1"))
    parser.add_argument("--judge-model")
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--judge-temperature", type=float, default=0.0)
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--max-retries", type=int, default=4)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--bucket", action="append", default=[])
    parser.add_argument("--max-cases", type=int)
    parser.add_argument("--case-limit", type=int, default=3)
    parser.add_argument("--min-treatment-total", type=int, default=6)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--codex-cd", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--codex-sandbox", choices=["read-only", "workspace-write", "danger-full-access"], default="read-only")
    parser.add_argument("--run-batch-script", type=Path, default=scripts_root / "run_batch.py")
    parser.add_argument("--judge-script", type=Path, default=scripts_root / "judge_runs.py")
    parser.add_argument("--refresh-script", type=Path, default=scripts_root / "refresh_results.py")
    parser.add_argument("--generate-cases-script", type=Path, default=scripts_root / "generate_cases.py")
    return parser


def extend_selection_flags(command: list[str], args: argparse.Namespace) -> list[str]:
    for case_id in args.case:
        command.extend(["--case", case_id])
    for bucket in args.bucket:
        command.extend(["--bucket", bucket])
    if args.max_cases is not None:
        command.extend(["--max-cases", str(args.max_cases)])
    if args.overwrite:
        command.append("--overwrite")
    return command


def run_step(command: list[str], title: str) -> None:
    print(f"[start] {title}")
    subprocess.run(command, check=True)
    print(f"[done] {title}")


def main() -> int:
    args = build_parser().parse_args()
    judge_model = args.judge_model or args.model

    if args.transport == "chat_completions" and not args.api_key:
        raise SystemExit("OPENAI_API_KEY is required unless --api-key is passed.")

    common = ["--transport", args.transport, "--concurrency", str(args.concurrency)]
    if args.transport == "chat_completions":
        common.extend(
            [
                "--base-url",
                args.base_url,
                "--api-key",
                args.api_key,
                "--timeout",
                str(args.timeout),
                "--max-retries",
                str(args.max_retries),
            ]
        )
    else:
        common.extend(
            [
                "--codex-bin",
                args.codex_bin,
                "--codex-cd",
                str(args.codex_cd),
                "--codex-sandbox",
                args.codex_sandbox,
            ]
        )

    run_batch_cmd = [
        sys.executable,
        str(args.run_batch_script),
        "--mode",
        "all",
        "--model",
        args.model,
        "--temperature",
        str(args.temperature),
        *common,
    ]
    run_batch_cmd = extend_selection_flags(run_batch_cmd, args)

    judge_cmd = [
        sys.executable,
        str(args.judge_script),
        "--model",
        judge_model,
        "--temperature",
        str(args.judge_temperature),
        *common,
    ]
    judge_cmd = extend_selection_flags(judge_cmd, args)

    refresh_cmd = [sys.executable, str(args.refresh_script)]

    generate_cases_cmd = [
        sys.executable,
        str(args.generate_cases_script),
        "--limit",
        str(args.case_limit),
        "--min-treatment-total",
        str(args.min_treatment_total),
    ]
    for case_id in args.case:
        generate_cases_cmd.extend(["--case", case_id])
    if not args.case:
        for bucket in args.bucket:
            generate_cases_cmd.extend(["--bucket", bucket])

    run_step(run_batch_cmd, "run_batch")
    run_step(judge_cmd, "judge_runs")
    run_step(refresh_cmd, "refresh_results")
    run_step(generate_cases_cmd, "generate_cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
