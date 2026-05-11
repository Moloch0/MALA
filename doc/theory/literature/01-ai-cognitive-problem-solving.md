# 经典 AI / 认知科学中的问题、问题状态与问题形式化

> 来源说明：本文基本保留子代理关于经典 AI / 认知科学问题求解传统的原始梳理，仅做 Markdown 标题、公式和链接格式整理。本文不套用 MALA 既有框架，而是从 Newell & Simon、Russell & Norvig、classical planning / state-space search 等传统自身出发。

## 结论先行

在这一传统中，problem 不是泛指“有困难的事情”，而是一个可在状态空间中被尝试求解的形式化任务：从一个或多个初始状态出发，经由允许的操作 / 行动，找到一条满足约束并到达目标状态的路径。problem state 是求解者或算法当前所在的、被抽象出来的状态表示；它不是整个真实世界，而是足以支持规划 / 搜索的相关信息。problem formulation 是把现实任务或任务环境抽象成这种可搜索结构的过程，核心是决定哪些差异算作状态、哪些改变算作行动、什么算成功、路径如何计价。

在最标准的 Russell & Norvig / AIMA 表述中，一个 well-defined search problem 由五个构件定义：

- initial state
- actions
- transition model
- goal test
- path cost

Newell / Simon / Newell 的 problem-space 表述更心理学化：problem space 是 `states + operators` 的空间；problem 是在该空间中给定 initial states、goal states 和 path constraints，寻找一条合法路径。两者的共同核心是：

```text
状态、操作、初始条件、目标条件、合法性 / 代价标准。
```

这些构件在该传统内部通常被当作“定义一个经典搜索 / 规划问题所需的充分构件”，但不是所有“问题”的充分必要条件。它们对可离散化、目标明确、行动模型已知、结果可预测的问题非常强；对开放式、价值冲突、目标会变化、状态空间无法预先界定、行动后果不确定或需要重新定义问题本身的任务覆盖较弱。

## 1. Newell & Simon：Problem Space 传统

Newell & Simon 的核心贡献是把人类问题求解理解为在一个内部表征的 problem space 中搜索。更精确地说，问题求解不是直接在“真实世界”里操作，而是在一个由符号状态和算子构成的空间中进行心理操作；外部行动可以发生，但理论的中心对象是内部 problem space。

Newell 在 “Problem Space as a Fundamental Category” 中写道，problem space 由 states 与 operators 构成：operators 接收一个 state 作为输入并产生一个 state 作为输出，operator 可以是 partial，即并非对所有状态都定义。原文短引：“A problem space consists of a set of symbolic structures ... and a set of operators”。见 [Newell, “Problem Space as a Fundamental Category”](https://iiif.library.cmu.edu/file/Newell_box00018_fld01301_doc0001/Newell_box00018_fld01301_doc0001.pdf)。

同一文献随后把 problem 定义为 problem space 中的一个求路任务：给定一组 initial states、一组 goal states，以及 path constraints，求一条从初始状态出发、满足路径约束、到达目标状态的路径。

由此可得 Newell / Simon 传统中的最小构件：

| 概念 | 在 Newell / Simon 传统中的含义 |
|---|---|
| Problem space | 一组可表征的状态，以及作用于这些状态的 operators |
| Problem state | problem space 中的一个符号结构；可以是当前状态、中间状态、初始状态或目标状态 |
| Operator | 把一个状态转换为另一个状态的心理 / 符号操作；可以是部分定义的 |
| Initial state(s) | 求解过程可以开始的状态 |
| Goal state(s) | 可识别为成功或目标达成的状态 |
| Path constraints | 路径必须满足的合法性约束；有时可以显式列出，有时被编码进 operator |
| Search control / heuristic knowledge | 决定如何选择下一步 operator 或候选状态的控制知识；它影响效率与成功率，但不是 problem space 本身 |

这里要注意两个重要点。

第一，problem space 与 problem 不是同一件事。problem space 是“可在其中移动的空间”，同一个 problem space 可以承载多个具体 problem；同一个外部任务也可以被表征为多个不同 problem space。Newell 在 Tower of Hanoi 例子中明确说 “Other problem spaces are possible”，例如可以把移动圆盘作为一个原子操作，也可以把它拆成拿起、移动手、放下等更细操作。

第二，problem space 是心理表征，不等同于外部任务环境。Newell 明确说 problem space and problem are mental constructs，虽然它们可能导向外部行动。也就是说，认知科学关心的是求解者如何表征任务，而不仅是任务客观上有什么规则。

## 2. 充分必要性判断

在 Newell / Simon 传统内部，如果一个求解者能够表征 states、执行 operators、识别 initial / goal / constraints，并把行为控制为在该空间中尝试求解，那么可以说他“在该 problem space 中有一个 problem”。这对“有一个可尝试的问题”是近似充分的。

但它不是“求解成功”的充分条件。成功还取决于搜索控制知识、启发式、记忆资源、空间大小、operator 粒度等。Newell 明确区分 problem space 与 search control knowledge；有空间并不等于知道如何高效穿过空间。

它也不是所有问题类型的必要条件。Simon 后来讨论 ill-structured problems 时承认 well-structured 与 ill-structured 的边界是 “vague, fluid”。见 Herbert A. Simon, [“The Structure of Ill Structured Problems”](https://www.sciencedirect.com/science/article/pii/0004370273900118), *Artificial Intelligence*, 1973。

## 3. Russell & Norvig：Problem Formulation 与 Classical Search

Russell & Norvig 在 *Artificial Intelligence: A Modern Approach* 的经典搜索章节中，把问题求解 agent 的流程概括为：

```text
formulate -> search -> execute
```

即先形成 goal 与 problem，再调用 search，得到 action sequence，然后执行。AIMA 第 3 章明确说 search 是寻找达到目标的 action sequence。见 [Russell & Norvig, AIMA 3e, sample chapters](https://www.pearsonhighered.com/assets/samplechapter/0/1/3/6/0136042597.pdf)。

AIMA 对 well-defined problem 的标准定义是五个构件：

| 构件 | 定义 | 作用 |
|---|---|---|
| Initial state | agent 开始所在的状态 | 给搜索树 / 状态空间路径一个起点 |
| Actions | 在某个状态下可执行的行动集合，通常写作 `ACTIONS(s)` | 定义从当前状态可以尝试什么 |
| Transition model | 描述行动效果的模型，通常写作 `RESULT(s, a)` | 定义行动如何把状态变成后继状态 |
| Goal test | 判断某状态是否为目标状态的函数 | 终止条件 / 成功判据 |
| Path cost | 给路径赋数值代价的函数，常由 step cost 累加 | 定义解的质量与 optimality |

AIMA 还指出，initial state、actions、transition model 共同隐式定义 state space，即从初始状态经任意行动序列可达的所有状态集合；state space 形成 directed graph，nodes 是 states，links 是 actions。

AIMA 的 solution 定义也很关键：solution 是从 initial state 通向 goal state 的 action sequence；optimal solution 是所有 solution 中 path cost 最低者。

## 4. Problem Formulation 的含义

Problem formulation 不是简单“写出问题描述”，而是把真实任务抽象成可搜索模型。AIMA 明确说 Bucharest 路线问题的 formulation “is still a model, an abstract mathematical description, and not the real thing”。它还说明 abstraction 是移除无关细节，例如真实旅行中广播、天气、风景、警察等都可能是 world state 的一部分，但若与找路线无关，就从 search state 中省略。

因此，problem formulation 的核心工作是选择抽象层级：

| 要决定的问题 | 例子 |
|---|---|
| 哪些世界差异进入 state？ | 路线规划中只保留城市位置，不保留车内音乐 |
| 哪些变化被建模为 action？ | `Go(Arad, Sibiu)`，而不是转方向盘三度 |
| 行动结果是否可预测？ | `RESULT(In(Arad), Go(Zerind)) = In(Zerind)` |
| 什么算目标？ | 到达 Bucharest，或满足 checkmate 属性 |
| 什么算好？ | 最短距离、最少步数、最低成本、最快时间 |

AIMA 对“好抽象”也给出判断标准：有效 abstraction 要保证抽象解可以扩展为真实世界中的解；有用 abstraction 要使抽象 action 比原问题更容易执行。

## 5. Problem State、World State、Search Node 的区别

Berkeley CS188 教材对这个区别说得很清楚：world state 包含给定状态的一切信息，而 search state 只包含 planning 所需的信息。见 [UC Berkeley CS188, State Spaces and Search Problems](https://inst.eecs.berkeley.edu/~cs188/textbook/search/state.html)。

在经典搜索中还要区分 state 与 node：

| 概念 | 含义 |
|---|---|
| State / problem state | 世界的抽象配置，例如 Pacman 的坐标和剩余食物布尔值 |
| Search node | 搜索树中的节点，通常包含 state、parent、action、path cost 等 |
| State-space graph | 每个 state 通常只出现一次 |
| Search tree | 同一 state 可以因不同路径出现多次，因为 node 编码了到达该 state 的路径 |

Berkeley CS188 也明确说 search tree node 不只编码状态，还编码从 start state 到该状态的整条 path / plan。

## 6. Planning / Search 中的最小必要构件

从 classical search 与 classical planning 的共同形式看，最小结构可以写成：

```math
P = \langle S, A, T, s_0, G, c \rangle
```

其中：

| 符号 | 名称 | 含义 |
|---|---|---|
| `S` | State space | 所有可能或可达的状态 |
| `s_0` | Initial state | 起点 |
| `A(s)` | Actions | 状态 `s` 下可用行动 |
| `T` 或 `RESULT` | Transition model | `T(s,a)=s'`，行动后的状态 |
| `G` 或 GoalTest | Goal condition / goal test | 判断 `s` 是否满足目标 |
| `c` | Step cost / path cost | 行动或路径代价 |

更偏 planning 的 STRIPS / PDDL 传统通常把 domain 与 problem 分开：

| 层级 | 内容 |
|---|---|
| Domain model | predicates / variables + operators / actions |
| Problem instance | objects + initial state + goal |

Cambridge Knowledge Engineering Review 对 classical planning 的概括是：在静态、确定、完全可观察环境中，寻找一个 action sequence，把 given initial state 转换为 desired goal state。见 [Reformulation techniques for automated planning: a systematic review](https://www.cambridge.org/core/journals/knowledge-engineering-review/article/reformulation-techniques-for-automated-planning-a-systematic-review/E212DBCBDA3179FC41BFAD86A8E4332F)。

STRIPS 表述更具体：一个 planning problem 可写为：

```math
\langle P,O,I,G\rangle
```

其中 `P` 是变量 / predicates，`O` 是 actions，`I` 是 initial state，`G` 是 goal。见 Carlo Liberatore, [Planning languages: STRIPS, SAS+, PDDL](https://www.diag.uniroma1.it/liberato/planning/languages/languages.html)。

## 7. 这些构件是否被视为充分必要？

### 在经典搜索问题内部：基本上是定义性的充分必要

对 AIMA 所说的 well-defined classical search problem，五个构件 initial state、actions、transition model、goal test、path cost 被当作“定义问题”的构件。少一个通常就不能完整运行标准搜索算法：

| 缺失项 | 后果 |
|---|---|
| 没有 initial state | 搜索没有起点 |
| 没有 actions | 不知道从状态能做什么 |
| 没有 transition model | 无法生成后继状态 |
| 没有 goal test | 不知道何时成功 |
| 没有 path cost | 可以找可行解，但无法定义最优解；若只关心 satisficing，可弱化 |

所以，对“求一个从起点到目标的最低代价行动序列”这类问题，五元组是充分的，也是近似必要的。

### 在 Newell / Simon 认知传统内部：对“能在一个空间中尝试问题”是充分

`states + operators + initial / goal / constraints` 足以把任务表征为 problem in a problem space。但是否能求出解，还取决于启发式、控制策略、工作记忆、表征质量和问题规模。

### 在更广义的 AI / 认知问题中：不是必要，也不是充分

很多问题并不自然满足单一 initial state、确定 transition、明确 goal test、可加 path cost 的结构。AIMA 自己也说明，经典搜索处理的是一类特定问题：observable、deterministic、known environments，solution 是 action sequence。也就是说，AIMA 并未声称五构件覆盖所有智能问题。

## 8. 该传统强覆盖的问题类型

| 类型 | 特征 | 例子 |
|---|---|---|
| Puzzle / toy problems | 规则清楚、状态离散、目标明确 | Tower of Hanoi、8-puzzle、missionaries and cannibals |
| Route / path planning | 状态是位置，行动是移动，代价是距离 / 时间 | Romania map 到 Bucharest |
| Classical planning | 完全可观察、确定、静态、行动模型已知 | Blocks world、STRIPS planning |
| Combinatorial search | 可枚举或隐式生成状态空间 | n-queens、TSP、scheduling 的某些形式 |
| Theorem proving / symbolic derivation | 状态是公式集合或证明状态，operator 是推理规则 | Logic Theorist、早期 GPS 任务 |

其共同点是：目标可以判定，行动可定义，状态差异可抽象，路径或最终状态可以评价。

## 9. 覆盖弱或无法充分覆盖的问题类型

这些不是说“完全不能形式化”，而是说用经典 problem-space / state-space search 直接覆盖会很弱，往往需要额外理论扩展，或者需要先把问题重新塑造成 well-structured problem。

### 9.1 Ill-Structured / Wicked Problems

这类问题的初始状态、目标状态、合法操作、评价标准都不完全给定，甚至会在求解过程中被重新定义。例如城市治理、组织战略、设计问题、政策冲突。问题在于，经典搜索要求先有 state space 和 goal test；而 ill-structured problem 的核心恰恰是“什么算状态、什么算目标、什么算好”尚未稳定。

### 9.2 Problem Finding / Problem Framing 本身

经典 formulation 假定可以把任务抽象成状态空间；但它较少解释“为什么这样定义问题而不是那样定义”。AIMA 承认 formulation 是 abstraction，是 model，不是真实任务本身；但 search 算法通常从 formulation 之后才开始。换言之，problem formulation 是前置的人类 / 设计活动，传统搜索理论对其自动化机制覆盖较弱。

### 9.3 开放式创造、设计、写作、科学发现

在这些任务中，goal state 可能不是预先可列举的集合，也未必有简单 goal test。目标可能是“优雅”“有说服力”“新颖且有用”“理论解释力强”。这类评价高度语境化，不能轻易化为可加 path cost。

### 9.4 动态、未知、部分可观察、随机环境

Classical search 假设行动结果已知、可预测，agent 执行 plan 时甚至可以忽略 percepts。对现实机器人、医疗决策、金融、网络安全等场景，状态不完全可知，transition model 不稳定，行动后果概率化，单纯 action sequence 不够，通常需要 belief state、policy、MDP / POMDP、online search、learning。

### 9.5 多主体、对抗、博弈和社会互动问题

若环境中有其他 agent，他们会响应、欺骗、协作或改变目标。此时 transition model 不是固定自然规律，而取决于其他主体的策略。经典单 agent search 可以扩展为 minimax、game tree、multi-agent planning，但原始 problem formulation 的“一个 agent 在状态空间中找路径”图景会变弱。

### 9.6 纯优化问题或偏好问题

AIMA 自己指出，很多 optimization problems 没有 goal test，也没有 path cost；例如演化中的 reproductive fitness 可被视为 objective function，但并没有清楚的目标测试和路径代价。因此，local search / optimization 只保留 state + neighbor relation + objective function，不再完全符合 classical search 的五构件。

### 9.7 连续、高维、难以离散化的问题

经典状态空间搜索天然适合离散符号状态。连续控制、运动规划、视觉-运动耦合、高维神经策略学习等可以离散化或抽象化，但状态空间爆炸、抽象有效性和行动粒度会成为主要问题。

### 9.8 目标会改变或价值冲突的问题

如果求解过程中目标本身改变，或者不同利益相关者对 goal test / path cost 有冲突，经典 formulation 需要先把冲突压缩成一个目标或一个代价函数。这常常不是技术步骤，而是政治、伦理、协商或制度设计问题。

## 10. 三个核心概念的综合定义

### Problem

在经典 AI / 认知科学问题求解传统中，problem 是一个在 problem space / state space 中定义的求路任务：给定起点、允许的操作、目标判据和路径约束 / 代价，寻找一个从初始状态到目标状态的操作序列。

更形式化地说：

```math
Problem = \langle S, A, T, s_0, G, c \rangle
```

或在 Newell 式表述中：

```math
ProblemSpace = \langle States, Operators \rangle
```

```math
Problem = \langle InitialStates, GoalStates, PathConstraints \rangle
\text{ within a ProblemSpace}
```

### Problem State

Problem state 是 problem space 中的一个状态表示。它不是完整世界，而是为求解目的保留的相关变量配置。它可以表示当前局面、中间局面、初始局面或目标局面。

| 任务 | Problem state 可以是什么 |
|---|---|
| Tower of Hanoi | 每个盘子在哪根柱子上 |
| Route planning | 当前所在城市 |
| 8-puzzle | 每个 tile 与 blank 的位置 |
| Pacman eat-all-dots | Pacman 坐标 + 每个 dot 是否已吃 |
| STRIPS blocks world | 一组当前为真的 predicates |

重要区别：problem state 不等于 search node。state 是局面；node 是搜索数据结构，通常还包括父节点、到达该状态的 action、累计 path cost 等。

### Problem Formulation

Problem formulation 是把任务环境抽象成 problem 的过程。它决定：

| 问题 | formulation 中的选择 |
|---|---|
| 什么被算作状态？ | state abstraction |
| 什么被算作行动？ | action abstraction |
| 行动如何改变状态？ | transition model |
| 什么算成功？ | goal test / goal condition |
| 什么算更好？ | path cost / objective |
| 哪些真实细节被忽略？ | abstraction boundary |
| 抽象是否有效？ | 抽象解能否扩展为真实解 |

AIMA 的关键提醒是：formulation 是 model，不是真实世界本身。好的 formulation 要尽量少保留细节，但不能删掉影响目标达成的关键差异。

## 11. 最小必要构件与充分必要性的最终归纳

| 传统 / 场景 | 最小构件 | 是否充分？ | 是否必要？ |
|---|---|---|---|
| Newell / Simon problem space | states, operators；具体 problem 还需 initial states, goal states, path constraints | 足以表征一个可尝试的问题；不足以保证求解成功 | 对该理论内部的问题空间解释是必要的；对所有问题不是 |
| AIMA classical search | initial state, actions, transition model, goal test, path cost | 足以定义 well-defined search problem，并作为搜索算法输入 | 对最低代价路径搜索近似必要；对 satisficing 可弱化 path cost |
| Classical planning / STRIPS | predicates / variables, operators, initial state, goal；可选 action cost | 足以定义 classical deterministic planning instance | 对 classical planning 必要；对 probabilistic / contingent / temporal planning 不足 |
| Local search / optimization | state space, neighbor relation, objective function | 对优化问题充分 | goal test / path cost 不一定必要 |
| CSP | variables, domains, constraints | 对 constraint satisfaction 充分 | initial/action/path 不必要，除非转写为搜索 |
| MDP / RL | states, actions, transition probabilities, rewards, policy criterion | 对随机序贯决策更合适 | goal test 不一定必要，path cost 被 reward / return 替代 |

## 12. 可核查资料与书目

1. Allen Newell & Herbert A. Simon. *Human Problem Solving*. Englewood Cliffs, NJ: Prentice-Hall, 1972. [Open Library 条目](https://openlibrary.org/works/OL4465098W?edition=humanproblemsolv0000newe)。
2. Allen Newell. “Problem Space as a Fundamental Category.” [CMU archival PDF](https://iiif.library.cmu.edu/file/Newell_box00018_fld01301_doc0001/Newell_box00018_fld01301_doc0001.pdf)。
3. Stuart Russell & Peter Norvig. *Artificial Intelligence: A Modern Approach*, 3rd ed., Chapter 3 “Solving Problems by Searching,” Chapter 4 “Beyond Classical Search.” [Pearson sample chapters PDF](https://www.pearsonhighered.com/assets/samplechapter/0/1/3/6/0136042597.pdf)。
4. UC Berkeley CS188. “State Spaces and Search Problems.” [CS188 textbook page](https://inst.eecs.berkeley.edu/~cs188/textbook/search/state.html)。
5. UC Berkeley CS188. Spring 2026 lecture slides on informed search. [CS188 lecture PDF](https://inst.eecs.berkeley.edu/~cs188/sp26/assets/lectures/cs188-sp26-lec03.pdf)。
6. Herbert A. Simon. “The Structure of Ill Structured Problems.” *Artificial Intelligence*, 4(3-4), 181-201, 1973. DOI: `10.1016/0004-3702(73)90011-8`. [ScienceDirect page](https://www.sciencedirect.com/science/article/pii/0004370273900118)。
7. Jussi Rintanen. *Introduction to Automated Planning* course script. [Course script PDF](https://users.aalto.fi/~rintanj1/FreiburgAIPcourse/script.pdf)。
8. Carlo Liberatore. “Planning languages: STRIPS, SAS+, PDDL.” [Planning languages notes](https://www.diag.uniroma1.it/liberato/planning/languages/languages.html)。
9. “Reformulation techniques for automated planning: a systematic review.” *The Knowledge Engineering Review*. [Cambridge Core article](https://www.cambridge.org/core/journals/knowledge-engineering-review/article/reformulation-techniques-for-automated-planning-a-systematic-review/E212DBCBDA3179FC41BFAD86A8E4332F)。

## 最终概括

经典 AI / 认知科学的问题求解传统把 problem 看成“在一个可表征状态空间中寻找从初始状态到目标状态的合法 / 低成本路径”。problem state 是这个空间中的一个抽象局面，不是完整世界。problem formulation 是把现实任务压缩为 states、actions / operators、transition model、goal test、path cost / constraints 的建模过程。

这套传统的强项是：清晰、可计算、可比较算法、能解释很多 puzzle、规划、路径搜索、符号推理任务。它的弱项是：它通常要求问题已经被良好结构化，而许多现实问题的难点恰恰在于状态、目标、行动、价值和边界尚未被确定。对于这些问题，经典传统往往只能覆盖被结构化之后的子问题，而不能充分解释“问题如何被发现、框定、协商和重构”。
