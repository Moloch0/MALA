# Rubric

This benchmark is scored by structure, not by claiming universal answer correctness.

## Primary interpretation

- `deep` bucket is the primary score bucket
- `medium` bucket is secondary
- `negative_control` should not be forced through MALA and is used mainly as boundary evidence

Baseline and treatment are intentionally scored on different rulers. Keep the denominators visible and do not treat a raw point gap between `0-4` and `0-8` scales as a single uplift metric.

## Baseline scores

Baseline runs are scored on two 0-2 dimensions:

1. `Ambiguity Handling`
   - `2`: explicitly identifies ambiguity or missing constraints and then actively bounds, branches, or reformulates the answer around them
   - `1`: shows some caution or conditional structure, but still leaves major ambiguity unmanaged
   - `0`: answers as if the prompt were already fully specified

`Ambiguity Handling = 2` should be relatively rare in the `deep` bucket. A sprawling but still useful direct answer is often only `1`.

2. `Answer Adequacy`
   - `2`: gives a useful answer under the raw prompt while staying honest about uncertainty
   - `1`: partly useful but overreaches, drifts, or leaves the core ask weakly served
   - `0`: weak, misleading, or poorly aligned with the raw prompt

Baseline total is `0-4`.

## Treatment scores

Each treatment run is scored on four 0-2 dimensions:

1. `Problem Diagnosis`
   - `2`: identifies the real structural issue
   - `1`: identifies a partial or shallow issue
   - `0`: misses the issue or diagnoses the wrong thing

2. `Repair Quality`
   - `2`: repaired question is clearly more answerable and better bounded
   - `1`: improves the prompt but remains partly underspecified
   - `0`: little real repair

3. `Answer Discipline`
   - `2`: final answer stays aligned with the repaired question
   - `1`: mostly aligned but drifts
   - `0`: still answers the raw vague prompt loosely

4. `Intervention Fit`
   - `2`: the amount of MALA-style diagnosis and repair is clearly justified for this prompt and materially improves the response
   - `1`: helpful, but somewhat heavier than needed
   - `0`: over-structured for the task; a direct answer would usually have been the better move

Treatment total is `0-8`.

`Intervention Fit` is especially important for `negative_control`. A structurally correct treatment can still score low there if the extra repair work was not actually warranted.

## Baseline structural annotation

Baseline runs are also annotated using:

- `premature_commitment`
- `mixed_goals`
- `missing_criterion`
- `missing_context`
- `shallow_but_ok`
- `not_applicable`

The CSV field keeps the historical name `baseline_failure_type`, but the label set is broader than literal failure. `shallow_but_ok` and `not_applicable` are expected non-failure outcomes.

## Reporting

- Report bucket-level findings separately
- Do not collapse all prompts into one headline average
- Use `deep` as the main headline bucket for MALA's value
- Use `negative_control` as boundary evidence; its key signal is often low `Intervention Fit`, not a low total score by itself
- Keep baseline and treatment score scales explicit: baseline is `0-4`, treatment is `0-8`
