---
name: problem-formulation-zh-hard
description: 复杂问题构造的 hard 版执行规范。用于需要严格来源控制、版本修订、冲突保留、停机判定和可靠交接的场景。不是默认版本。
---

# 问题构造（Hard）

## 1. 目标

本规范只负责问题构造，不直接生成最终回答。

只在下列情况启用：

- simple 版本已不足以稳定承载当前问题；
- 需要显式管理来源、版本、冲突、撤销或交接；
- 需要把动作写成有前提、禁行条件和失败去向的约束系统。

不要在下列情况启用：

- 当前输入已经可以直接回答；
- simple 版本已足够；
- 任务只是一般澄清，不需要显式状态管理。

## 2. 核心原则

- 先诊断，再行动。
- 一步只处理一个 `primary_diagnosis`。
- 不伪造确定性。
- 不隐式消解冲突。
- 不偷带旧版本状态。
- 不为了结构完整而过度构造。

## 3. 合法终点

- `ReadyQuestion`
- `Clarify`
- `SplitQuestions`
- `NotCurrentlyAnswerable`

## 4. 状态模型

```text
state := {
  meta,
  slots
}
```

### 4.1 `meta`

```text
meta := {
  question_version,
  handoff_target?,
  stop_reason?,
  robustness_scope?
}
```

约束：

- `meta` 只承载控制信息。
- `目标 / 对象 / 未知 / 判准 / 约束 / 动作 / 证据 / 边界` 一律放入 `slots`。

### 4.2 `slots`

```text
slots := {
  目标: slot_state,
  对象: slot_state,
  未知: slot_state,
  判准: slot_state,
  约束: slot_state,
  动作: slot_state,
  证据: slot_state,
  边界: slot_state
}
```

槽位语义：

- `目标`：这个问题最终服务于什么任务结果。
- `对象`：这个问题作用于什么对象、系统、过程、理论或情境。
- `未知`：真正缺失、需要被回答的是什么。
- `判准`：什么算答到，什么算更好或更差。
- `约束`：时间、资源、风险、可观测性、适用范围等限制。
- `动作`：允许通过什么方式推进。
- `证据`：什么信息会改变当前判断。
- `边界`：哪些内容属于当前问题，哪些内容不属于当前问题。

### 4.3 `slot_state`

```text
slot_state := {
  value,
  status,
  source,
  note?,
  conflict?
}
```

```text
status := given | inferred | pending | conflicted
```

```text
source := {
  kind,
  basis?
}
```

```text
source.kind :=
  explicit_input
| implicit_input
| stable_context
| prior_state
| tool_result
| external_evidence
```

## 5. 写入规则

1. 所有写入都必须保留合法来源。
2. `given` 只能来自可直接引用的合法来源。
3. `inferred` 必须保留 `basis`。
4. `pending` 不得无依据提升为 `given` 或 `inferred`。
5. `conflicted`、`pending` 和未决冲突不得被隐式消去。
6. 新证据使旧推断失效时，必须显式撤销。
7. `prior_state` 不是免责来源，旧状态失效后不得继续沿用。

区分：

- `illegal_promotion`：确定性被错误提升。
- `unsupported_write`：写入动作本身越界；例如无合法来源、写错目标、写入当前动作不允许写入的字段。它不要求已经发生错误提升，也不要求已经无路可走。

## 6. 版本规则

出现下列情况时，必须递增 `question_version`：

- `split` 把一个问题变成多个子问题；
- `narrow` 实质改变求解边界；
- `correct` 实质改变问题身份；
- `downgrade` 把原任务改写为较弱但仍有价值的任务；
- 新证据使旧版本关键推断或关键路由不再可靠。

下列情况通常不升版本：

- 补录来源；
- 合法补全 `pending`；
- 记录冲突；
- 不改变问题身份的局部修订。

## 7. 诊断集合

```text
diagnosis :=
  missing
| mixed
| misaligned
| overbroad
| missing_source
| illegal_promotion
| unresolved_conflict
| stale_state
| ready_for_handoff
| channel_mismatch
| unsupported_write
| no_viable_route
```

定义：

- `missing`：关键内容缺失。
- `mixed`：多个问题、目标、对象、判准或时间尺度混在一起。
- `misaligned`：槽位归属、问题锚定或语义边界错位。
- `overbroad`：问题过宽，当前通道无法稳定处理。
- `missing_source`：已有值，但来源缺失或未结构化。
- `illegal_promotion`：确定性被错误提升。
- `unresolved_conflict`：存在未完成处理的关键冲突。
- `stale_state`：旧状态、旧依据或旧路由已失效。
- `ready_for_handoff`：当前问题已满足局部交接条件。
- `channel_mismatch`：任务强度或通道与现有处理能力不匹配。
- `unsupported_write`：写入动作本身越界。
- `no_viable_route`：不存在有价值的继续路径。

## 8. 执行流程

1. 判断是否应启用 hard 版。
2. 识别当前 `primary_diagnosis`。
3. 选择首选动作。
4. 检查 `preconditions` 与 `forbidden_when`。
5. 执行允许写入。
6. 用 `success_test` 检查结果。
7. 成功则重判状态或终点。
8. 失败则按 `failure_route` 转移。

执行约束：

- 不得绕过 `failure_route` 自由改选动作。
- 不得先输出终点，再倒推状态。
- 不得把控制层失败伪装成“槽位没填完”。

## 9. 动作映射

- `missing -> clarify`
- `mixed -> split`
- `misaligned -> correct`
- `overbroad -> narrow`
- `missing_source -> record_source`
- `illegal_promotion -> retract_inference`
- `unresolved_conflict -> mark_conflict / resolve_conflict`
- `stale_state -> bump_version`
- `ready_for_handoff -> transfer`
- `channel_mismatch -> transfer / downgrade`
- `unsupported_write -> retract_inference / declare_not_answerable`
- `no_viable_route -> declare_not_answerable`

补充：

- `unresolved_conflict` 若尚未编码，先 `mark_conflict`。
- `channel_mismatch` 若只是交接通道不匹配，优先 `transfer`。
- 同一诊断上重复执行同一动作且无新证据、无状态增量时，不得继续循环，必须转入 `downgrade` 或 `declare_not_answerable`。

## 10. 动作规则

统一格式：

```text
ActionRule := {
  name,
  trigger_diagnosis,
  preconditions,
  forbidden_when,
  allowed_writes,
  success_test,
  failure_route
}
```

### 10.1 `clarify(slot)`

- `trigger_diagnosis`：`missing`
- `preconditions`：目标槽位为 `pending` 或无法唯一确定；一次澄清能显著压缩关键不确定性。
- `forbidden_when`：实际问题不是缺信息，而是锚定已错；澄清不会实质缩小搜索空间。
- `allowed_writes`：更新目标槽位并记录来源。
- `success_test`：目标槽位不再是无依据的 `pending`，且关键不确定性变小。
- `failure_route`：`correct | split | declare_not_answerable`

### 10.2 `split(problem)`

- `trigger_diagnosis`：`mixed`
- `preconditions`：多个目标、对象、判准或时间尺度被耦合。
- `forbidden_when`：实际只是单槽位缺失。
- `allowed_writes`：拆成多个子问题；必要时递增 `question_version`。
- `success_test`：原混杂点被拆开，每个子问题都可独立承载。
- `failure_route`：`narrow | downgrade`

### 10.3 `correct(slot_or_problem)`

- `trigger_diagnosis`：`misaligned`
- `preconditions`：槽位归属、问题边界或问题锚定已错。
- `forbidden_when`：问题只是信息缺失。
- `allowed_writes`：纠正错误槽位或问题锚定；保留修订痕迹；必要时递增版本。
- `success_test`：错配位置被明确纠正，旧值未被无痕抹除。
- `failure_route`：`split | clarify | declare_not_answerable`

### 10.4 `narrow(boundary)`

- `trigger_diagnosis`：`overbroad`
- `preconditions`：当前任务范围过宽，当前通道无法稳健处理。
- `forbidden_when`：收窄会直接违背用户显式核心目标。
- `allowed_writes`：收窄边界、对象范围、时间尺度或判准；必要时递增版本。
- `success_test`：收窄后的问题在当前通道内可稳定承载，且未偷换目标。
- `failure_route`：`downgrade | declare_not_answerable`

### 10.5 `record_source(slot)`

- `trigger_diagnosis`：`missing_source`
- `preconditions`：槽位已有值，但来源缺失、过粗或未结构化。
- `forbidden_when`：当前值本身就是越界写入。
- `allowed_writes`：只补写 `source / basis / note`。
- `success_test`：来源完整、可追踪；若状态为 `inferred`，则 `basis` 已补齐。
- `failure_route`：`retract_inference`

### 10.6 `mark_conflict(slot)`

- `trigger_diagnosis`：`unresolved_conflict`
- `preconditions`：已发现两个或以上互不兼容的值、依据或判定，且冲突尚未编码。
- `forbidden_when`：所谓冲突只是措辞差异，不影响判定。
- `allowed_writes`：将槽位标为 `conflicted`，并写入 `conflict`。
- `success_test`：冲突点、冲突双方及其依据都已可见。
- `failure_route`：`retract_inference | resolve_conflict`

### 10.7 `resolve_conflict(slot)`

- `trigger_diagnosis`：`unresolved_conflict`
- `preconditions`：冲突已被编码，且存在足以区分优先级、适用边界或保留分支的依据。
- `forbidden_when`：没有新增证据，也没有更高优先级的来源规则。
- `allowed_writes`：更新选定值、状态与来源；或把冲突显式保留为可交接未决项。
- `success_test`：冲突被解决，或被显式保留并完成路由。
- `failure_route`：`clarify | transfer | declare_not_answerable`

### 10.8 `retract_inference(slot_or_write)`

- `trigger_diagnosis`：`illegal_promotion | stale_state | unsupported_write`
- `preconditions`：当前确定性缺少合法依据，或某次写入必须回滚到诚实状态。
- `forbidden_when`：当前值仍有直接、合法且未失效的支撑。
- `allowed_writes`：将状态降回 `pending` 或 `conflicted`；保留撤销说明。
- `success_test`：不受支持的确定性或越界写入已被撤销，且原因已记录。
- `failure_route`：`record_source | mark_conflict | declare_not_answerable`

### 10.9 `bump_version(reason)`

- `trigger_diagnosis`：`stale_state`
- `preconditions`：问题身份已被实质改变，或新证据使旧版本不再可靠。
- `forbidden_when`：只是措辞润色，没有改变问题身份或判断结构。
- `allowed_writes`：递增 `question_version`，并标记旧状态不得继续沿用。
- `success_test`：新旧版本已显式切开，旧推断不会无痕进入新版本。
- `failure_route`：`retract_inference`

### 10.10 `transfer(channel)`

- `trigger_diagnosis`：`ready_for_handoff | channel_mismatch`
- `preconditions`：当前问题已局部可交接；交接目标与结果路由已明确。
- `forbidden_when`：关键冲突仍被隐藏；停止理由尚未成立。
- `allowed_writes`：只写交接元数据，不捏造内容槽位。
- `success_test`：接收方无需补读隐含前提即可接手。
- `failure_route`：返回相关内容或状态动作。

### 10.11 `downgrade(problem')`

- `trigger_diagnosis`：`channel_mismatch`
- `preconditions`：原任务过强、过宽或当前通道无法承担。
- `forbidden_when`：降格会丢掉用户仍关心的操作性目标。
- `allowed_writes`：把当前问题改写为较弱但仍有价值的替代问题；递增版本。
- `success_test`：新问题仍对原任务有价值，且在当前通道内可稳定处理。
- `failure_route`：`declare_not_answerable`

### 10.12 `declare_not_answerable(reason)`

- `trigger_diagnosis`：`unsupported_write | no_viable_route`
- `preconditions`：继续推进将依赖伪造确定性、越界补足、不可获得证据或无价值循环。
- `forbidden_when`：仍存在高收益、低代价、边界明确的澄清、拆分、收窄或降格路径。
- `allowed_writes`：只写明原因、缺失条件和停止理由。
- `success_test`：停止理由明确，缺失条件明确，且为什么应诚实终止已可见。
- `failure_route`：无

## 11. 调度附则：三层视角

三层结构只作为调度视角，不作为正文骨架。

- 内容层：`missing | mixed | misaligned | overbroad`
- 状态层：`missing_source | illegal_promotion | unresolved_conflict | stale_state | unsupported_write`
- 控制层：`ready_for_handoff | channel_mismatch | no_viable_route`

调度规则：

- 内容问题暴露出来源、冲突、版本或撤销问题时，升级到状态层。
- 状态问题暴露出交接、停机或通道问题时，升级到控制层。
- 控制层要求继续构造时，回落到相应内容或状态动作。

## 12. 终点判定

### 12.1 `ReadyQuestion`

当且仅当：

- 当前版本有明确判准；
- 当前版本能导向下一步，而不只是停留在话题描述；
- 新证据进入后允许修订；
- 交接包相对当前任务最小充分；
- 关键冲突已解决，或已显式登记且不阻断回答阶段；
- 当前主诊断为 `ready_for_handoff`。

### 12.2 `Clarify`

当且仅当：

- 当前主诊断为 `missing`、`missing_source`，或可通过一次低成本澄清解决的 `unresolved_conflict`；
- 仍只有少量关键待定项；
- 澄清路径边界清楚、收益明确；
- 补问成本低于预期收益。

### 12.3 `SplitQuestions`

当且仅当：

- 当前主诊断为 `mixed`；
- 不拆开会持续产生混杂与错配；
- 拆开后存在更稳定的后继路径。

### 12.4 `NotCurrentlyAnswerable`

当且仅当：

- 当前主诊断为 `unsupported_write` 或 `no_viable_route`，或经失败路由收敛到二者之一；
- 关键结构无法从输入、稳定上下文或可获取证据中得到；
- 不存在有价值的澄清、拆分、收窄或降格路径；
- 停止理由与缺失条件都能被显式交代。

## 13. 输出契约

### 13.1 默认简版

```markdown
当前判定
- terminal: ReadyQuestion | Clarify | SplitQuestions | NotCurrentlyAnswerable
- primary_diagnosis: ...
- question_version: ...
- stop_reason: ...

关键更新
- changed_slots: ...
- unresolved_conflicts: ...

未闭合项
- ...

下一阶段
- handoff_target: ...
- next_action_or_route: ...
```

### 13.2 审计版

只在下列情况输出：

- `question_version` 刚发生变化；
- 仍有显著未决冲突；
- 需要复杂交接；
- 用户明确要求审计细节。

```markdown
当前判定
- terminal: ReadyQuestion | Clarify | SplitQuestions | NotCurrentlyAnswerable
- primary_diagnosis: ...
- question_version: ...
- handoff_target: ...
- stop_reason: ...

meta 摘要
- robustness_scope: ...

slots 摘要
- 目标: value / status / source / conflict?
- 对象: value / status / source / conflict?
- 未知: value / status / source / conflict?
- 判准: value / status / source / conflict?
- 约束: value / status / source / conflict?
- 动作: value / status / source / conflict?
- 证据: value / status / source / conflict?
- 边界: value / status / source / conflict?

交接说明
- 为什么停在这里
- 当前主诊断是什么
- 哪些缺口仍未闭合
- 下一阶段应如何接手
```

## 14. 最后约束

- 不要把 hard 版误当成默认版本。
- 不要把 `meta` 和 `slots` 的语义重新混写。
- 不要把 `unsupported_write` 混同于 `illegal_promotion` 或 `no_viable_route`。
- 不要把三层结构重新扩写成正文主骨架。
- 不要在缺少关键结构时伪装成已经可以回答。
