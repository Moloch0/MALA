# 逻辑、形式语义与问题语义：Question / Problem / Answerhood

> 来源说明：本文基本保留子代理关于 erotetic logic、形式语义和 inquisitive semantics 的原始梳理，仅做 Markdown 标题、公式和链接格式整理。本文不套用 MALA 既有框架，而是从该传统自身出发。

## 总论

在 erotetic logic、形式语义和 inquisitive semantics 这一传统里，“问题”通常不是先被理解为一个心理状态、任务目标或社会行动，而是被压缩成一个可形式化的 **answerhood / resolution profile**：什么东西算作回答，什么信息状态算作解决该问题。最小共同点可以写成：

```math
Q \approx \text{一个把逻辑空间 } W \text{ 划分、筛选或约束为若干可解决状态的结构}
```

其中 `W` 是可能世界 / 可能状态集合；命题是 `W` 的子集；问题的语义不是一个单一真假命题，而是关于若干命题、答案或解决状态的结构。

需要区分三层：

1. **问题句 / interrogative sentence**：自然语言中的疑问句，或形式语言中的 erotetic expression。Groenendijk & Stokhof 明确把 interrogatives 与 questions 区分开：疑问句表达问题，但二者不等同。见 [Groenendijk & Stokhof, “Questions”](https://stokhof.org/wp-content/uploads/2020/10/groenendijk-stokhof_q.pdf)。
2. **问题 / question as semantic object**：疑问句的语义值，例如答案集合、划分、下闭的信息状态集合。
3. **提问行为 / asking**：说话人用问题句执行的言语行为，包含请求、承诺、共同议题更新等语用成分。

Hamblin 的核心思想是，questions set up a “choice-situation” among answer propositions。参见 [Inquisitive Semantics, ch. 9](https://academic.oup.com/book/35968/chapter/311298396)。

## 1. Hamblin：问题是可能答案的集合

Hamblin 1973 的基本思想是：一个问题的意义是它的可能答案所表达的命题集合。形式上：

```math
\llbracket Q \rrbracket = \{p_1,p_2,\ldots\}, \quad p_i \subseteq W
```

例子：

```math
\llbracket \text{Is it raining?} \rrbracket = \{r,\neg r\}
```

```math
\llbracket \text{Who came?} \rrbracket =
\{\text{John came}, \text{Mary came}, \ldots\}
```

Karttunen 在介绍 Hamblin 时说，Hamblin 让直接问题 “denote a set of propositions”，即 possible answers 所表达的命题集合。见 [Karttunen 1977 PDF](https://semantics.uchicago.edu/kennedy/classes/s08/semantics2/karttunen77.pdf)。

最小必要构件是：

1. 可能世界空间 `W`。
2. 命题作为 `W` 的子集。
3. 一个从疑问句到答案命题集合的语义规则。
4. answerhood：直接回答至少是该集合中的一个命题，或能表达其中一个命题的句子。

在 Hamblin 自身框架里，答案集合基本上就是问题意义的充分结构：知道所有 possible answers，就知道问题。必要性也在该理论内部成立，因为问题被语义化为答案集合。但这不是跨理论的充分必要条件。后来文献的主要批评是：“possible answer” 本身不够清楚。SEP 举例：对 “Who is coming for dinner?”，不同 response 都像某种回答，但 Hamblin/Karttunen 只把某些算作 possible answer；标准何在并不自明。见 [SEP Questions §2.1.1](https://plato.stanford.edu/entries/questions/)。

覆盖弱点：

1. 对“可能答案”的判准偏原始，缺少独立定义。
2. 难以自然定义“一个问题比另一个问题更强 / question entailment”。
3. 对过度信息回答、部分回答、间接回答、合作性回答的区分较弱。
4. 对 why-questions、解释性问题、身份识别问题、语境相关 answerhood 覆盖弱。
5. 可以表示任意答案集合，反而过宽：许多集合未必对应自然语言可表达的问题。

## 2. Karttunen：问题是真答案集合的世界依赖函数

Karttunen 1977 保留 Hamblin 的“命题集合”想法，但把问题在世界 `w` 中的外延设为 **真答案集合**：

```math
\llbracket Q \rrbracket^w =
\{p: p \text{ is a true answer to } Q \text{ in } w\}
```

所以问题的 intension 是：

```math
\lambda w.\{p_1,p_2,\ldots\}
```

Karttunen 自己说，他选择让 questions denote “the set of propositions expressed by their true answers”，而不是 all possible answers。见 [Karttunen 1977](https://semantics.uchicago.edu/kennedy/classes/s08/semantics2/karttunen77.pdf)。

最小必要构件是：

1. `W`：可能世界。
2. `p ⊆ W`：命题。
3. 世界参数 `w`。
4. 问题意义：从世界到真答案命题集合的函数。
5. answerhood：真答案是该世界中属于此集合的命题；完整答案由集合整体共同构成。

与 Hamblin 的差别：Hamblin 的问题通常是世界不变的 possible-answer set；Karttunen 的问题在每个世界取出 true-answer subset。OUP 概括说，在 Hamblin 中每个世界映到同一个 possible-answer set；在 Karttunen 中每个世界映到其中真答案的子集；Karttunen 认为差别不根本。见 [Inquisitive Semantics ch. 9](https://academic.oup.com/book/35968/chapter/311298396)。

充分必要性：在 Karttunen 的嵌入问句语义中，`λw` 到真答案集合足以作为问题意义，尤其适合处理 know、tell、wonder 等 question-embedding verbs。但它仍把 answerhood 当成语义构造的核心，而不是从“解决条件”推出 answerhood。

覆盖弱点：

1. 仍继承 possible/direct answer 判准问题。
2. 对 alternative questions 的“恰一为真”、wh-questions 的存在预设等，需要额外语用 / 预设机制。
3. 对强穷尽回答的处理不如 partition semantics 直接。
4. 对 mention-some 问题、条件问题、解释性 why 问题仍不是天然适配。

## 3. Groenendijk & Stokhof：问题是逻辑空间的 Partition

Groenendijk & Stokhof 的关键转向是：问题不是答案命题集合，而是把可能世界划分为等价类的结构。两个世界 `w,v` 在同一个 cell 中，当且仅当它们给出同一个完整穷尽答案。

```math
w \sim_Q v
\iff
\text{the complete answer to } Q \text{ is the same in } w \text{ and } v
```

由等价关系得到 partition：

```math
\Pi_Q = W/{\sim_Q}
```

每个 cell 是一个完整可能答案；在实际世界 `w`，真实完整答案就是 `w` 所在的 cell：

```math
Ans_Q(w) = [w]_Q
```

SEP 概括：Groenendijk & Stokhof 让问题在每个世界表示 “the true exhaustive answer”，而问题意义可识别为形成 logical space partition 的命题集合。见 [SEP Questions §2.1.2](https://plato.stanford.edu/entries/questions/)。

最小必要构件是：

1. `W`：逻辑空间，或满足问题预设的世界域。
2. `~_Q`：世界间等价关系。
3. `Π_Q`：由等价关系生成的 partition。
4. 每个 partition cell 是一个完整且精确的可能答案。
5. answerhood：完整语义答案是 cell；部分答案可被建模为排除若干 cells 或包含于某 cell 的信息。

这里的核心条件是：

1. **互斥性**：不同完整答案不能同时为真。
2. **穷尽性**：所有 cells 覆盖相关逻辑空间。
3. **唯一真完整答案**：每个世界中恰有一个完整答案为真。

这三者在 partition theory 内部几乎是充分必要条件：一个问题就是一个 partition；一个 partition 就给出一种问题意义。Groenendijk & Stokhof 称这个图景给出统一且形式上优雅的 question-answerhood 观念，并能处理问题等价、问题蕴涵、合取问题等。

覆盖弱点：

1. **mention-some questions**：如 “Where can I buy an Italian newspaper?” 只需给一个地点即可。若多个地点都可行，则在同一世界有多个最小解决答案，没有唯一穷尽答案。OUP 明确说这类问题 cannot be represented as a partition。
2. **conditional questions**：如 “If Ann comes, will Bill come?”。否定 antecedent 的回答可“消解”但不按预期“解决”；partition 难表达这种特殊地位。
3. **alternative questions / open disjunctive questions**：某些答案状态不是标准 partition cell，但又显然是相关回应。
4. **approximate-value questions**：如“这个值大约是多少？”答案容许重叠区间，不天然互斥。
5. **why-questions**：解释性 answerhood 依赖原因、反事实、对比类、解释规则，不只是划分世界。
6. **语境化身份问题**：如 “Who is Hong Oak Yun?”，什么算满意回答取决于识别方式和语境；标准 partition 太粗或太客观。

## 4. Inquisitive Semantics：问题是解决条件的下闭集合

Inquisitive semantics 的核心改变是：问题意义不是 possible answers，也不必须是 partition，而是 **哪些信息状态足以解决该 issue**。

信息状态：

```math
s \subseteq W
```

问题 / 句子的 inquisitive proposition：

```math
\llbracket Q \rrbracket \subseteq \mathcal{P}(W)
```

并要求非空且下闭：

```math
s \in \llbracket Q \rrbracket
\text{ and }
t \subseteq s
\Rightarrow
t \in \llbracket Q \rrbracket
```

直觉：如果信息状态 `s` 已经解决问题，那么更强的信息状态 `t` 也解决问题。Springer 的定义写得很直接：inquisitive proposition 是 “non-empty and downward closed” 的信息状态集合。见 [Foundations of Inquisitive Logic](https://link.springer.com/chapter/10.1007/978-3-031-09706-5_2)。

在此框架中：

1. `[[Q]]` 的元素不是“答案句”，而是解决该 issue 的信息状态。
2. 最大元素 `Alt([[Q]])` 是 alternatives，即最小充分解决状态。
3. answerhood 不是原始概念，而是派生概念：最小回答、完整回答、部分回答都从 resolution conditions 定义。

OUP 明确指出：inquisitive semantics 不把问题意义定义为 possible/minimal/complete/partial answers；相反，先定义 issue 的解决条件，再定义 answerhood。见 [Inquisitive Semantics ch. 9](https://academic.oup.com/book/35968/chapter/311298396)。

最小必要构件是：

1. `W`：可能世界空间。
2. `s ⊆ W`：信息状态。
3. 支持 / 解决关系 `s ⊨ Q`，或等价地 `[[Q]]={s:s⊨Q}`。
4. 下闭性：解决状态的增强仍解决。
5. alternatives：最大解决状态，作为最小回答。
6. 对纯问题，通常要求 alternatives 多于一个，并且覆盖相关逻辑空间；若还传递信息，则可同时有 informative content。

充分必要性：在 InqB 的语义类型内，非空下闭集合是 proposition 的一般形式；作为 issue，下闭解决条件是核心必要条件。对普通非信息性问题，还需有多个 alternatives，并覆盖逻辑空间。它比 partition 更弱，因为 alternatives 可以重叠或不形成互斥穷尽划分；因此能覆盖 mention-some、条件问题、开放析取问题等非 partition issue。

覆盖弱点：

1. 基础 InqB 主要刻画 informative/inquisitive content，不完整刻画言语行为、承诺结构、偏向问题、tag questions、declarative questions。
2. 基础框架不自动处理 discourse anaphora、后续指称、语篇 referents；Roelofsen & Farkas 等扩展才处理这些问题。
3. why-questions、解释性问题、实践性问题、方法问题仍需要额外解释理论或语用理论。
4. 结构化问句意义、焦点、语调、问句内部构型的细粒度差异，单靠下闭集合可能过粗。

## 5. Erotetic Logic / IEL：问题如何从前提中产生

Erotetic logic 更像“问题与回答的逻辑”，不只做自然语言语义。Belnap & Steel 的经典目标是设计 formal notation for questions and answers。见 [PhilPapers: The Logic of Questions and Answers](https://philpapers.org/rec/BELTLO-2)。

Wiśniewski 的 inferential erotetic logic, IEL，则把重点放在问题如何从前提出发、如何由一个问题推出另一个问题。IEL 的最小设定：

1. 形式语言中有 declarative formulas 和 questions 两类表达式。
2. 每个问题 `Q` 被赋予一个直接答案集合 `dQ`。
3. `dQ` 至少有两个元素，且直接答案是陈述句 / 公式。
4. 问题不能简单等同于答案集合；例如 `?{p,q} ≠ ?{q,p}`。见 [Wiśniewski & Leszczyńska-Jasion 2015](https://link.springer.com/article/10.1007/s11229-013-0355-4)。

IEL 对“问题何时从前提出发”给出 evocation：

```math
E(X,Q)
\iff
X \Vdash dQ
\text{ 且对每个 } A \in dQ,\ X \not\Vdash \{A\}
```

在经典命题逻辑情形下可理解为：

```math
X \models A_1 \vee \cdots \vee A_n
```

但：

```math
X \not\models A_i
\quad
\text{for each } A_i
```

直觉很清楚：前提保证至少有一个直接答案为真，但不保证哪一个为真；所以问题产生。见 [Inferential erotetic logic meets inquisitive semantics](https://link.springer.com/article/10.1007/s11229-013-0355-4)。

这给 “problem” 一个很精确的逻辑解释：一个 problem 不是任意缺口，而是相对于背景 `X`，存在一个被保证可答但尚未决定的直接答案空间。也就是：

```math
\text{problem} = \langle X,Q,dQ\rangle
```

其中 `X` 使问题有根据，但未解决问题。

充分必要性：在 IEL 中，“直接答案集合至少两个 + 问题表达式”是构造问题的必要条件；但直接答案集合本身不充分，因为问题还有形式表达式身份、顺序或构型。Evocation 条件则给出“问题从前提中产生”的充分必要条件。

覆盖弱点：

1. 偏形式语言和推理结构，不是完整自然语言语义。
2. 通常要求直接答案有限且明确；开放式、解释性、程度性、方法性问题难处理。
3. 对“有用回答”“合作回答”“纠错回答”“回答的语境充分性”覆盖较弱。
4. 对问句的语法、嵌入、语调、焦点、偏向等语言现象不是主战场。

## 6. 最小语义结构：综合但不外套框架

如果只从这条传统内部抽象，最小语义结构不是“一个问号”或“一个未知变量”，而是：

```math
Q = \text{一个定义 answerhood/resolution 的结构}
```

更具体地有三个层级版本。

### 6.1 答案集合版

```math
Q \subseteq \mathcal{P}(W)
```

问题是可能答案命题集合。Hamblin/Karttunen 路线。

### 6.2 划分版

```math
Q = \Pi_Q,\quad \Pi_Q \text{ is a partition of } W
```

问题是互斥且穷尽的完整答案划分。Groenendijk & Stokhof 路线。

### 6.3 解决条件版

```math
Q \subseteq \mathcal{P}(W),\quad Q \text{ non-empty and downward closed}
```

问题是足以解决 issue 的信息状态集合。Inquisitive semantics 路线。

三者的关系可以这样看：

```math
\text{Partition} \subset \text{Inquisitive issue}
```

partition 是一种特殊 issue：每个世界有唯一完整穷尽答案。Hamblin/Karttunen 的答案集合则是较早、较自由但约束较少的表示方式。IEL 则提醒我们：若关心“问题如何从前提中产生”，最小结构还必须加入背景前提 `X` 与直接答案集合 `dQ`。

## 7. 最终回答

对“什么是一个问题 / 问题句 / 问题的最小语义结构”的回答是：

1. **问题句**：表达问题的疑问句或形式 erotetic expression；它不是问题本身。
2. **问题**：一种以 answerhood 或 resolution 为核心的语义对象。
3. **问题的最小语义结构**：至少需要一个可能性空间 `W`，以及一个规定哪些命题 / 信息状态算作回答或解决的结构。
4. **是否充分必要**：在各自理论内部可以是充分必要的，但跨理论没有唯一充分必要结构；partition 太强，Hamblin/Karttunen 太宽，inquisitive issue 当前最一般但仍需语用扩展。
5. **problem**：在这条传统中最接近“尚未解决的 issue”；在 IEL 中尤其精确，即背景保证答案存在但未决定具体答案。
