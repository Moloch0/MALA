# Protocol

## Baseline

Send the raw prompt only.

```text
{raw_prompt}
```

## Treatment

Send the following prompt exactly:

```text
Read and apply this skill exactly as written:
C:\Users\LihengLuo\Documents\Codex\2026-05-09\git\MALA\en\skill\SKILL.md

Now apply it to this input:

{raw_prompt}
```

If the runner is an API harness that cannot read local files by path, keep the path line above and append the exact file contents immediately after it so the treatment still uses the real skill text rather than a paraphrase. Baseline must still remain raw-prompt-only.

The treatment is intentionally exact. Do not summarize the skill, rewrite the instructions in your own words, or add any extra setup text beyond the path line or the exact-content fallback above.

## Comparison intent

Baseline and treatment are deliberately asymmetric:

- baseline tests how the model behaves when given only the raw prompt
- treatment tests whether MALA adds an appropriate diagnosis-and-repair intervention before answering

That asymmetry is expected later in scoring: baseline is judged on a `0-4` raw-prompt scale, while treatment is judged on a `0-8` intervention scale.

## Run rules

- Every baseline run must be a fresh isolated conversation.
- Every treatment run must be a fresh isolated conversation.
- Do not reuse context across cases.
- Do not add hidden clarifications or extra setup text.
- If the model asks a follow-up clarification question, do not answer it mid-run.
- Use the same model and similar runtime settings across the batch when possible.
