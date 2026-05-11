# MALA-Graph 核心架构

本文只记录 MALA-Graph 的算法架构草案。它不是实现计划，也不是最终理论证明。真正的理论基础见 [theoretical-foundation.md](theoretical-foundation.md)。

## 1. 总体定义

MALA-Graph 暂定为：

```text
MALA-Graph = ProblemStateGraph + SolverActions + ControlPolicy + SaturationCriterion
```

其中：

- `ProblemStateGraph` 是持久化的问题状态图；
- `SolverActions` 是允许改变图状态的一组操作；
- `ControlPolicy` 决定下一步在图上执行哪个操作；
- `SaturationCriterion` 判断一个节点或分支是否已经足够饱满，或为何不能继续推进。

MALA-Graph 的目标不是替代 MALA-core，而是把 MALA-core 构造出的可求解问题放入一个递归求解结构中。

## 2. 四层架构

```text
Layer 4: Interface Layer
  可视化、交互、审批、修改、导航。

Layer 3: Control Layer
  选择 frontier node，选择 solver，分配预算，判断停止。

Layer 2: Solver Layer
  formulate / decompose / clarify / retrieve / critique / answer / compress / saturate。

Layer 1: State Layer
  ProblemNode / ProblemEdge / Evidence / Residual / GraphPatch / GraphSnapshot。
```

实现顺序不应从 UI 开始，而应从 State Layer 和 Control Layer 开始。没有稳定状态表示和控制策略，solver 与 UI 都会退化为普通文本生成。

## 3. ProblemNode

一个节点不是一句话，而是一个局部问题状态。

```yaml
id: node_001
parent_id: null
type: root_problem | subproblem | hypothesis | evidence_gap | decision | answer_candidate
status: open | active | answered | saturated | blocked | rejected

question:
  raw: ""
  repaired: ""

target:
  description: ""
  parent_relevance: ""

unknowns:
  - id: u1
    description: ""

criteria:
  - ""

constraints:
  budget_tokens: null
  time_limit: null
  tools_allowed: []
  assumptions: []

evidence:
  supporting: []
  opposing: []
  missing: []

dependencies:
  requires: []
  informs: []

candidate_outputs:
  answers: []
  decisions: []
  artifacts: []

residual:
  kind: none | resolved | missing_info | resource_limited | theoretical_hardness | value_conflict | acceptable_risk | ill_posed
  description: ""

next_actions:
  - solver: decompose
    reason: ""
    priority: 0.0

audit:
  created_by: ""
  updated_by: ""
  confidence: 0.0
  last_update: ""
```

这个结构保存的是可审计推理状态，而不是完整思维链。完整思维链不适合作为长期载体；问题状态可以被读取、验证、更新、合并和回传。

## 4. ProblemStateGraph

第一版可以实现成树，但理论对象应是有向图，通常是 DAG。复杂问题中多个分支常常共享同一个子问题，纯树会导致重复展开。

```yaml
nodes:
  node_001: ...
  node_002: ...

edges:
  - from: node_001
    to: node_002
    type: decomposes_to
  - from: node_004
    to: node_002
    type: depends_on
```

建议第一版边类型控制在少量集合内：

```text
decomposes_to
depends_on
supports
contradicts
refines
answers
blocks
updates
```

## 5. SolverActions

Solver 不是一个 agent 角色，而是对图状态的变换。

```text
solver(input_graph, target_node_id, budget, objective) -> graph_patch
```

第一版 solver 集合：

```text
formulate
  调用 MALA-core，把原始输入修成初始 ProblemNode。

decompose
  把一个问题拆成子问题。

clarify
  找出缺失目标、对象、未知、判准、约束、证据或边界。

retrieve
  获取外部证据、引用或事实。

critique
  找前提错误、伪问题、错配目标、反例和风险。

answer
  在当前节点足够饱满时给出局部答案。

compress
  把子节点结果回传并压缩到父节点。

saturate
  判断节点是否已经饱满，或剩余问题属于哪种 residual。
```

Solver 不直接改写文件或隐式改变图，而是返回 `GraphPatch`：

```yaml
patch:
  update_nodes: []
  add_nodes: []
  add_edges: []
  remove_edges: []
  notes: []
```

## 6. ControlPolicy

MALA-Graph 的关键算法问题是：

> 下一步展开哪个节点，并执行哪个 solver？

启发式第一版可以使用：

```text
priority(node, solver)
=
decision_relevance
* uncertainty
* tractability
* dependency_centrality
* expected_information_gain
/ estimated_cost
```

但这只是初始工程近似，不应被误写成理论最优。理论上，ControlPolicy 应被理解为一个受预算约束的元推理策略：它选择的不是世界动作，而是计算动作、澄清动作、检索动作和问题构造动作。

## 7. 控制循环

```python
def run_mala_graph(root_input, budget):
    graph = initialize_graph(root_input)
    graph = run_solver("formulate", graph, root_node_id)

    while budget.remaining_steps > 0:
        frontier = collect_frontier(graph)
        if not frontier:
            break

        candidate_actions = []
        for node in frontier:
            candidate_actions.extend(propose_actions(graph, node))

        scored = score_actions(graph, candidate_actions, budget)
        action = select_best(scored)

        if action.expected_value < action.cost:
            mark_saturated_or_blocked(graph, action.node_id)
            continue

        patch = run_solver(action.solver, graph, action.node_id, budget)
        validate_patch(patch)
        apply_patch(graph, patch)

        propagate_child_updates(graph)
        update_saturation(graph)
        budget.consume(action)

    return export_result(graph)
```

这只是操作骨架。它是否合理，取决于 [theoretical-foundation.md](theoretical-foundation.md) 中定义的问题状态、好问题标准、元动作价值和饱满条件能否成立。

## 8. 实现层次

在理论未完成前，不进入完整实现。可接受的落地层次是：

```text
Level 0: 文档规范层
  定义状态、solver、控制循环、饱满条件。

Level 1: 离线 JSON/YAML 状态机
  LLM 对图提交 GraphPatch，不做 UI。

Level 2: CLI runner
  自动执行有限步 solver loop。

Level 3: 可视化工作台
  人类查看、修改、批准、冻结、合并节点。

Level 4: 多 agent / 多 solver 调度
  多模型或工具并行处理不同节点。
```

当前阶段只应推进 Level 0。
