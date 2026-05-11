中文 | [English](README.en.md)

# MALA

MALA 现在指向更大的 **MALA-Graph**：一个面向复杂问题的结构化求解框架。

它的目标不是让 LLM 一次性给出更长的答案，而是把复杂任务显式表示为一个可递归展开、可验证、可回传、可停止的 **Problem State Graph**。在这个图上，LLM 不只是回答问题，而是根据当前问题状态选择合适的 solver，继续澄清、拆分、检索、验证、压缩或停止。

## 核心区分

- `MALA-core`：原始 More Ask, Less Answer。负责把模糊输入修复成可判断、可推进、可更新的问题。
- `MALA-Graph`：新的顶层框架。负责把问题状态组织成图，并用 solver policy 决定下一步最值得推进的节点和动作。

现有 MALA 已下移到 [core/](core/README.md)，作为 MALA-Graph 的问题构造核心。

## 当前结构

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

## 从哪里读起

- [MALA-Graph 顶层定位](doc/overview.md)
- [MALA-Graph 理论基础与形式化纲领](doc/theoretical-foundation.md)
- [MALA-Graph 核心架构](doc/architecture.md)
- [Related Work：从已有工作到 MALA-Graph 的缺口](doc/related-work.md)
- [MALA-core 中文入口](core/README.md)
- [MALA-core English entry](core/README.en.md)
- [中文 Skill](core/zh/skill/SKILL.md)
- [English skill](core/en/skill/SKILL.md)
- [MALA-core benchmark](core/benchmark/public-prompts-v0.1/README.zh.md)

## 工作假设

MALA-Graph 的基本形式可以写成：

```text
MALA-Graph = ProblemStateGraph + SolverPolicy
```

- `ProblemStateGraph` 记录问题、未知、判准、约束、证据、依赖、候选答案和残余不确定性。
- `SolverPolicy` 根据当前状态、预算和目标，选择下一步执行澄清、拆分、检索、验证、回答、合并、剪枝或停止。

一个分支的目标不是消灭所有未知，而是达到“饱满”：剩余问题已经被明确归类为理论困难、资源受限、信息阻塞、价值冲突、可接受风险，或已经足以支持上层决策。

## 谨慎主张

MALA-Graph 不声称解决所有问题，也不声称存在跨所有任务的绝对最优求解方式。

它更合理的主张是：在给定问题状态表示、solver 集合、预算约束和价值函数时，MALA-Graph 试图以元推理和信息价值为依据，选择单位成本下预期收益最高的问题推进动作。

## License

This repository is licensed under [CC BY 4.0](LICENSE).
