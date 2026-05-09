# The Mathematical Criterion For A Good Question

The previous essays have repeated one claim: a good question is not a sentence with a question mark, but a solvable structure. At this point, that sentence needs to be tightened into a precise mathematical object. Otherwise "good question" remains only a methodological slogan rather than a concept that can be defined, tested, and compared.

This essay discusses only one sharply bounded case: **finite-horizon control problems in a fixed task and a fixed environment**. Within this range, we no longer ask what question sounds deeper. We ask only one thing:

> For a given control task, what kind of problem formulation is both sufficient to support optimal decision making and free of decision-irrelevant redundancy?

The answer I will give is:

> For a fixed control problem, a good question is the coarsest exact control state abstraction of the original history.

This is not a metaphor. It is the object that will be formally defined and justified below.

## I. Formal Setup

Consider a discrete-time controlled stochastic process with time steps $t=0,1,\dots,T$. Let

- observation be $O_t$
- action be $A_t \in \mathcal A_t$
- reward be $R_t \in \mathbb R$

The full history up to time $t$ is

$$
H_t = (O_0, A_0, R_0, \dots, O_t).
$$

Let a policy $\pi$ map each history to an action distribution. Given a discount factor $\gamma \in [0,1]$, the optimal value function from history $h \in \mathcal H_t$ is

$$
V_t^\star(h)
=
\sup_\pi
\mathbb E^\pi\!\left[
\sum_{k=t}^{T-1} \gamma^{k-t} R_k
\;\middle|\;
H_t = h
\right].
$$

Now introduce the mathematical version of a "problem formulation." A problem formulation is a compression of the full history into some state representation:

$$
\phi_t : \mathcal H_t \to \mathcal S_t,
\qquad
S_t = \phi_t(H_t).
$$

So this essay is not about linguistic question sentences. It is about the properties of a history-compression map $\phi$.

## II. Exact Control Abstraction

If a compressed state really represents the case in which "the problem has been written correctly," it must satisfy at least one basic condition: once the current state and action are given, the future evolution relevant to the task should no longer depend on the discarded details of history.

This yields the first definition.

### Definition 1: Closed Under Control

Say that a representation $\phi = (\phi_t)_{t=0}^T$ is **closed under control** if for every $t<T$, there exists a kernel

$$
K_t^\phi(dr, ds' \mid s, a)
$$

such that for every $h \in \mathcal H_t$ and $a \in \mathcal A_t$,

$$
\mathcal L\!\left(
R_t,\phi_{t+1}(H_{t+1})
\mid
H_t=h, A_t=a
\right)
=
K_t^\phi(\cdot \mid \phi_t(h), a).
$$

That is, once the compressed state $s=\phi_t(h)$ and the action $a$ are given, the conditional distribution of the next reward and next compressed state no longer depends on the full history $h$.

This property is necessary if Bellman recursion is to hold over the compressed state.

### Definition 2: Exact Control Abstraction

If a representation $\phi$ is closed under control, and there exist functions $\bar V_t^\phi : \mathcal S_t \to \mathbb R$ such that

$$
V_t^\star(h) = \bar V_t^\phi(\phi_t(h))
\qquad
\text{for all } h \in \mathcal H_t,
$$

then $\phi$ is called an **exact control abstraction**.

This definition turns the sentence "the state representation is sufficient to support optimal control" into a strict statement: the optimal value function varies only through the compressed state, no longer through the distinctions in history that have been compressed away.

## III. Why Minimality Is Also Needed

Even this is still not enough. If we take the full history itself as the state, namely

$$
\phi_t(h) = h,
$$

then it is obviously closed under control and obviously an exact control abstraction. But this is clearly not yet a "good question," because it has performed no compression at all.

So we must distinguish further: which state representations are merely correct, and which are both correct and stripped of all task-irrelevant redundancy?

To do this we need to define, directly on the history space, an equivalence relation in the sense of control.

## IV. Control Equivalence

When should two histories count as "the same state"? Not when they look similar observationally, nor when they can be grouped narratively, but when they are completely equivalent with respect to **future control**.

### Definition 3: Control Equivalence

At the terminal time $T$, define all histories to be equivalent.

For any $t<T$, define recursively a relation $\sim_t$: if two histories $h,h' \in \mathcal H_t$ satisfy, for every action $a \in \mathcal A_t$,

$$
\mathcal L\!\left(
R_t, [H_{t+1}]_{\sim_{t+1}}
\mid
H_t=h, A_t=a
\right)
=
\mathcal L\!\left(
R_t, [H_{t+1}]_{\sim_{t+1}}
\mid
H_t=h', A_t=a
\right),
$$

then we say

$$
h \sim_t h'.
$$

Here $[H_{t+1}]_{\sim_{t+1}}$ denotes the equivalence class of the next history.

The meaning of this definition is: if two histories, under any action, induce the same distribution over immediate reward and the same distribution over next-step control-equivalence classes, then they have no real difference in the sense of control.

This yields the canonical state representation

$$
S_t^\star = [H_t]_{\sim_t}.
$$

It compresses full histories into control-equivalence classes.

## V. Main Theorem

We can now state the central result.

### Theorem: The Coarsest Exact Control Abstraction

The canonical states induced by the control-equivalence relation,

$$
S_t^\star = [H_t]_{\sim_t},
$$

satisfy the following three properties:

1. $S^\star$ is closed under control;
2. the optimal value function depends only on $S_t^\star$;
3. any exact control abstraction $\psi_t(H_t)$ must refine $S_t^\star$.

In other words, $S^\star$ is the coarsest among all exact control abstractions.

### Proof Sketch

**1. Closure.**  
By definition, if $h \sim_t h'$, then for any action $a$, the two histories induce the same conditional distribution over

$$
(R_t, [H_{t+1}]_{\sim_{t+1}}).
$$

So this common distribution can be represented using only the current equivalence class $S_t^\star$ and the action $a$, which gives the required kernel $K_t^\star$.

**2. Sufficiency.**  
Use backward induction. The terminal case is immediate. If $V_{t+1}^\star$ depends only on $S_{t+1}^\star$, then

$$
Q_t^\star(h,a)
=
\mathbb E\!\left[
R_t + \gamma V_{t+1}^\star(H_{t+1})
\mid
H_t=h, A_t=a
\right]
$$

depends only on

$$
\mathcal L(R_t, S_{t+1}^\star \mid H_t=h, A_t=a),
$$

and by definition that distribution depends only on $S_t^\star(h)$. Therefore $V_t^\star(h)=\max_a Q_t^\star(h,a)$ also depends only on $S_t^\star(h)$.

**3. Minimality.**  
Let $\psi$ be any exact control abstraction, and suppose $\psi_t(h)=\psi_t(h')$. Since $\psi$ is both closed under control and sufficient for optimal control, two histories merged by $\psi$ cannot still differ in their future control consequences; otherwise $\psi$ would already have lost task-relevant information. Hence $h \sim_t h'$. This means every state class of $\psi$ is contained in some control-equivalence class, i.e. $\psi$ can only refine $S^\star$.

The theorem follows.

## VI. Corollary: A Strict Definition Of A Good Question

The theorem above already provides everything this essay needs. So the definition of a "good question" can now be compressed into one sentence:

> For a fixed control task, a good question is the coarsest exact control state abstraction.

Expanded, this means:

- **Exact**: it cannot lose any information that affects future optimal control;
- **Coarsest**: it cannot preserve any redundant distinction that does not affect future optimal control.

So a good question is neither "the more information the better" nor "the shorter the better," but rather:

> It quotients the history exactly by control relevance, neither merging what should stay distinct nor splitting what should be treated as the same.

This is the first point at which the repeated phrase "the least but sufficient structure" acquires a genuinely rigorous meaning.

## VII. Modeling Principles

If we translate the definition above into modeling principles, only three are truly central.

### 1. Task Relativity

There is no good question apart from a task. State abstraction is always defined relative to the action set, reward structure, time scale, and optimization goal. To ask "what is a good question?" before specifying the task is itself undefined.

### 2. Control Relevance

Preserve all and only those distinctions that change future control consequences. Modeling is not the listing of facts. It is the decision, over the history space, of which differences matter and which should be treated as equivalent.

### 3. Closure

Once a state representation is adopted, future recursion should not secretly depend again on the deleted history. If closure fails, the abstraction has not truly taken hold of the problem.

Seen this way, modeling ability is not "being able to write many variables," but **being able to define the right equivalence relation**.

## VIII. Boundary

The conclusion of this essay has a clear boundary. It deals only with problem formulation under a fixed task and a fixed environment. At that level, "the coarsest exact control abstraction" is already the full answer.

But if we further require that the formulation remain valid under environmental change, distribution shift, or intervention, then closure and minimality are no longer enough. A representation can be perfectly exact in the current environment and yet still capture only local correlation rather than stable mechanism.

That leads to the stronger condition of the next essay:

> For problems that must remain robust across environments, a good question must not only be exact and coarsest, but must also align with causally stable structure.
