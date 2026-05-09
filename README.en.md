English | [中文](README.md)

# MALA

MALA, short for More Ask, Less Answer, is a skill for repairing vague requests into answerable questions, and also a set of essays about problem formulation.
Its core principle is:
> Answers are given inside an already specified problem space, while questioning constructs the solvable structure of the problem itself.

## Quickstart

Load the [English skill](en/skill/SKILL.md), then directly send your raw question.

## If You Want To Understand MALA

See the [English docs](en/docs/README.md).

## Should I Use MALA?

Use MALA when:

- the input is still a topic, wish, or direction rather than a formed question;
- several questions are mixed together and the real unknown is unclear;
- the criterion, constraint, or boundary is missing, so direct answering will drift;
- the next useful step depends on repairing the problem first.

Do not use MALA when:

- the request is already a clear fact lookup or definition lookup;
- the request is already an explicit comparison;
- the request is already a decision task with enough constraints;
- direct answering is better than adding a formulation pass.

## One Before / After Example

Raw input:

> How long do contestants get to answer on Jeopardy?

Without MALA, a model often commits to one interpretation, such as "five seconds," and ignores that the show has different timing rules for regular clues, Final Jeopardy, and the online test.

With MALA:

- `Diagnosis`: the object is clear, but the unknown is mixed across multiple Jeopardy formats.
- `Repaired question`: "How long do contestants get to answer regular clues, Final Jeopardy, and the Jeopardy online test?"
- `Final answer`: regular clues are about 5 seconds, Final Jeopardy is 30 seconds, and the online test allows about 15 seconds per item.

More verified examples live in [English cases](en/cases/README.md), but they are still incomplete. I have not yet found a benchmark that is good enough.

## License

This repository is licensed under [CC BY 4.0](LICENSE). If you share, adapt, or redistribute the material, keep attribution and include a link to the license.
