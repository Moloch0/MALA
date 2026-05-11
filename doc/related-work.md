# Related Work：从已有工作到 MALA-Graph 的缺口

本文整理 MALA-Graph 周边的相关工作。这里的目标不是做完整文献史，而是回答一个更窄的问题：

> 已有工作各自覆盖了 MALA-Graph 的哪一部分？它们为什么还不足以替代 MALA-Graph？

MALA-Graph 的核心位置可以概括为：它不是单纯的论证图、任务流图、推理搜索树或多智能体编排图，而是试图把“问题如何被构造、修正、检验并进入求解”表示成一个可检查、可搜索、可执行、可回代修正的图结构。

因此，下面每一类工作都覆盖 MALA-Graph 的一部分，但都留下不同缺口。本文在每个引用下都明确说明两点：

- 它覆盖了 MALA-Graph 的哪一部分；
- 它为什么还不能替代 MALA-Graph。

## 1. IBIS / gIBIS / Compendium

IBIS（Issue-Based Information System）传统把复杂公共问题、设计问题或协作讨论中的 issue、position、argument 显式组织成网络。它给 MALA-Graph 的直接启发是：问题不应只藏在线性文本或对话上下文里，而应成为可指认、可追踪、可修改的一等对象。

- [Kunz 与 Rittel, *Issues as Elements of Information Systems*](https://escholarship.org/uc/item/5cj786v8) 是 IBIS 的源头工作，把 issue 作为信息系统中的基本元素，用于支持复杂政治/规划决策过程中的问题识别、结构化和讨论。
  - 覆盖 MALA-Graph 的部分：它覆盖了“问题图化”的最早一层，即把争议点、候选立场和相关论据从连续文本中抽出，形成可导航的讨论结构。
  - 不能替代 MALA-Graph 的原因：IBIS 的核心目标是协作讨论和议题组织，不是判断一个问题节点是否已达到可求解、最小充分、控制闭合或因果稳定的状态；它也不规定何时应澄清、分解、检索、求解或停止。

- [Conklin 与 Begeman, *gIBIS: A Hypertext Tool for Exploratory Policy Discussion*](https://doi.org/10.1145/58566.59297) 将 IBIS 实现为超文本协作工具，用 typed IBIS networks 支持大型复杂问题中的早期设计 deliberation。
  - 覆盖 MALA-Graph 的部分：它覆盖了“可交互的问题-立场-论据网络”和协作记忆机制，说明问题构造过程可以被工具化、浏览、增量编辑和多人共享。
  - 不能替代 MALA-Graph 的原因：gIBIS 仍主要服务于讨论记录与浏览，而不是为问题状态提供形式化类型、质量判准和价值驱动的下一步动作选择；它不会把“当前 issue 是否已经可进入求解”作为中心控制对象。

- [Conklin, Selvin, Shum 与 Sierhuis, *Facilitated Hypertext for Collective Sensemaking: 15 Years on from gIBIS*](https://doi.org/10.1145/1111449.1111475) 总结了从 gIBIS 到 Compendium 的协作 sensemaking 工具传统，强调用可视化超文本支持会议、项目知识和集体理解。
  - 覆盖 MALA-Graph 的部分：它覆盖了“群体 sensemaking 的可视化工作区”，对 MALA-Graph 中多人/多 agent 共享问题图、记录问题演化和保留讨论来龙去脉有直接启发。
  - 不能替代 MALA-Graph 的原因：Compendium 风格的工具强调知识建模、会议捕获和观点组织，但不把问题表述本身形式化为带对象、未知量、判准、约束、状态抽象和证据需求的节点；它也没有把元层动作的成本收益作为图扩展原则。

这条传统的贡献是把问题、立场和论据图化。MALA-Graph 需要在此基础上前进一步：把“讨论图”升级为“问题构造图”。节点不只表示 issue、answer、argument，还要表示任务、对象、未知量、判准、约束、状态抽象、证据需求、澄清动作与求解动作；边也不只表示支持/反驳，还要表示重述、分解、合并、抽象、检索、求解和回代。

## 2. GSN / Assurance Cases

GSN（Goal Structuring Notation）和 assurance cases 把系统安全性、可靠性或合规性主张组织成可审查的论证结构。它们与 MALA-Graph 的共同点是：都关心主张、上下文、假设、证据和分解策略之间的显式关系。

- [Kelly 与 Weaver, *The Goal Structuring Notation - A Safety Argument Notation*](https://www.researchgate.net/publication/228990118_The_goal_structuring_notation-a_safety_argument_notation) 介绍 GSN 如何用 goal、strategy、context、solution 等元素表达安全论证。
  - 覆盖 MALA-Graph 的部分：它覆盖了“主张-策略-上下文-证据”的可审计论证链，为 MALA-Graph 记录某个问题 framing 依赖哪些假设、哪些证据支撑该 framing 提供了重要模板。
  - 不能替代 MALA-Graph 的原因：GSN 通常从一个较稳定的顶层 claim 或 goal 出发，关注如何论证该主张可信；MALA-Graph 更上游，关心 goal/problem 本身如何被发现、修正、拆分，以及什么时候应该从问题构造转入求解。

- [GSN Community Standard](https://scsc.uk/scsc-141C) 给出了 GSN 的标准化符号、语法和用法，是 assurance case 社群维护的规范入口。
  - 覆盖 MALA-Graph 的部分：它覆盖了“图式论证语言的标准化”这一层，说明主张、策略、上下文、假设、证据和未解决节点可以被规范化为可交换、可审查的结构。
  - 不能替代 MALA-Graph 的原因：GSN 标准规定的是 assurance argument 的表示法，而不是问题构造动作的运行语义；它不定义“好问题”的最小充分性、控制闭合性、信息价值或答案回代规则。

- [OMG, *Structured Assurance Case Metamodel (SACM)*](https://www.omg.org/spec/SACM/) 提供 assurance case 的建模标准，用于表达 argumentation、evidence 和 artifact 之间的关系。
  - 覆盖 MALA-Graph 的部分：它覆盖了“可机器处理的论证/证据元模型”，对 MALA-Graph 将证据、假设、来源和审计轨迹纳入图结构有参考价值。
  - 不能替代 MALA-Graph 的原因：SACM 面向 assurance case 的交换和建模，不面向问题空间的生成、修正和控制；它不会告诉系统何时应重写问题、追问约束、合并等价问题或拒绝在错误 framing 下继续回答。

GSN/assurance cases 可以增强 MALA-Graph 的审计能力，但不能替代 MALA-Graph。MALA-Graph 需要把“对结论的论证”前移到“对问题表述的论证”：不仅问答案有没有证据，还要问这个答案所在的问题空间是否已经被正确构造。

## 3. Blackboard Architecture

Blackboard architecture 起源于早期 AI 系统。其基本思想是：多个知识源围绕一个共享黑板工作，每个知识源根据当前黑板状态贡献局部推断、假设或修改，再由控制机制决定下一步激活哪个知识源。

- [Erman, Hayes-Roth, Lesser 与 Reddy, *The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty*](https://doi.org/10.1145/356810.356816) 展示了 Hearsay-II 如何把多种知识源集成到共享黑板上，以处理语音理解中的不确定性。
  - 覆盖 MALA-Graph 的部分：它覆盖了“多知识源围绕共享状态增量协作”的运行架构。MALA-Graph 中的澄清、分解、检索、反例生成、约束检查、候选问题重写和答案回代，都可以视为不同知识源对共享图状态的操作。
  - 不能替代 MALA-Graph 的原因：Hearsay-II 的黑板节点服务于语音理解任务中的分层假设，不提供通用的问题构造语义；它不区分对象层求解与元层问题修正，也不定义问题节点的最小充分、控制闭合或信息价值。

- [Nii, *Blackboard Systems*](https://doi.org/10.1609/aimag.v7i3.537) 系统总结了 blackboard 模型的组成：知识源、黑板数据结构和控制机制。
  - 覆盖 MALA-Graph 的部分：它覆盖了“黑板 + 知识源 + 控制”的架构分解，说明一个系统可以把推理过程设计成对公共工作区的反复改写。
  - 不能替代 MALA-Graph 的原因：blackboard 是通用协作架构，不规定黑板内容必须是问题、未知量、判准、约束、状态抽象或证据缺口；控制策略也通常是启发式或任务特化的，而不是围绕问题构造动作的预期价值来选择。

Blackboard architecture 可作为 MALA-Graph 的运行时参考，但 MALA-Graph 需要的是“带问题构造语义的 blackboard”。图中每类节点和边都应有明确的问题构造角色，而不仅是任意中间假设或工作产物。

## 4. Decision Analysis / Value of Information / Metareasoning

决策分析、Value of Information（VOI）和 metareasoning 为 MALA-Graph 提供策略层基础：问题构造动作也应像信息获取、计算和规划一样，有成本、有收益，并且需要停止规则。

- [Howard, *Information Value Theory*](https://doi.org/10.1109/TSSC.1966.300074) 从决策后果与不确定性出发讨论信息价值，奠定了“信息是否值得获取”这一决策分析问题。
  - 覆盖 MALA-Graph 的部分：它覆盖了“是否值得获取额外信息”的价值判准。MALA-Graph 中的检索、追问、实验或证据补充，都应被看作有成本的信息动作，而不是机械步骤。
  - 不能替代 MALA-Graph 的原因：经典 VOI 通常假定决策变量、状态变量、效用函数和信息结构已经给定；MALA-Graph 关心的是更上游的问题，即这些变量、目标、判准和约束是否已经被正确构造成问题空间。

- [Raiffa 与 Schlaifer, *Applied Statistical Decision Theory*](https://mitpress.mit.edu/9780262180131/applied-statistical-decision-theory/) 是统计决策理论和贝叶斯决策分析的重要基础，系统处理不确定性下的行动、后果和信息。
  - 覆盖 MALA-Graph 的部分：它覆盖了“在不确定性、行动和效用之间进行规范选择”的对象层决策框架，可为 MALA-Graph 中某些已成形问题的求解和信息价值评估提供数学基础。
  - 不能替代 MALA-Graph 的原因：该框架的前提通常是问题已经被建模为决策问题；MALA-Graph 还要处理建模之前的工作：用户到底在问什么、目标是否混合、判准是否缺失、状态抽象是否错误、是否应先重述或拆分问题。

- [Russell 与 Wefald, *Principles of Metareasoning*](https://doi.org/10.1016/0004-3702(91)90015-C) 把计算和推理本身视为有成本的行动，提出用决策理论分析计算动作的价值。
  - 覆盖 MALA-Graph 的部分：它覆盖了“推理动作也要按预期效用选择”的元层控制思想。MALA-Graph 的澄清、分解、检索、求解和回代都可以被视为元层动作。
  - 不能替代 MALA-Graph 的原因：metareasoning 讨论如何选择计算或推理动作，但不提供问题图的数据模型；它不定义什么是问题节点、问题边、问题质量判准，也不直接处理“问题表述是否写对”这一中心对象。

- [Horvitz, *Reasoning about Beliefs and Actions under Computational Resource Constraints*](https://doi.org/10.1016/0004-3702(87)90003-1) 以及相关 bounded rationality 工作把资源限制纳入智能系统的推理和行动选择。
  - 覆盖 MALA-Graph 的部分：它覆盖了“有限时间、有限计算和有限交互下的理性控制”，提醒 MALA-Graph 不能无限追问、无限分解或无限检索。
  - 不能替代 MALA-Graph 的原因：资源受限理性提供控制原则，但不提供问题构造语义层；它不能单独说明一个自然语言输入应该被改写成哪些问题节点、哪些约束、哪些证据缺口，以及答案如何回代检验原 framing。

这类工作给 MALA-Graph 的关键启发是：图上的下一步动作不应只是规则触发，而应近似求解一个元决策问题。MALA-Graph 需要把 VOI 从对象层事实获取扩展到元层问题构造：不仅评估“查这个事实是否值得”，还要评估“重写这个问题、拆分这个目标、追问这个约束、改变这个判准是否值得”。

## 5. LLM Reasoning / Search：Self-Ask, ReAct, ToT, GoT, RAP, LATS

近年的 LLM reasoning/search 工作把大模型从单步回答器扩展成能够显式组织中间问题、行动、搜索和反思的系统。它们与 MALA-Graph 的关系不是替代，而是可作为局部操作、搜索后端或执行策略。

- [Press et al., *Measuring and Narrowing the Compositionality Gap in Language Models* / Self-Ask](https://arxiv.org/abs/2210.03350) 让模型显式提出 follow-up questions，并可接入搜索引擎回答子问题。
  - 覆盖 MALA-Graph 的部分：它覆盖了“把复杂问题分解为显式子问题”的操作，可作为 MALA-Graph 中的分解或澄清动作。
  - 不能替代 MALA-Graph 的原因：Self-Ask 生成子问题并不等于判断原问题是否最小充分、是否控制闭合、是否包含错误判准；它仍主要服务于回答既定输入，而不是维护一个可审计的问题构造图。

- [Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629) 将 reasoning traces 与 actions 交织，使模型在推理中调用外部工具或环境反馈。
  - 覆盖 MALA-Graph 的部分：它覆盖了“推理-行动-观察循环”，可作为 MALA-Graph 中检索、工具调用和环境反馈的执行模式。
  - 不能替代 MALA-Graph 的原因：ReAct 的 action-observation 循环主要服务于任务执行；它不保证系统会审查问题 framing 是否正确，也不定义哪些观察应改变问题节点、证据状态、判准或约束。

- [Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*](https://arxiv.org/abs/2305.10601) 把中间 thought 组织成树，在多个候选推理路径之间搜索、评价和回溯。
  - 覆盖 MALA-Graph 的部分：它覆盖了“多候选路径搜索”和“非线性推理展开”，可作为 MALA-Graph 中某个已成形问题节点的求解后端。
  - 不能替代 MALA-Graph 的原因：ToT 的 thought 节点通常是求解路径上的中间文本，不是带对象、未知量、判准、约束和证据需求的问题节点；它关注如何解题，而不是先判断问题是否被写对。

- [Besta et al., *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*](https://arxiv.org/abs/2308.09687) 将 thought 从树扩展为任意图，支持合并、聚合、反馈循环和更复杂的 thought transformations。
  - 覆盖 MALA-Graph 的部分：它覆盖了“LLM 中间产物可以图结构化”的算法层，为 MALA-Graph 使用图而非链或树提供了直接技术邻近性。
  - 不能替代 MALA-Graph 的原因：GoT 的顶点是 LLM thoughts，边是 thought 依赖或变换；MALA-Graph 的顶点和边需要更强的问题构造语义，包括任务目标、状态抽象、证据缺口、求解状态和答案回代。

- [Hao et al., *Reasoning with Language Model is Planning with World Model* / RAP](https://arxiv.org/abs/2305.14992) 把推理看作规划问题，让 LLM 同时充当世界模型和 reasoning agent，并用 MCTS 进行搜索。
  - 覆盖 MALA-Graph 的部分：它覆盖了“用规划和价值估计指导推理搜索”的算法思路，可用于 MALA-Graph 中某些候选问题或候选答案路径的搜索。
  - 不能替代 MALA-Graph 的原因：RAP 的状态、动作、奖励和任务目标通常仍由外部问题设定；MALA-Graph 关心的是这些设定本身是否合理，以及是否应先修改问题空间再规划。

- [Zhou et al., *Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models* / LATS](https://arxiv.org/abs/2310.04406) 结合树搜索、反思和环境反馈，把 reasoning、acting 与 planning 统一到语言智能体搜索中。
  - 覆盖 MALA-Graph 的部分：它覆盖了“带反思和反馈的 agent tree search”，可作为 MALA-Graph 中执行、试错、评估候选路径的后端。
  - 不能替代 MALA-Graph 的原因：LATS 搜索的是行动/推理轨迹，不是问题构造状态本身；它不提供问题节点类型、问题质量判准、信息价值驱动的澄清策略，也不强制最终答案回代修正原问题图。

这些工作证明了 LLM 可以显式分解、搜索、行动、反思和使用工具。但它们多服务于“如何更好地求解既定问题”。MALA-Graph 要补的是：什么时候应调用这些操作、它们操作的是哪类问题节点、每次操作如何改变问题表述的可求解性，以及最终答案如何回代检验原问题是否被切对。

## 6. Agent Orchestration：AutoGen, MetaGPT, LangGraph, STORM

Agent orchestration 工作关注如何把多个 LLM agent、工具、角色和状态机组织成可运行系统。它们覆盖 MALA-Graph 的工程执行层，但通常不提供问题构造理论。

- [Wu et al., *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*](https://arxiv.org/abs/2308.08155) 提供多 agent 对话框架，使可定制 agent 通过自然语言和代码协作，并可结合人工输入和工具。
  - 覆盖 MALA-Graph 的部分：它覆盖了“多 agent 协作执行”和“人-模型-工具混合工作流”，可承载 MALA-Graph 中不同角色的澄清、检索、验证、生成和审计 agent。
  - 不能替代 MALA-Graph 的原因：AutoGen 定义的是对话式协作基础设施，不定义问题节点、问题边、问题质量标准或何时应停止澄清进入求解；多 agent 对话本身并不保证问题被正确构造。

- [Hong et al., *MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework*](https://arxiv.org/abs/2308.00352) 将软件开发等任务组织为产品经理、架构师、工程师等角色协作流程，把人类工作流引入 LLM 多 agent 系统。
  - 覆盖 MALA-Graph 的部分：它覆盖了“角色化分工”和“流程化产物生成”，对 MALA-Graph 中把澄清、分解、检索、求解、评审分配给不同 agent 有工程启发。
  - 不能替代 MALA-Graph 的原因：MetaGPT 的核心是把既定任务放进工程流程；它不提供通用的问题构造表示，也不判断用户原始任务是否混合了多个目标、缺少判准或需要先重写。

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/) 将 LangGraph 定位为构建 stateful、multi-actor、可循环、可分支 LLM 应用的低层编排框架。
  - 覆盖 MALA-Graph 的部分：它覆盖了“有状态图执行、条件边、循环、持久化和人工介入”的工程机制，非常适合作为 MALA-Graph 的运行时之一。
  - 不能替代 MALA-Graph 的原因：LangGraph 只提供图执行机制，图上的状态语义由应用自己定义；MALA-Graph 的贡献恰恰是定义问题构造图的节点/边语义、质量判准和转向/停止规则。

- [Shao et al., *Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models* / STORM](https://arxiv.org/abs/2402.14207) 提出通过检索、多视角提问和大纲合成来辅助长文写作；[Stanford STORM 项目页](https://storm-project.stanford.edu/research/storm/) 也说明了其 pre-writing 流程。
  - 覆盖 MALA-Graph 的部分：它覆盖了“面向写作的研究、提问、观点组织和大纲生成”，对 MALA-Graph 中的信息收集、观点覆盖和问题分解有启发。
  - 不能替代 MALA-Graph 的原因：STORM 的目标是生成高质量 Wikipedia-like 文章，问题构造服务于写作大纲；MALA-Graph 的目标更通用，是表示任意任务中问题空间如何被构造、验证、求解和回代修正。

这些框架可以承载 MALA-Graph，但不是 MALA-Graph 本身。MALA-Graph 的独立贡献不在“又做一个 agent 框架”，而在给 agent 工作流提供问题构造语义和停止/转向判准。

## 7. 汇总：已有工作覆盖范围与 MALA-Graph 缺口

| 类别 | 代表工作 | 已有工作覆盖什么 | 对 MALA-Graph 仍缺什么 |
| --- | --- | --- | --- |
| IBIS / gIBIS / Compendium | [Kunz & Rittel](https://escholarship.org/uc/item/5cj786v8), [gIBIS](https://doi.org/10.1145/58566.59297), [Compendium](https://doi.org/10.1145/1111449.1111475) | 问题、立场、论据的图式组织；协作讨论记忆；群体 sensemaking | 缺少问题表述质量标准、控制闭合、信息价值和可执行策略 |
| GSN / Assurance cases | [Kelly & Weaver](https://www.researchgate.net/publication/228990118_The_goal_structuring_notation-a_safety_argument_notation), [GSN Standard](https://scsc.uk/scsc-141C), [SACM](https://www.omg.org/spec/SACM/) | 主张、策略、上下文、假设、证据的审计链 | 默认目标较稳定，弱于动态发现和修正问题本身 |
| Blackboard architecture | [Hearsay-II](https://doi.org/10.1145/356810.356816), [Nii](https://doi.org/10.1609/aimag.v7i3.537) | 多知识源围绕共享状态协作；对公共工作区增量改写 | 缺少问题构造语义和元层动作价值评估 |
| Decision analysis / VOI / Metareasoning | [Howard](https://doi.org/10.1109/TSSC.1966.300074), [Raiffa & Schlaifer](https://mitpress.mit.edu/9780262180131/applied-statistical-decision-theory/), [Russell & Wefald](https://doi.org/10.1016/0004-3702(91)90015-C), [Horvitz](https://doi.org/10.1016/0004-3702(87)90003-1) | 信息获取、计算和停止规则的价值分析 | 通常假定问题结构已给定，弱于构造问题空间 |
| Self-Ask / ReAct / ToT / GoT / RAP / LATS | [Self-Ask](https://arxiv.org/abs/2210.03350), [ReAct](https://arxiv.org/abs/2210.03629), [ToT](https://arxiv.org/abs/2305.10601), [GoT](https://arxiv.org/abs/2308.09687), [RAP](https://arxiv.org/abs/2305.14992), [LATS](https://arxiv.org/abs/2310.04406) | LLM 的分解、行动、树/图搜索、规划与反思 | 多服务于求解既定问题，弱于审查原问题是否写对 |
| AutoGen / MetaGPT / LangGraph / STORM | [AutoGen](https://arxiv.org/abs/2308.08155), [MetaGPT](https://arxiv.org/abs/2308.00352), [LangGraph](https://langchain-ai.github.io/langgraph/), [STORM](https://arxiv.org/abs/2402.14207) | 多 agent、状态图、工具调用、复杂流程编排和研究写作流程 | 提供执行框架，但不提供“什么是好问题”的理论判准 |

由此可见，MALA-Graph 的空间不是凭空出现的。它位于几条传统的交汇处：

- 从 IBIS 继承问题图化；
- 从 GSN 继承证据和审计意识；
- 从 blackboard 继承共享工作区和多知识源协作；
- 从 VOI/metareasoning 继承元层动作的成本收益判断；
- 从 LLM reasoning/search 继承显式分解、搜索、反思和工具反馈；
- 从 agent orchestration 继承可运行的状态图和流程控制。

但这些传统还没有合成一个统一对象：

> 一个以“问题构造”为中心，能同时表示问题语义、证据状态、搜索动作、信息价值、执行流程和回代检验的图结构。

这就是 MALA-Graph 要填补的缺口。

## 8. MALA-Graph 的最小差异化命题

为了避免把 MALA-Graph 说成一个过大的万能框架，可以把它的差异化收紧为四个命题。

### 8.1 问题节点不是普通文本节点

在 MALA-Graph 中，一个问题节点至少应显式携带：

- 对象：问题谈论的是什么；
- 未知量：真正要求解的是什么；
- 任务目标：求解结果服务于什么控制或判断；
- 判准：什么算好答案或有效推进；
- 约束：时间、成本、资源、范围和背景条件；
- 状态抽象：哪些差别被保留，哪些差别被合并；
- 证据需求：还缺什么信息才能进入求解或判断；
- 当前状态：已成形、待澄清、待拆分、待检索、可求解或应拒答。

这使它不同于一般 argument node、thought node 或 workflow state。

### 8.2 边表示问题构造动作，而不只是关系

MALA-Graph 中的边不应只表示“支持”“反对”“下一步”。它还应表达：

- 澄清：补足缺失对象、约束或判准；
- 重述：把模糊输入改写成可操作问题；
- 分解：把混合问题拆成多个任务；
- 合并：把等价或冗余子问题收束；
- 抽象：把历史或上下文压缩成状态表示；
- 检索：为某个证据缺口获取信息；
- 求解：在已成形问题内生成答案；
- 回代：用答案检查原问题 framing 是否错误。

这使 MALA-Graph 不只是知识图或工作流图，而是问题状态转移图。

### 8.3 下一步动作需要价值判准

MALA-Graph 不应机械地总是追问、总是分解或总是检索。每一步都应近似回答：

> 这个元层动作对后续求解质量的预期提升，是否超过它的成本？

这使它与普通 prompt decomposition 或 agent pipeline 区分开来。关键不是“步骤更多”，而是“步骤是否值得”。

### 8.4 答案必须回到问题图中

MALA-Graph 不把最终回答当作流程终点。一个答案生成后，至少还应回代检查：

- 它是否回答了当前问题节点的未知量；
- 它是否满足原先判准；
- 它是否暴露出任务目标或状态抽象错误；
- 它是否需要拆出新问题；
- 它是否改变某些假设、证据状态或边权重。

这使 MALA-Graph 从“生成答案的流程图”变成“问题构造-求解-回代修正”的闭环。

## 9. 结论

现有工作已经分别证明了很多关键部件是可行的：问题可以图化，论证可以审计，多知识源可以协作，信息获取可以按价值评估，LLM 推理可以搜索化，agent 系统可以流程化。

但 MALA-Graph 的核心缺口仍然存在：这些部件尚未围绕“问题是否被写对”这一中心对象统一起来。MALA-Graph 要补的不是又一种更复杂的推理提示词，也不是又一个多智能体框架，而是一个更基础的表示层：

> 把问题构造本身表示为可审查、可搜索、可执行、可回代修正的图。

如果 MALA 的理论主张是“回答是在既定问题空间中取值，提问是在构造这个空间”，那么 MALA-Graph 的工程主张就是：

> 让这个空间的构造过程不再只停留在隐含对话里，而成为显式图对象。
