---
name: problem-formulation-en
description: Rewrite not-yet-formed English input into a genuinely answerable question. Use when the raw input is still only a topic, wish, attitude, vague goal, or mixed formulation and therefore lacks a target, object, unknown, criterion, constraint, action, evidence, or boundary, or when these elements are mixed up or mismatched. Do not use when the question is already clear and can be answered directly, such as definition lookup, fact lookup, explicit comparison, or a decision task whose constraints are already sufficiently specified.
---

# Problem Formulation

## Definition

A good question is one that, under a given goal, uses the least but sufficient structure to expose the real unknown as a gap that can be judged, advanced, and updated.

This definition has four conditions:

- `Judgeable`: it must be clear what counts as having answered the question and what does not.
- `Actionable`: different answers must lead to different next steps; otherwise it is only a topic.
- `Updatable`: once new evidence enters, both the question and the answer can be revised.
- `Least but sufficient`: relative to the given goal, it neither keeps irrelevant redundancy nor deletes key structure.

This skill has only one task: repair the raw input until it satisfies these four conditions.

## Elements

A question is made of the following elements:

- `Target`: what this question ultimately serves.
- `Object`: what object, system, process, theory, or situation the question acts on.
- `Unknown`: what is actually missing.
- `Criterion`: what counts as answering it, and what counts as better or worse.
- `Constraint`: limits such as time, resources, risk, observability, or scope of applicability.
- `Action`: what kinds of moves are allowed to advance it, such as comparison, testing, reasoning, experiment, design, or decision.
- `Evidence`: what information would change the current judgment.
- `Boundary`: what belongs to this question and what does not.

If these elements have not formed a structure, the input is not yet a good question.

## Failure Modes

Relative to a good question, a bad question has only three basic failure modes:

- `Missing`: some necessary element is absent.
- `Mixed`: multiple elements or multiple questions have been kneaded together.
- `Mismatched`: the element is present but wrong, for example treating a proxy metric as the target, treating an attitude as the criterion, or treating correlation as evidence.

When diagnosing, do not invent categories first; first check these three failures.

So-called redundancy is not a fourth failure mode. It either comes from mixing caused by an uncleared boundary, or from mismatch caused by wrongly retaining irrelevant content.

## Workflow

### 1. Extract Elements

First extract from the raw input:

- target
- object
- unknown
- criterion
- constraint
- action
- evidence
- boundary

If one item is not given, mark it explicitly as missing. Do not secretly fill it in yourself.

### 2. Diagnose Failure

For each element, check three things:

- whether it is missing
- whether it is mixed with other elements
- whether it is mismatched

The diagnosis should land on the elements themselves, not on vague overall evaluation.

### 3. Repair

Repair only does the following three kinds of work:

- complete missing elements
- separate mixed elements
- correct mismatched elements

Common repairs include:

- clarifying the real target instead of inheriting the most convenient proxy metric
- compressing a topic into the real unknown instead of keeping a broad wish
- clarifying the criterion instead of staying at the level of attitude expression
- adding necessary constraints so that an answer can change the next step
- specifying the allowed advancing actions instead of leaving only empty talk
- stating what evidence would update the judgment
- drawing boundaries so that several mixed questions are separated

The goal of repair is not to make the wording prettier, but to complete the structure.

### 4. Verify the Result

After repair, check only four things:

1. Is it now `Judgeable`?
2. Is it now `Actionable`?
3. Is it now `Updatable`?
4. Is it now `Least but sufficient`?

If even one of the four still fails, the repair is not complete.

## Output

By default, output in the following order:

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

If the original input has not yet formed a question, first state clearly that it is still only a topic, wish, attitude, or under-formed goal rather than a question that can be answered directly. The final answer should respond to the repaired question, not to the raw input.
