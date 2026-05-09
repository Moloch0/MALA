#!/usr/bin/env python3
"""
Generate benchmark-backed case-study markdown files from official artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_ENCODING = "utf-8"

EN_CASE_ROOT_README = """# English Cases

These case pages are generated from official `public-prompts-v0.1` artifacts.

Selection rule:

- prefer the `deep` bucket first
- prefer `headline_bucket = true`
- then prefer higher judged treatment totals

Source benchmark:

- [Public prompts benchmark](../../benchmark/public-prompts-v0.1/README.md)

{body}
"""

ZH_CASE_ROOT_README = """# 中文案例

这些案例页由 `public-prompts-v0.1` 的官方 artifacts 自动生成。

选择规则：

- 优先使用 `deep` bucket
- 优先使用 `headline_bucket = true`
- 再按 treatment 的 judged total 从高到低排序

来源 benchmark：

- [Public prompts benchmark](../../benchmark/public-prompts-v0.1/README.zh.md)

{body}
"""

EN_CASE_TEMPLATE = """# {case_id}: {task_type}

Source benchmark bucket: `{depth_bucket}`

## Raw input

```text
{raw_prompt}
```

## Without MALA

```text
{baseline_text}
```

## With MALA: diagnosis

```text
{diagnosis_text}
```

## With MALA: repaired question

```text
{repaired_question}
```

## Final answer after repair

```text
{final_answer}
```

## What changed structurally

- Expected structural issue: `{expected_problem}`
- Baseline annotation: `{baseline_failure_type}`
- Baseline scores: ambiguity handling `{baseline_ambiguity_handling_score}`, answer adequacy `{baseline_answer_adequacy_score}`, total `{baseline_total}`
- Treatment scores: diagnosis `{diagnosis_score}`, repair `{repair_score}`, answer discipline `{answer_discipline_score}`, intervention fit `{intervention_fit_score}`, total `{treatment_total}`
- Judge note: {review_note}
- Repair notes:

```text
{repair_notes}
```

## Artifact links

- [Baseline JSON](../../benchmark/public-prompts-v0.1/runs/baseline/{case_id}.json)
- [Treatment JSON](../../benchmark/public-prompts-v0.1/runs/treatment/{case_id}.json)
- [Judgment JSON](../../benchmark/public-prompts-v0.1/judgments/{case_id}.json)
"""

ZH_CASE_TEMPLATE = """# {case_id}: {task_type}

来源 benchmark bucket：`{depth_bucket}`

## 原始输入

```text
{raw_prompt}
```

## 不用 MALA

```text
{baseline_text}
```

## 使用 MALA：诊断

```text
{diagnosis_text}
```

## 使用 MALA：修复后的问题

```text
{repaired_question}
```

## 修复后的最终回答

```text
{final_answer}
```

## 结构变化

- 预期结构问题：`{expected_problem}`
- Baseline 标注：`{baseline_failure_type}`
- Baseline 分数：ambiguity handling `{baseline_ambiguity_handling_score}`，answer adequacy `{baseline_answer_adequacy_score}`，total `{baseline_total}`
- Treatment 分数：diagnosis `{diagnosis_score}`，repair `{repair_score}`，answer discipline `{answer_discipline_score}`，intervention fit `{intervention_fit_score}`，total `{treatment_total}`
- Judge 说明：{review_note}
- Repair notes：

```text
{repair_notes}
```

## Artifact links

- [Baseline JSON](../../benchmark/public-prompts-v0.1/runs/baseline/{case_id}.json)
- [Treatment JSON](../../benchmark/public-prompts-v0.1/runs/treatment/{case_id}.json)
- [Judgment JSON](../../benchmark/public-prompts-v0.1/judgments/{case_id}.json)
"""

SECTION_MARKERS = {
    "problems in the original input": "problems",
    "problem in the original input": "problems",
    "repaired question": "repaired_question",
    "final answer": "final_answer",
    "repair notes": "repair_notes",
}


def build_parser() -> argparse.ArgumentParser:
    benchmark_root = Path(__file__).resolve().parents[1]
    repo_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description="Generate case-study markdown from official benchmark artifacts.")
    parser.add_argument("--tasks", type=Path, default=benchmark_root / "tasks.jsonl")
    parser.add_argument("--runs-dir", type=Path, default=benchmark_root / "runs")
    parser.add_argument("--judgments-dir", type=Path, default=benchmark_root / "judgments")
    parser.add_argument("--en-cases-dir", type=Path, default=repo_root / "en" / "cases")
    parser.add_argument("--zh-cases-dir", type=Path, default=repo_root / "zh" / "cases")
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--bucket", action="append", default=["deep"])
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--min-treatment-total", type=int, default=6)
    return parser


def load_tasks(path: Path) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    with path.open("r", encoding=DEFAULT_ENCODING) as handle:
        for line in handle:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding=DEFAULT_ENCODING))


def normalize_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n")
    normalized = normalized.replace("漒n", "\n")
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def heading_key(line: str) -> str:
    stripped = re.sub(r"^[#>*\-\s]+", "", line).strip()
    stripped = stripped.strip("*").strip("`").rstrip(":").strip()
    return stripped.lower()


def parse_treatment_sections(text: str) -> dict[str, str]:
    lines = normalize_text(text).split("\n")
    sections: dict[str, list[str]] = {
        "lead": [],
        "problems": [],
        "repaired_question": [],
        "final_answer": [],
        "repair_notes": [],
    }
    current = "lead"

    for raw_line in lines:
        marker = SECTION_MARKERS.get(heading_key(raw_line))
        if marker is not None:
            current = marker
            continue
        sections[current].append(raw_line)

    diagnosis_parts = []
    if sections["lead"]:
        diagnosis_parts.append("\n".join(sections["lead"]).strip())
    if sections["problems"]:
        diagnosis_parts.append("**Problems in the original input**\n\n" + "\n".join(sections["problems"]).strip())

    parsed = {
        "diagnosis": "\n\n".join(part for part in diagnosis_parts if part).strip(),
        "repaired_question": "\n".join(sections["repaired_question"]).strip(),
        "final_answer": "\n".join(sections["final_answer"]).strip(),
        "repair_notes": "\n".join(sections["repair_notes"]).strip(),
    }

    fallback = normalize_text(text)
    for key, value in parsed.items():
        if not value:
            parsed[key] = fallback
    return parsed


def collect_candidates(tasks: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    explicit_order = {case_id: index for index, case_id in enumerate(args.case)}
    allowed_buckets = set(args.bucket)
    for task in tasks:
        case_id = task["id"]
        if args.case and case_id not in explicit_order:
            continue
        if not args.case and allowed_buckets and task["depth_bucket"] not in allowed_buckets:
            continue
        baseline_path = args.runs_dir / "baseline" / f"{case_id}.json"
        treatment_path = args.runs_dir / "treatment" / f"{case_id}.json"
        judgment_path = args.judgments_dir / f"{case_id}.json"
        if not baseline_path.exists() or not treatment_path.exists() or not judgment_path.exists():
            continue
        judgment = load_json(judgment_path)
        task["_baseline_path"] = baseline_path
        task["_treatment_path"] = treatment_path
        task["_judgment_path"] = judgment_path
        task["_judgment"] = judgment
        selected.append(task)
    if args.case:
        selected.sort(key=lambda task: explicit_order[task["id"]])
        return selected[: args.limit]
    selected = [
        task
        for task in selected
        if int(task["_judgment"].get("treatment_total", 0)) >= args.min_treatment_total
    ]
    selected.sort(
        key=lambda task: (
            0 if task.get("headline_bucket") else 1,
            -int(task["_judgment"].get("treatment_total", 0)),
            -int(task["_judgment"].get("treatment_repair_score", 0)),
            task["id"],
        )
    )
    return selected[: args.limit]


def case_body(task: dict[str, Any]) -> dict[str, str]:
    baseline = load_json(task["_baseline_path"])
    treatment = load_json(task["_treatment_path"])
    judgment = task["_judgment"]
    sections = parse_treatment_sections(treatment["response_text"])
    return {
        "case_id": task["id"],
        "task_type": task["task_type"],
        "depth_bucket": task["depth_bucket"],
        "raw_prompt": task["raw_prompt"].strip(),
        "baseline_text": normalize_text(baseline["response_text"]),
        "diagnosis_text": sections["diagnosis"],
        "repaired_question": sections["repaired_question"],
        "final_answer": sections["final_answer"],
        "repair_notes": sections["repair_notes"],
        "expected_problem": task["expected_problem"],
        "baseline_failure_type": judgment.get("baseline_failure_type", ""),
        "baseline_ambiguity_handling_score": str(judgment.get("baseline_ambiguity_handling_score", "")),
        "baseline_answer_adequacy_score": str(judgment.get("baseline_answer_adequacy_score", "")),
        "baseline_total": str(judgment.get("baseline_total", "")),
        "diagnosis_score": str(judgment.get("treatment_diagnosis_score", "")),
        "repair_score": str(judgment.get("treatment_repair_score", "")),
        "answer_discipline_score": str(judgment.get("treatment_answer_discipline_score", "")),
        "intervention_fit_score": str(judgment.get("treatment_intervention_fit_score", "")),
        "treatment_total": str(judgment.get("treatment_total", "")),
        "review_note": judgment.get("review_note", ""),
    }


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding=DEFAULT_ENCODING)


def write_case_pages(selected: list[dict[str, Any]], args: argparse.Namespace) -> None:
    en_lines: list[str] = []
    zh_lines: list[str] = []
    if not selected:
        en_lines.append("No official case pages have been generated yet because no judged run artifacts are available.")
        zh_lines.append("目前还没有生成正式案例页，因为仓库里还没有可用的 judged run artifacts。")
    else:
        en_lines.append("Generated case pages:")
        zh_lines.append("已生成案例页：")
        for task in selected:
            body = case_body(task)
            case_name = f"{task['id']}.md"
            write_text(args.en_cases_dir / case_name, EN_CASE_TEMPLATE.format(**body))
            write_text(args.zh_cases_dir / case_name, ZH_CASE_TEMPLATE.format(**body))
            en_lines.append(f"- [{task['id']}]({case_name})")
            zh_lines.append(f"- [{task['id']}]({case_name})")
    write_text(args.en_cases_dir / "README.md", EN_CASE_ROOT_README.format(body="\n".join(en_lines)))
    write_text(args.zh_cases_dir / "README.md", ZH_CASE_ROOT_README.format(body="\n".join(zh_lines)))


def main() -> int:
    args = build_parser().parse_args()
    tasks = load_tasks(args.tasks)
    selected = collect_candidates(tasks, args)
    write_case_pages(selected, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
