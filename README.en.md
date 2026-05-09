English | [中文](README.md)

# MALA

**MALA = More Ask, Less Answer.**

MALA is a bilingual problem-formulation repository for one practical job: turn vague requests into answerable questions before rushing into answers.

Use MALA when the input is still a topic, wish, mixed request, or underspecified goal. The output is not just a smoother answer. It is:

- a diagnosis of what is missing, mixed, or mismatched;
- a repaired question that can actually be answered;
- a final answer grounded in that repaired question.

Start here:

- [Try the skill](en/skill/SKILL.md)
- [See the benchmark and cases](benchmark/public-prompts-v0.1/README.md)

Not for already well-specified questions. If the request already has a clear target, unknown, criterion, and constraints, answer it directly instead of running MALA.

## What MALA Does

MALA is built on a simple claim:

> Answers are given inside an already specified problem space, while questioning constructs the solvable structure of the problem itself.

This repository packages that claim in two forms:

- essays that explain the conceptual and mathematical background;
- a usable skill that repairs under-formed input into something judgeable, actionable, updatable, and minimally sufficient.

## When To Use / When Not To Use

Use MALA when the input:

- lacks a real unknown;
- mixes several questions together;
- uses the wrong criterion or proxy target;
- omits constraints that would change the next step;
- sounds like a broad intention instead of an answerable problem.

Do not use MALA when the request is already a direct fact lookup, definition lookup, explicit comparison, or decision task with sufficient constraints.

## One Before / After Example

Raw input:

> How long do contestants get to answer on Jeopardy?

Without MALA, a model often commits to one interpretation, such as "five seconds," and ignores that the show has different timing rules for regular clues, Final Jeopardy, and the online test.

With MALA:

- `Diagnosis`: the object is clear, but the unknown is mixed across multiple Jeopardy formats.
- `Repaired question`: "How long do contestants get to answer regular clues, Final Jeopardy, and the Jeopardy online test?"
- `Final answer`: regular clues are about 5 seconds, Final Jeopardy is 30 seconds, and the online test allows about 15 seconds per item.

More verified examples live in [English cases](en/cases/README.md).

## How It Works

MALA treats a question as a structure made of eight elements:

- `Target`
- `Object`
- `Unknown`
- `Criterion`
- `Constraint`
- `Action`
- `Evidence`
- `Boundary`

It diagnoses three failure modes:

- `Missing`
- `Mixed`
- `Mismatched`

And it verifies the repaired question against four conditions:

- `Judgeable`
- `Actionable`
- `Updatable`
- `Least but sufficient`

The full operational spec is in [en/skill/SKILL.md](en/skill/SKILL.md).

## Quickstart

If the input is still under-formed, use the skill in this order:

1. Extract the eight elements.
2. Mark what is missing, mixed, or mismatched.
3. Repair the formulation.
4. Answer the repaired question instead of the raw input.

Minimal output shape:

```markdown
Problems in the original input
- What is missing
- What is mixed
- What is wrong

Repaired question
> ...

Final answer
- ...

Repair notes
- What was added
- What was separated
- What was corrected
```

## Benchmark / Cases

`v0.1` includes a frozen release benchmark built from real public user prompts.

- [Public prompts benchmark](benchmark/public-prompts-v0.1/README.md)
- [Benchmark tasks](benchmark/public-prompts-v0.1/tasks.jsonl)
- [Benchmark results](benchmark/public-prompts-v0.1/results.csv)
- [Benchmark summary](benchmark/public-prompts-v0.1/summary.md)
- [English cases](en/cases/README.md)
- [中文案例](zh/cases/README.md)

What `v0.1` actually ships:

- a frozen 12-prompt release-eval set;
- three depth buckets: `deep` (5), `medium` (5), and `negative_control` (2);
- official protocol, rubric, raw run artifacts, judgments, merged results, and generated case pages.

The benchmark compares two runs for each prompt:

- `Baseline`: answer the raw question directly
- `Treatment`: run MALA first, then answer the repaired question

The benchmark is depth-stratified:

- `Deep`: MALA should help the most
- `Medium`: MALA may help, but gains are smaller
- `Negative control`: already clear enough that MALA should not be forced

How to read the release honestly:

- read the `deep` bucket first; that is the headline bucket for `v0.1`;
- treat `medium` as supporting evidence, not the main claim;
- use `negative_control` to show the boundary where direct answering is often the better move;
- do not collapse the scoring into one leaderboard: baseline uses a compact `0-4` score, while treatment uses a structural `0-8` score because it includes diagnosis, repair, answer discipline, and intervention fit.

## Repository Map

- [English skill](en/skill/SKILL.md)
- [Chinese skill](zh/skill/SKILL.md)
- [English docs](en/docs/README.md)
- [Chinese docs](zh/docs/README.md)
- [Benchmark](benchmark/public-prompts-v0.1/README.md)
- [Benchmark workflow](benchmark/public-prompts-v0.1/scripts/run_pipeline.py)
- [Cases](en/cases/README.md)
- [Release notes](releases/v0.1.md)

## Versioning

Current version target: `v0.1`

`v0.1` claims:

- a stable MALA skill entry point;
- onboarding-first READMEs in both languages;
- a first frozen public release-eval set with depth-stratified prompts and official artifacts;
- benchmark-backed case pages derived from that release set.

`v0.1` does not claim:

- a single-number benchmark win across all prompt types;
- universal reasoning improvement;
- guaranteed answer correctness;
- a full academic evaluation.

## License

This repository is licensed under [CC BY 4.0](LICENSE). If you share, adapt, or redistribute the material, keep attribution and include a link to the license.
