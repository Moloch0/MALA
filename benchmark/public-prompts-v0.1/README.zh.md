# Public Prompts v0.1

这是 MALA 第一版基于真实公开用户 prompt 的冻结发布评估集。

它不是论文级 benchmark，而是一个发布评估包，用来展示：在什么情况下，MALA 式的问题构造会减少过早作答，并把模糊输入修成更可回答的问题。

## 为什么要按深度分层

MALA 不是给所有 prompt 用的。

- 如果一个 prompt 本来就清楚而且浅，最优动作通常是直接回答。
- 如果一个 prompt 有缺口但容易修复，MALA 可能有帮助。
- 如果一个 prompt 深、混杂、结构不完整，MALA 理论上应该最有收益。

所以这个 benchmark 被分成三层：

- `deep`：主评估层
- `medium`：次评估层
- `negative_control`：本来就足够明确，不应强行跑 MALA 的题

`v0.1` 的主结论应该优先从 `deep` bucket 读取，而不是把所有题粗暴平均。

更诚实的 headline 是一个窄主张：在 `deep` prompt 上，MALA 应该更稳定地把隐藏的问题结构说清楚、把问题修得更可答，并让最终回答跟着这个修复走。`negative_control` 则是边界证据，用来说明这种额外结构不该被到处硬套。

## 协议

- `Baseline`：只发送原始 prompt
- `Treatment`：先读取并应用 MALA skill 文件，再回答同一个原始 prompt
- 每次运行必须在全新的独立对话中完成
- 尽量固定同一模型、同一温度、同一天批量完成
- 不允许中途人工补充澄清

详见：

- [protocol.md](protocol.md)
- [rubric.md](rubric.md)
- [tasks.jsonl](tasks.jsonl)
- [results.csv](results.csv)

## 如何读结果

- `deep` bucket 是主结果
- `medium` bucket 是辅助证据
- `negative_control` 是边界证据，用来说明：MALA 不该被滥用到所有 prompt 上
- baseline 和 treatment 的总分不在同一把尺子上，报告时必须带分母；不要把它们读成一个共享的点数体系
- baseline 使用紧凑的原始 prompt 分数（`0-4`），由 ambiguity handling 和 answer adequacy 组成
- treatment 使用结构化分数（`0-8`），由 diagnosis、repair、answer discipline 和 intervention fit 组成
- `baseline_failure_type` 这个列名是历史遗留；实际应把它看成 baseline 的粗粒度结构标注，其中也包含 `shallow_but_ok`、`not_applicable` 这类非失败标签

## 工作流

在 Codex 环境里，最快的方式是通过本地 `codex exec` 一条命令跑完整条 release-eval 流水线：

```bash
python benchmark/public-prompts-v0.1/scripts/run_pipeline.py --transport codex_exec --bucket deep --concurrency 3 --model gpt-5.5 --judge-model gpt-5.5
```

这条命令会：

1. 收集 baseline 和 treatment runs
2. 批量 judge
3. 刷新 `results.csv` 和 `summary.md`
4. 在 `en/cases/` 与 `zh/cases/` 下生成案例页

这条路径会复用你本机 Codex client 已经能跑通的 model/provider/auth。

如果要手动分步执行，也可以按下面顺序跑：

1. 生成 baseline / treatment

```bash
python benchmark/public-prompts-v0.1/scripts/run_batch.py --transport codex_exec --mode all --bucket deep --concurrency 3 --model gpt-5.5
```

2. 批量判分

```bash
python benchmark/public-prompts-v0.1/scripts/judge_runs.py --transport codex_exec --bucket deep --concurrency 3 --model gpt-5.5
```

3. 回写结果表与摘要

```bash
python benchmark/public-prompts-v0.1/scripts/refresh_results.py
```

4. 基于官方 artifacts 生成案例页

```bash
python benchmark/public-prompts-v0.1/scripts/generate_cases.py --bucket deep --limit 3
```

这套 harness 固定遵守你确认过的公平协议：

- baseline = 只发原始 prompt
- treatment = 使用批准过的 MALA treatment 模板；若 runner 不能按路径读文件，则保留路径行并紧接着附上 skill 文件的精确内容

如果不在 Codex 环境里，同一套脚本也仍然支持通过 `--transport chat_completions` 调 OpenAI-compatible endpoint。

## 局限

- 样本量小
- 评分仍含人工判断
- 不声称统计显著性
- 测的是问题构造收益，不是通用答案正确率
