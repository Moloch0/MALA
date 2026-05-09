# Public Prompts v0.1

This is MALA's first frozen release benchmark built from real public user prompts.

It is not a paper benchmark. It is a release-evaluation set designed to show when MALA-style problem formulation reduces premature answering and turns a vague request into a more answerable one.

## Why this benchmark is depth-stratified

MALA is not meant for every prompt.

- If a prompt is already clear and shallow, the right move is often to answer directly.
- If a prompt is under-specified but repairable, MALA may help.
- If a prompt is deep, mixed, or structurally incomplete, MALA should help the most.

Because of that, this benchmark is split into three buckets:

- `deep`: primary evaluation bucket
- `medium`: secondary evaluation bucket
- `negative_control`: prompts that are already clear enough and should not be forced through MALA

The main claim in `v0.1` should be read from the `deep` bucket first, not from a single average across every prompt.

The honest headline is narrow: on `deep` prompts, MALA should make the latent problem explicit, repair the question, and keep the answer aligned with that repair. `negative_control` is boundary evidence that this extra structure should not be imposed everywhere.

## Protocol

- `Baseline`: send the raw prompt only
- `Treatment`: read and apply the MALA skill file, then answer the same raw prompt
- Each run must be done in a fresh isolated conversation
- Same model, same temperature, same day batch where possible
- No manual clarification added mid-run

See:

- [protocol.md](protocol.md)
- [rubric.md](rubric.md)
- [tasks.jsonl](tasks.jsonl)
- [results.csv](results.csv)

## Reading the results

- `deep` bucket is the headline bucket
- `medium` bucket is supporting evidence
- `negative_control` is boundary evidence that MALA should not be applied indiscriminately
- baseline and treatment totals are on different scales and should always be reported with their denominators; do not read them as one shared point system
- baseline uses a compact raw-prompt score (`0-4`) from ambiguity handling and answer adequacy
- treatment uses a structural score (`0-8`) from diagnosis, repair, answer discipline, and intervention fit
- the `baseline_failure_type` column name is historical; in practice it is a coarse baseline structural annotation and includes non-failure labels such as `shallow_but_ok` and `not_applicable`

## Workflow

Fast path inside Codex: run the whole release-eval workflow through the local `codex exec` client.

```bash
python benchmark/public-prompts-v0.1/scripts/run_pipeline.py --transport codex_exec --bucket deep --concurrency 3 --model gpt-5.5 --judge-model gpt-5.5
```

This will:

1. collect baseline and treatment runs
2. judge them
3. refresh `results.csv` and `summary.md`
4. generate case-study markdown under `en/cases/` and `zh/cases/`

This path reuses the model/provider/auth that your local Codex client already knows how to use.

You can still run each step manually:

1. Run generations

```bash
python benchmark/public-prompts-v0.1/scripts/run_batch.py --transport codex_exec --mode all --bucket deep --concurrency 3 --model gpt-5.5
```

2. Run judgments

```bash
python benchmark/public-prompts-v0.1/scripts/judge_runs.py --transport codex_exec --bucket deep --concurrency 3 --model gpt-5.5
```

3. Refresh merged outputs

```bash
python benchmark/public-prompts-v0.1/scripts/refresh_results.py
```

4. Generate case-study pages from official artifacts

```bash
python benchmark/public-prompts-v0.1/scripts/generate_cases.py --bucket deep --limit 3
```

The batch runner uses the exact approved baseline rule:

- baseline = raw prompt only
- treatment = approved MALA treatment template, with the exact skill file contents appended when the runner cannot read files by path

For non-Codex environments, the same scripts still support an OpenAI-compatible `chat/completions` endpoint via `--transport chat_completions`.

## Limitations

- Small sample size
- Human judgment remains part of scoring
- No claim of statistical significance
- Measures formulation gain, not universal answer correctness
