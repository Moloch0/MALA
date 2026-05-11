# 劣构问题、棘手问题、设计理论与问题结构化方法

> 来源说明：本文基本保留子代理关于 ill-structured problems / wicked problems / design theory / problem structuring methods 的原始梳理，仅做 Markdown 标题、链接和表格格式整理。本文不套用 MALA 既有框架，而是从 Simon、Rittel & Webber、Jonassen、Checkland SSM、Rosenhead / Mingers PSM 等传统自身出发。

## 结论先行

不套用外部框架，只从这条传统内部看，“问题”不是一个天然摆在那里的对象，而是一个由主体在情境中构成的、面向行动的差异或未知。它的最小构成可以压缩为：

1. **情境 / 当前状态**：某个现实、任务或社会情境被遭遇到。
2. **主体 / 关切者**：至少有人把它感知为值得处理；在劣构、棘手问题中通常是多主体。
3. **差异、未知或不满意**：当前状态与目标、需要、偏好状态、规范性判断之间存在落差，或存在一个值得求解的未知。
4. **行动取向**：问题不是纯描述，而是暗含“要做些什么”或“如何改变”的方向。
5. **表征 / 框定**：必须把情境组织成某种问题空间、根定义、认知图、概念模型或论证框架。
6. **评价依据**：要能以某种方式判断方案、行动或改善是否可接受；劣构问题中评价标准常常多元、争议、变化。
7. **因果 / 后果假设**：行动为何会改变情境、会带来什么后果，必须被某种模型、信念或判断连接起来；劣构问题中这部分往往最不稳定。

因此，**劣构问题的最小构成**不是“缺少结构”本身，而是：一个被主体认为值得行动的情境性差异 / 未知，其中目标、边界、约束、可行动作、评价标准、相关知识或后果关系中至少有关键部分不能在求解前稳定给定，并且会在求解、争论、建模或行动中继续被重构。若再进入 Rittel-Webber、SSM、PSM 的社会规划传统，劣构还通常包含多主体、多视角、价值冲突和不可完全回滚的社会后果。

## 1. Simon：劣构是相对于问题空间和求解器能力的未定性

Herbert Simon 的核心文献是 [“The Structure of Ill Structured Problems”](https://iiif.library.cmu.edu/file/Simon_box00085_fld06830_bdl0008_doc0001/Simon_box00085_fld06830_bdl0008_doc0001.pdf)，*Artificial Intelligence*, 1973，DOI: [10.1016/0004-3702(73)90011-8](https://doi.org/10.1016/0004-3702(73)90011-8)。Simon 明说 ill-structured problem 是一个 “residual concept”，也就是通过“不满足良构问题条件”来识别。

在 Simon 那里，一个良构问题大致需要：

- 明确的测试标准；
- 可表征初始状态、目标状态和中间状态的问题空间；
- 可表征的合法动作 / 状态转换；
- 相关知识能进入问题空间；
- 外部世界行动后果能被问题空间准确反映；
- 这些过程在实践上可计算、可搜索。

由此反推，劣构问题并不是完全没有结构，而是这些要素的某些部分不稳定、不可穷尽、无法预先表征或超出求解器可操作能力。

Simon 的最小问题构成是偏认知和计算的：

```text
初始状态、目标状态、状态空间、操作符、知识表征、评价标准、求解器能力。
```

劣构的最小条件则是其中任一关键构件无法预先充分给定，例如建筑设计中没有明确测试标准，问题空间也会被新材料、新形式、新需求不断突破。

充分必要性方面，Simon 明确否认严格边界。他说良构与劣构之间的边界是模糊和流动的；良构问题的条件只是 “some or all” 的特征，不是形式化定义。因此这些构件在 Simon 那里是**启发式判据**，不是充分必要条件。

覆盖弱点：Simon 的框架强于解释个人或人工智能求解器如何在巨大知识空间中处理未定性，但弱于处理价值冲突、权力、合法性、责任、不可逆社会后果等问题。也就是说，它能把建筑设计、棋局、机器人行动等都看成相对于求解器能力的劣构，却较少说明为什么公共政策问题中的“谁有权定义问题”“谁承担后果”本身就是问题的一部分。

## 2. Rittel & Webber：棘手问题是社会规划中定义、求解和评价不可分的困境

Horst Rittel 与 Melvin Webber 的核心文献是 [“Dilemmas in a General Theory of Planning”](https://urbanpolicy.net/wp-content/uploads/2015/06/Rittel-Webber_1973_DilemmasInAGeneralTheoryOfPlanning.pdf)，*Policy Sciences*, 1973，DOI: [10.1007/BF01405730](https://doi.org/10.1007/BF01405730)。他们区分 tame problems 与 wicked problems，强调社会规划问题不是自然科学或工程中的可分解问题。短引一句即可概括其立场：“The formulation of a wicked problem is the problem!”

Rittel-Webber 的 wicked problem 最著名的是十条特征：

1. 没有 definitive formulation。
2. 没有 stopping rule。
3. 方案不是 true/false，而是 good/bad。
4. 无法立即或最终检验全部后果。
5. 每次尝试都是 one-shot operation。
6. 没有可穷尽方案集合。
7. 每个问题本质上独特。
8. 每个问题都可看成另一个问题的症状。
9. 解释方式多样且解释决定解决方向。
10. 规划者无权犯错。

由这些特征反推，wicked problem 的最小构成是：

```text
一个被视为“现状与应然状态不一致”的社会差异；
多个有资格评价的公众或利益相关方；
对差异的竞争性解释；
不可穷尽的处理方案；
依赖判断而非真假的评价；
行动会留下现实后果和责任。
```

Rittel-Webber 不是说“目标不清楚”这么简单，而是说目标、事实、解释和方案互相构成：你如何定义贫困、犯罪、教育失败，已经决定了你会把哪些行动看成可能方案。

充分必要性方面，十条特征更像**诊断画像**，不是严格必要充分条件。他们说 “at least ten distinguishing properties”，说明这是规划型 wicked problems 的一组识别属性，而非逻辑定义。尤其是不同学者后来常把 wickedness 当成程度变量，而不是二元分类。

覆盖弱点：Rittel-Webber 很强地覆盖公共政策、城市规划、社会福利、教育、犯罪、环境等开放社会系统，但对以下问题覆盖较弱：

- 已有共同目标和可测指标的工程优化；
- 可重复试验的科学问题；
- 低价值冲突的技术诊断；
- 纯个人认知任务；
- 虽然复杂但不存在强烈政治评价冲突的问题。

它也容易被过度泛化，一旦所有社会问题都叫 wicked，具体分析力会下降。

## 3. Jonassen：教育心理学中的问题是有价值的未知

David Jonassen 的核心文献包括 [1997 年 ETR&D 论文](https://www.davidlewisphd.com/courses/EDD8121/readings/1997-Jonassen.pdf)，DOI: [10.1007/BF02299613](https://doi.org/10.1007/BF02299613)，以及 [“Toward a Design Theory of Problem Solving”](https://site.caes.uga.edu/sandlin/files/2023/09/Jonassen-2000.pdf)，DOI: [10.1007/BF02300500](https://doi.org/10.1007/BF02300500)。Jonassen 2000 年给出很清楚的最小定义：问题有两个 critical attributes：

```text
一是情境中的未知；
二是求解这个未知具有社会、文化或智识价值。
```

1997 年论文还说，传统上问题由 problem domain、problem type、problem-solving process、solution 构成。良构问题有明确初始状态、目标状态、有限规则、收敛答案、规定过程。劣构问题则通常来自具体情境，问题描述不清，所需信息不在题干中，解不收敛，可能跨多个领域，并要求学习者定义问题、判断所需知识、提出并辩护方案。

Jonassen 的劣构问题最小构成是：

```text
情境中的未知 / 差异；
学习者或行动者的 felt need；
具体语境；
不完全的问题元素、目标或约束；
多个可能方案和评价标准；
需要论证与元认知监控的问题表征。
```

他特别强调劣构问题求解要包含问题空间建构、视角比较、证据搜集、方案辩护、监控问题空间与方案选项。

充分必要性方面，Jonassen 对“一般问题”的两个属性接近必要条件：有未知、有价值。但他对劣构问题的各条特征明确放在连续谱中，而非严格分类。1997 年说 puzzle、well-structured、ill-structured 不是 well-defined classifications，而是从去情境、收敛到高度情境化、多解的连续体；2000 年还承认良构 / 劣构二分不足以容纳问题类型复杂性。

覆盖弱点：Jonassen 对教育设计、学习任务、专业训练非常有用，但它把许多社会政治问题转译成学习者的认知、论证和知识建构问题，因此弱于处理制度权力、利益冲突、组织政治、合法性、责任分配和不可逆公共后果。它也较少处理无明显“学习者”的集体行动困境，或强制、操控、结构性不平等造成的问题定义冲突。

## 4. Checkland SSM：问题不是对象，而是由世界观构成的问题情境

Peter Checkland 的 Soft Systems Methodology 可查 [1989 年论文页](https://journals.sagepub.com/doi/10.3233/HSM-1989-8405)，DOI: [10.3233/HSM-1989-8405](https://doi.org/10.3233/HSM-1989-8405)，以及书目 [Systems Thinking, Systems Practice / 30-year Retrospective](https://cir.nii.ac.jp/crid/1130282268952033152)。Cambridge IfM 对 SSM 的概述也很清楚：[Soft Systems Methodology](https://www.ifm.eng.cam.ac.uk/research/dstools/soft-systems-methodology/)。

SSM 的关键转向是：不要一开始问“问题是什么”，而要看“problem situation”。Cambridge IfM 概括说，复杂组织 / 社会情境中常常 “the problem is ‘what is the problem?’”

SSM 的最小构成不是“问题 = 差距 + 解法”，而是：

```text
被关切者感知为有问题的情境；
多种 worldviews；
可被建模的 purposeful activity systems；
从某一世界观出发的 root definition；
CATWOE 元素；
与现实情境比较后形成的可行且合意的改变。
```

CATWOE 包括：

| 元素 | 含义 |
|---|---|
| Customers | 受 transformation 影响的人 |
| Actors | 执行 transformation 的行动者 |
| Transformation | 输入如何被有目的活动转化为输出 |
| Weltanschauung / Worldview | 使 transformation 有意义的世界观 |
| Owners | 有权停止或改变系统的人 |
| Environmental constraints | 外部约束 |

核心是 transformation：某种输入如何通过有目的活动变成输出，但这个 transformation 必须放在特定世界观、所有者、行动者和环境约束中理解。

充分必要性方面，CATWOE 不是“问题的充分必要定义”，而是构造 root definition 的检查表。SSM 允许多个 root definitions 和多个概念模型并存，用来组织辩论和学习。Checkland 1989 摘要中的短语 “systematically desirable and culturally feasible” 说明，SSM 追求的是通过模型引发学习和改变，而非证明一个唯一正确问题定义。

覆盖弱点：SSM 弱于处理已经高度明确、目标一致、可优化的技术问题；弱于需要精确预测、控制或实时决策的场景；也依赖参与者能进入讨论、表达世界观并形成某种可行改变。在强制、暴力、严重权力不对称或参与被操纵的情境中，SSM 的“辩论和学习”前提会变弱。它对物理机制本身、统计估计和算法优化也不是主工具，通常需与硬 OR 或工程模型结合。

## 5. Rosenhead / Mingers 的 PSM：问题是结构化过程的产物

Problem Structuring Methods 的核心资料包括 Rosenhead 的 [“What’s the Problem? An Introduction to Problem Structuring Methods”](https://pubsonline.informs.org/doi/abs/10.1287/inte.26.6.117)，*Interfaces*, 1996，DOI: [10.1287/inte.26.6.117](https://doi.org/10.1287/inte.26.6.117)；Rosenhead & Mingers 编的书 [Rational Analysis for a Problematic World Revisited](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/rational-analysis-for-a-problematic-world-revisited-978-0-471-49523-9)；以及 Mingers & Rosenhead 的 [“Problem Structuring Methods in Action”](https://researchonline.lse.ac.uk/33400/)，*European Journal of Operational Research*, 2004，DOI: [10.1016/S0377-2217(03)00056-0](https://doi.org/10.1016/S0377-2217(03)00056-0)。

PSM 传统直接批评传统 OR 只适用于已经能以 performance measures、constraints、action-consequence relations 表述的良构问题。Mingers & Rosenhead 说，在这类情境中，“问题属于什么类型”本身是 problem structuring 的结果，而不是出发点。

PSM 的劣构问题最小构成是：

```text
problematic situation；
多个 actors；
多个 perspectives；
不可通约或冲突的 interests；
重要但难量化的 intangibles；
关键 uncertainties；
一个可被参与者理解和共同操作的模型 / 表征；
通过参与式过程形成局部行动承诺。
```

PSM 的目标不一定是全局最优解，而是帮助参与者澄清处境、形成一个可行动的共同问题或议题，并承诺部分改善。

充分必要性方面，PSM 文献也不把这些条件当作严格分类学。Mingers & Rosenhead 明说 PSM / 非 PSM 的边界有任意性；这些特征说明 PSM 适用的“问题情境”，而不是定义所有劣构问题的必要充分条件。PSM 对方法也提出“must”：要能并置多视角、让非专家可参与、迭代调整表征、允许局部改善承诺。但这是方法设计的必要特征，不是问题本体的充分定义。

覆盖弱点：PSM 弱于单一决策者、目标明确、数据充分、可优化的问题；弱于没有参与渠道或相关行动者无法共同工作的问题；弱于必须依靠精密数学、仿真、统计推断才能判断的问题。它也可能低估深层权力结构：如果某些利益相关者不能进入房间，或某些利益无法被合法表达，模型的“共同表征”会产生表面共识。

## 6. 跨传统比较：什么是“问题”的最小构成

| 传统 | “问题”的基本单位 | 劣构性的来源 | 构件是否充分必要 |
|---|---|---|---|
| Simon | 求解器面对的问题空间 | 目标、状态空间、操作符、知识、评价或计算可行性不充分 | 否。连续谱，相对求解器能力 |
| Rittel-Webber | 社会规划中的应然-实然差异 | 定义、解释、方案、评价、后果和责任纠缠 | 否。十特征是诊断画像 |
| Jonassen | 有价值的未知 | 目标、约束、信息、方案、标准、知识组织不清 | 一般问题有两个近似必要属性；劣构是连续谱 |
| Checkland SSM | 被感知为有问题的情境 | 多世界观下“问题是什么”本身需学习 | 否。CATWOE 是 root definition 检查表 |
| Rosenhead PSM | 多主体参与结构化的问题情境 | 多视角、冲突利益、无形因素、不确定性 | 否。是适用情境和方法要求 |

如果把它们压缩成一句话：

```text
一个问题至少是“某主体在某情境中感知到一个值得行动的未知 / 差异，并通过某种表征把现状、可能行动和评价依据联系起来”。
```

劣构问题则是在这个联系尚不能稳定、完整、共识化地建立时出现。

## 7. 最小必要构件的分层

第一层，构成“问题”本身的必要构件：

| 构件 | 说明 | 主要来源 |
|---|---|---|
| 情境 | 问题总是位于任务、实践、组织或社会情境中 | Jonassen, SSM, PSM |
| 主体 / 关切者 | 没有人感知、关心或承担，至少不是实践意义上的问题 | Jonassen, SSM, PSM |
| 未知 / 差异 | 不知道什么、缺什么、现状与目标或应然有何落差 | Jonassen, Rittel-Webber |
| 价值 / 需要 | 该未知必须值得解决；否则只是事实差异 | Jonassen |
| 行动可能性 | 问题面向改变，不只是观察 | Simon, Rittel-Webber, SSM, PSM |
| 表征 / 框定 | 必须把情境组织成可讨论、可搜索或可行动的形式 | Simon, Schön / 设计传统, SSM, PSM |
| 评价 | 至少要有某种判断“更好 / 可接受 / 有效”的方式 | Simon, Rittel-Webber, SSM, PSM |

第二层，构成“劣构问题”的必要或强相关构件：

| 劣构构件 | 含义 |
|---|---|
| 边界未定 | 哪些因素属于问题尚不清楚 |
| 目标未定或多元 | 目标可能冲突，且会随理解改变 |
| 方案空间不可穷尽 | 不能列出所有可行动作 |
| 评价标准不唯一 | 没有单一 true/false，常是 good/bad、desirable/feasible |
| 因果知识不稳 | 行动与后果关系不确定，且有长链条后果 |
| 表征会变 | 求解过程会改变问题定义 |
| 多主体冲突 | 在 wicked / SSM / PSM 中尤其关键，但在 Simon 的个体认知意义上不是必要条件 |
| 行动不可完全试错 | 在 wicked public planning 中关键，但不适用于所有劣构问题 |

所以，**多主体冲突不是所有劣构问题的必要条件**，因为 Simon 和 Jonassen 可以讨论个体设计者或学习者面对的劣构问题；但它是 wicked problems、SSM、PSM 中社会性劣构的核心条件。**不可逆后果也不是所有劣构问题的必要条件**，但它是 Rittel-Webber 的 wickedness 中非常关键的增强条件。

## 8. 这些传统共同无法充分覆盖的类型

第一，**纯粹恶意、欺骗或操控造成的问题定义**。PSM / SSM 假设参与、表达和学习有意义；但若问题定义被宣传、审查、威胁、利益绑架系统性扭曲，仅靠结构化对话不够。

第二，**深层结构性权力与不平等**。这些传统会谈 stakeholders、worldviews、interests，但对谁能进入议程、谁的语言被承认为理性、谁承担外部性，往往需要批判理论、政治经济学、法学或组织权力分析补足。

第三，**高速、灾难性、实时控制问题**。例如网络攻击响应、核事故控制、金融闪崩等。它们可能劣构，但没有充分时间做参与式 problem structuring，需要预案、控制理论、韧性工程和应急决策。

第四，**高度形式化但计算困难的问题**。如 NP-hard 优化、复杂调度、组合爆炸。这类问题不一定劣构；目标、约束和评价可能很清楚，只是求解困难。Simon 可部分覆盖“相对计算能力”的难度，但 wicked / SSM / PSM 不应被滥用到这里。

第五，**事实机制主导、价值争议较低的科学问题**。例如某材料失效机制、某算法 bug、某设备故障。问题可能初期不清楚，但一旦诊断目标和证据标准明确，硬科学 / 工程方法更合适。

第六，**无明确人类目的系统中的“问题”**。SSM 的 purposeful activity system、PSM 的参与式承诺、Jonassen 的 felt need 都要求人类关切。生态系统、气候系统、AI 系统可以成为问题情境，但“问题性”来自人类或制度评价，不是系统自身天然拥有。

## 9. 最终定义

基于这条文献传统，一个稳健定义可以写成：

```text
问题，是某个主体或主体群在特定情境中，把一个具有价值或规范意义的未知、差异或不满意状态，表征为需要行动、判断和改变的对象。
```

劣构问题则是：

```text
劣构问题，是这样一种问题：其情境边界、目标、相关知识、行动集合、约束、评价标准、因果后果或责任归属，不能在求解前被充分、稳定、共识化地给定；并且问题的表述会随着探索、争论、建模和行动而改变。
```

更窄地说，wicked / SSM / PSM 传统中的社会性劣构问题是：

```text
多主体在开放社会系统中面对的、价值和解释冲突显著、方案不可穷尽、后果不可完全预知且行动会改变情境的问题情境；其中“什么是问题”本身就是需要结构化、辩论和学习的核心任务。
```

## 10. 核心资料清单

- Herbert A. Simon, 1973, “The Structure of Ill Structured Problems,” *Artificial Intelligence*. [PDF](https://iiif.library.cmu.edu/file/Simon_box00085_fld06830_bdl0008_doc0001/Simon_box00085_fld06830_bdl0008_doc0001.pdf), [DOI](https://doi.org/10.1016/0004-3702(73)90011-8)
- Horst W. J. Rittel & Melvin M. Webber, 1973, “Dilemmas in a General Theory of Planning,” *Policy Sciences*. [PDF](https://urbanpolicy.net/wp-content/uploads/2015/06/Rittel-Webber_1973_DilemmasInAGeneralTheoryOfPlanning.pdf), [DOI](https://doi.org/10.1007/BF01405730)
- David H. Jonassen, 1997, “Instructional Design Models for Well-Structured and Ill-Structured Problem-Solving Learning Outcomes,” *ETR&D*. [PDF](https://www.davidlewisphd.com/courses/EDD8121/readings/1997-Jonassen.pdf), [DOI](https://doi.org/10.1007/BF02299613)
- David H. Jonassen, 2000, “Toward a Design Theory of Problem Solving,” *ETR&D*. [PDF](https://site.caes.uga.edu/sandlin/files/2023/09/Jonassen-2000.pdf), [DOI](https://doi.org/10.1007/BF02300500)
- Peter Checkland, 1989, “Soft Systems Methodology,” *Human Systems Management*. [SAGE page](https://journals.sagepub.com/doi/10.3233/HSM-1989-8405), [DOI](https://doi.org/10.3233/HSM-1989-8405)
- Peter Checkland, *Systems Thinking, Systems Practice / Soft Systems Methodology: A 30-Year Retrospective*. [书目](https://cir.nii.ac.jp/crid/1130282268952033152)
- Cambridge Institute for Manufacturing, “Soft Systems Methodology.” [概述](https://www.ifm.eng.cam.ac.uk/research/dstools/soft-systems-methodology/)
- Jonathan Rosenhead, 1996, “What’s the Problem? An Introduction to Problem Structuring Methods,” *Interfaces*. [INFORMS page](https://pubsonline.informs.org/doi/abs/10.1287/inte.26.6.117), [DOI](https://doi.org/10.1287/inte.26.6.117)
- Jonathan Rosenhead & John Mingers, eds., 2001, *Rational Analysis for a Problematic World Revisited: Problem Structuring Methods for Complexity, Uncertainty and Conflict*. [Wiley 书目](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/rational-analysis-for-a-problematic-world-revisited-978-0-471-49523-9)
- John Mingers & Jonathan Rosenhead, 2004, “Problem Structuring Methods in Action,” *European Journal of Operational Research*. [LSE record](https://researchonline.lse.ac.uk/33400/), [DOI](https://doi.org/10.1016/S0377-2217(03)00056-0)
