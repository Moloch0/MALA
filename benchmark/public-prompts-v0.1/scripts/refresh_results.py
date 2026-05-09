#!/usr/bin/env python3
"""
Merge run/judgment artifacts back into results.csv and summary.md.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_ENCODING = "utf-8"


def build_parser() -> argparse.ArgumentParser:
    benchmark_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Refresh results.csv and summary.md from artifacts.")
    parser.add_argument("--tasks", type=Path, default=benchmark_root / "tasks.jsonl")
    parser.add_argument("--results", type=Path, default=benchmark_root / "results.csv")
    parser.add_argument("--runs-dir", type=Path, default=benchmark_root / "runs")
    parser.add_argument("--judgments-dir", type=Path, default=benchmark_root / "judgments")
    parser.add_argument("--summary", type=Path, default=benchmark_root / "summary.md")
    return parser


def load_tasks(path: Path) -> list[dict]:
    tasks: list[dict] = []
    with path.open("r", encoding=DEFAULT_ENCODING) as handle:
        for line in handle:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def baseline_status(runs_dir: Path, case_id: str) -> str:
    return "collected" if (runs_dir / "baseline" / f"{case_id}.json").exists() else "pending"


def treatment_status(runs_dir: Path, case_id: str) -> str:
    return "collected" if (runs_dir / "treatment" / f"{case_id}.json").exists() else "pending"


def load_judgment(judgments_dir: Path, case_id: str) -> dict:
    path = judgments_dir / f"{case_id}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding=DEFAULT_ENCODING))


def write_results(tasks: list[dict], results_path: Path, runs_dir: Path, judgments_dir: Path) -> None:
    fieldnames = [
        "case_id",
        "depth_bucket",
        "headline_bucket",
        "baseline_status",
        "treatment_status",
        "baseline_failure_type",
        "baseline_ambiguity_handling_score",
        "baseline_answer_adequacy_score",
        "baseline_total",
        "treatment_diagnosis_score",
        "treatment_repair_score",
        "treatment_answer_discipline_score",
        "treatment_intervention_fit_score",
        "treatment_total",
        "notes",
    ]
    with results_path.open("w", encoding=DEFAULT_ENCODING, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            judgment = load_judgment(judgments_dir, task["id"])
            writer.writerow(
                {
                    "case_id": task["id"],
                    "depth_bucket": task["depth_bucket"],
                    "headline_bucket": "yes" if task["headline_bucket"] else "no",
                    "baseline_status": baseline_status(runs_dir, task["id"]),
                    "treatment_status": treatment_status(runs_dir, task["id"]),
                    "baseline_failure_type": judgment.get("baseline_failure_type", ""),
                    "baseline_ambiguity_handling_score": judgment.get("baseline_ambiguity_handling_score", ""),
                    "baseline_answer_adequacy_score": judgment.get("baseline_answer_adequacy_score", ""),
                    "baseline_total": judgment.get("baseline_total", ""),
                    "treatment_diagnosis_score": judgment.get("treatment_diagnosis_score", ""),
                    "treatment_repair_score": judgment.get("treatment_repair_score", ""),
                    "treatment_answer_discipline_score": judgment.get("treatment_answer_discipline_score", ""),
                    "treatment_intervention_fit_score": judgment.get("treatment_intervention_fit_score", ""),
                    "treatment_total": judgment.get("treatment_total", ""),
                    "notes": task["why_included"],
                }
            )


def write_summary(tasks: list[dict], summary_path: Path, runs_dir: Path, judgments_dir: Path) -> None:
    bucket_totals = Counter(task["depth_bucket"] for task in tasks)
    bucket_collected = Counter()
    bucket_judged = Counter()
    bucket_high_scores = Counter()
    baseline_total_sum = Counter()
    treatment_total_sum = Counter()
    failure_types: dict[str, Counter] = defaultdict(Counter)

    for task in tasks:
        case_id = task["id"]
        bucket = task["depth_bucket"]
        if (runs_dir / "treatment" / f"{case_id}.json").exists():
            bucket_collected[bucket] += 1
        judgment = load_judgment(judgments_dir, case_id)
        if judgment:
            bucket_judged[bucket] += 1
            baseline_total_sum[bucket] += int(judgment.get("baseline_total", 0))
            treatment_total_sum[bucket] += int(judgment.get("treatment_total", 0))
            if int(judgment.get("treatment_total", 0)) >= 6:
                bucket_high_scores[bucket] += 1
            failure = judgment.get("baseline_failure_type")
            if failure:
                failure_types[bucket][failure] += 1

    lines = [
        "# Summary",
        "",
        "This summary is generated from artifact status and available judgments.",
        "",
        "## Bucket status",
        "",
    ]
    for bucket in ["deep", "medium", "negative_control"]:
        lines.append(
            f"- `{bucket}`: {bucket_collected[bucket]}/{bucket_totals[bucket]} treatment runs collected, "
            f"{bucket_judged[bucket]}/{bucket_totals[bucket]} judged, "
            f"{bucket_high_scores[bucket]} scored 6 or higher"
        )
    lines.extend(["", "## Score snapshot", ""])
    for bucket in ["deep", "medium", "negative_control"]:
        judged = bucket_judged[bucket]
        if not judged:
            lines.append(f"- `{bucket}`: no numeric score summary yet")
            continue
        baseline_avg = baseline_total_sum[bucket] / judged
        treatment_avg = treatment_total_sum[bucket] / judged
        lines.append(
            f"- `{bucket}`: baseline avg {baseline_avg:.2f}/4, treatment avg {treatment_avg:.2f}/8"
        )
    if bucket_judged["deep"]:
        lines.extend(
            [
                "",
                "## Deep-bucket note",
                "",
                "Some `deep` baselines may still look usable on the surface.",
                "In this release, the stronger claim is that MALA makes diagnosis, repaired scope, and answer discipline explicit and replayable, not that every raw baseline collapses completely.",
            ]
        )
    lines.extend(["", "## Baseline failure-type counts", ""])
    for bucket in ["deep", "medium", "negative_control"]:
        if not failure_types[bucket]:
            lines.append(f"- `{bucket}`: no judgments yet")
            continue
        parts = [f"{name}={count}" for name, count in sorted(failure_types[bucket].items())]
        lines.append(f"- `{bucket}`: " + ", ".join(parts))
    lines.extend(
        [
            "",
            "## Reading rule",
            "",
            "- Read `deep` first.",
            "- Treat `medium` as supporting evidence.",
            "- Use `negative_control` to show where MALA should not be forced.",
        ]
    )
    summary_path.write_text("\n".join(lines) + "\n", encoding=DEFAULT_ENCODING)


def main() -> int:
    args = build_parser().parse_args()
    tasks = load_tasks(args.tasks)
    write_results(tasks, args.results, args.runs_dir, args.judgments_dir)
    write_summary(tasks, args.summary, args.runs_dir, args.judgments_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
