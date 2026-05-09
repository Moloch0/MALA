中文 | [English](README.en.md)

# MALA

**MALA = More Ask, Less Answer。**

MALA 是一个双语的问题构造仓库，负责一件很具体的事：在急着回答之前，先把模糊请求修成可回答的问题。

当输入还只是话题、愿望、混杂请求或未充分约束的目标时，用 MALA。它给出的不是“更顺滑的答案”，而是：

- 对原始输入中缺失、混杂、错配之处的诊断；
- 一个真正可回答的修复后问题；
- 基于修复后问题给出的最终回答。

从这里开始：

- [使用 Skill](zh/skill/SKILL.md)
- [查看 benchmark 与案例](benchmark/public-prompts-v0.1/README.zh.md)

它不适用于已经充分成形的问题。若一个请求已经具备明确的目标、未知、判准和约束，就直接回答，而不是先跑 MALA。

## MALA 是做什么的

MALA 建立在一个很简单的判断上：

> 回答是在既定问题空间中给出结果，而提问是在构造问题本身的可求解结构。

这个仓库把这个判断打包成两层：

- 解释其概念与数学背景的一组文稿；
- 一个可直接使用的 skill，把尚未成形的输入修成可判断、可推进、可更新且最少但足够的问题。

## 什么时候用 / 什么时候不用

当输入存在以下情况时，用 MALA：

- 没有暴露出真正的未知；
- 把多个问题揉在了一起；
- 用错了判准或代理目标；
- 缺少会改变下一步的必要约束；
- 更像宽泛意图，而不是可回答的问题。

当请求已经是定义查询、事实查询、明确比较题，或约束足够清楚的决策题时，不用 MALA。

## 一个前后对比例子

原始输入：

> Jeopardy 参赛者有多长时间作答？

不用 MALA 时，模型很容易直接押一个解释，比如“5 秒”，然后忽略这个问题其实混了常规题、Final Jeopardy 和线上测试三种作答场景。

用 MALA 时：

- `诊断`：对象清楚，但“未知”被多个 Jeopardy 场景混在一起。
- `修复后问题`："Jeopardy 常规题、Final Jeopardy 和线上测试各给参赛者多少作答时间？"
- `最终回答`：常规题大约 5 秒，Final Jeopardy 是 30 秒，线上测试每题大约 15 秒。

更多经过验证的案例见 [中文案例](zh/cases/README.md)。

## 它如何工作

MALA 把一个问题视为由八个元素组成的结构：

- `目标`
- `对象`
- `未知`
- `判准`
- `约束`
- `动作`
- `证据`
- `边界`

它诊断三种失效形式：

- `缺失`
- `混杂`
- `错配`

并用四个条件验证修复结果：

- `可判断`
- `可推进`
- `可更新`
- `最少但足够`

完整操作规范见 [zh/skill/SKILL.md](zh/skill/SKILL.md)。

## Quickstart

如果输入还没有成形，就按下面顺序使用这个 skill：

1. 抽取八个元素。
2. 标出哪里缺失、混杂或错配。
3. 修复问题表述。
4. 回答修复后的问题，而不是直接回答原始输入。

最小输出格式：

```markdown
原始输入的问题
- 缺了什么
- 混了什么
- 错了什么

修复后的问题
> ...

最终回答
- ...

修复说明
- 补了什么
- 拆了什么
- 改正了什么
```

## Benchmark / Cases

`v0.1` 带有一个冻结的发布评估集，题目来自真实公开用户 prompt。

- [Public prompts benchmark](benchmark/public-prompts-v0.1/README.zh.md)
- [Benchmark 任务集](benchmark/public-prompts-v0.1/tasks.jsonl)
- [Benchmark 结果表](benchmark/public-prompts-v0.1/results.csv)
- [Benchmark 摘要](benchmark/public-prompts-v0.1/summary.md)
- [中文案例](zh/cases/README.md)
- [English cases](en/cases/README.md)

`v0.1` 实际交付的是：

- 一个冻结的 12 题 release-eval 集；
- 三个深度层：`deep`（5 题）、`medium`（5 题）、`negative_control`（2 题）；
- 完整的 protocol、rubric、原始 run artifacts、judgments、汇总结果和自动生成案例页。

每道题都固定比较两次运行：

- `Baseline`：直接回答原始问题
- `Treatment`：先运行 MALA，再回答修复后的问题

这个 benchmark 按深度分层：

- `Deep`：最应该体现 MALA 收益
- `Medium`：可能受益，但增益较小
- `Negative control`：本来就足够明确，不应强行使用 MALA

更诚实的读取方式是：

- 优先读 `deep` bucket；这才是 `v0.1` 的主结果层；
- 把 `medium` 当作辅助证据，而不是主结论；
- 用 `negative_control` 标出边界：很多题直接回答反而更合适；
- 不要把分数硬并成一个排行榜：baseline 用的是紧凑的 `0-4` 分，treatment 用的是结构化的 `0-8` 分，因为它额外评价 diagnosis、repair、answer discipline 和 intervention fit。

## 仓库地图

- [中文 Skill](zh/skill/SKILL.md)
- [English skill](en/skill/SKILL.md)
- [中文文稿](zh/docs/README.md)
- [English docs](en/docs/README.md)
- [Benchmark](benchmark/public-prompts-v0.1/README.zh.md)
- [Benchmark workflow](benchmark/public-prompts-v0.1/scripts/run_pipeline.py)
- [案例](zh/cases/README.md)
- [版本说明](releases/v0.1.md)

## 版本

当前版本目标：`v0.1`

`v0.1` 声称的是：

- 一个稳定的 MALA skill 入口；
- 中英文 onboarding-first README；
- 第一版冻结的公开 release-eval 集，包含按深度分层的 prompt 与官方 artifacts；
- 基于该发布评估集生成的 benchmark-backed 案例页。

`v0.1` 不声称：

- 所有 prompt 类型都能用一个总分证明 MALA 更强；
- 通用推理能力提升；
- 答案必然正确；
- 已完成完整学术评测。

## 授权

本仓库采用 [CC BY 4.0](LICENSE) 授权。转载、改写和再分发时，请保留署名并附上许可证链接。
