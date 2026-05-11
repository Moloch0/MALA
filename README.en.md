English | [中文](README.md)

# MALA

MALA now refers to the larger **MALA-Graph** project: a structured problem-solving framework for complex tasks.

Its goal is not to make an LLM produce a longer one-shot answer. Its goal is to represent a complex task as a recursive, inspectable, updateable, and stoppable **Problem State Graph**. On this graph, the LLM does not merely answer. It reads the current problem state, chooses an appropriate solver action, and continues clarifying, decomposing, retrieving, verifying, compressing, or stopping.

## Core Distinction

- `MALA-core`: the original More Ask, Less Answer layer. It repairs vague input into a judgeable, actionable, and updatable question.
- `MALA-Graph`: the new top-level framework. It organizes problem states into a graph and uses a solver policy to decide which node and action are most worth advancing next.

The original MALA material now lives under [core/](core/README.en.md), where it serves as the problem-formulation core of MALA-Graph.

## Current Layout

```text
MALA/
  README.md
  README.en.md
  doc/
    README.md
    overview.md
    related-work.md
  core/
    README.md
    README.en.md
    zh/
    en/
    benchmark/
    releases/
```

## Start Here

- [MALA-Graph top-level positioning](doc/overview.md)
- [MALA-Graph theoretical foundation](doc/theoretical-foundation.md)
- [MALA-Graph core architecture](doc/architecture.md)
- [Related work and the gap for MALA-Graph](doc/related-work.md)
- [MALA-core Chinese entry](core/README.md)
- [MALA-core English entry](core/README.en.md)
- [Chinese skill](core/zh/skill/SKILL.md)
- [English skill](core/en/skill/SKILL.md)
- [MALA-core benchmark](core/benchmark/public-prompts-v0.1/README.md)

## Working Hypothesis

MALA-Graph can be summarized as:

```text
MALA-Graph = ProblemStateGraph + SolverPolicy
```

- `ProblemStateGraph` records the problem, unknowns, criteria, constraints, evidence, dependencies, candidate answers, and residual uncertainty.
- `SolverPolicy` uses the current state, budget, and objective to choose whether to clarify, decompose, retrieve, verify, answer, merge, prune, or stop.

The goal of a branch is not to eliminate every unknown. The goal is to become saturated: the remaining uncertainty has been explicitly classified as theoretical hardness, resource limit, information blockage, value conflict, acceptable risk, or sufficient for the parent decision.

## Careful Claim

MALA-Graph does not claim to solve all problems, and it does not claim an absolute optimum across all tasks.

The more defensible claim is: given a problem-state representation, a solver set, a budget, and a value function, MALA-Graph attempts to use metareasoning and value-of-information principles to select the highest expected-value problem-advancement action per unit cost.

## License

This repository is licensed under [CC BY 4.0](LICENSE).
