# Summary

This summary is generated from current artifacts and available judgments.

Read `deep` first. Baseline and treatment totals are on different scales (`0-4` vs `0-8`), so raw point gaps are not a single shared uplift metric.

## Headline read

- `deep`: headline bucket. 5/5 treatment runs collected, 5/5 judged, baseline avg 3.60/4, treatment avg 7.80/8, and 5/5 treatment runs scored 6 or higher.
- `medium`: supporting evidence. 5/5 treatment runs collected, 5/5 judged, baseline avg 3.40/4, treatment avg 7.00/8, and 5/5 treatment runs scored 6 or higher.
- `negative_control`: boundary evidence. 2/2 treatment runs collected, 2/2 judged, baseline avg 2.50/4, treatment avg 5.50/8, and 1/2 treatment runs scored 6 or higher.

## Interpretation notes

Some `deep` baselines still look usable on the surface. The `v0.1` claim is not that every raw baseline collapses; it is that MALA makes diagnosis, repaired scope, and answer discipline explicit and replayable on deeper prompts.

`negative_control` should be read through `Intervention Fit`, not just through total score. A control treatment can still look structurally competent and reach 6/8 while receiving `Intervention Fit = 0`, which is exactly the signal that the extra MALA structure was unnecessary.

## Baseline structural annotation counts

- `deep`: missing_criterion=1, mixed_goals=2, not_applicable=2
- `medium`: missing_context=3, missing_criterion=1, not_applicable=1
- `negative_control`: missing_context=1, shallow_but_ok=1

The CSV field name remains `baseline_failure_type`, but these counts include non-failure labels such as `not_applicable` and `shallow_but_ok`.

## Reading rule

- Read `deep` first.
- Treat `medium` as supporting evidence.
- Use `negative_control` as boundary evidence for where MALA should not be forced.
