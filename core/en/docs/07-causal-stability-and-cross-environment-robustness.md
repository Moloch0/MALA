# Causal Stability And Cross-Environment Robustness

The previous essay already gave a fairly strong conclusion: for a fixed control problem, a good question is the coarsest exact control state abstraction, or in brief, "minimal sufficiency plus closure under control."

If we stopped there, the whole theory would already explain a great many things. It tells us that the essence of problem construction is not to phrase a question beautifully, but to compress history into a state representation just sufficient to support optimal decision making.

But that is still not the whole story. What is sufficient in a single environment is not necessarily the same as having grasped a truly stable structure.

This point is extremely important. A state representation may work perfectly well in the current environment: the value function may be learned accurately, the policy may perform optimally, and yet the moment the environment changes slightly, the representation collapses. The reason is not mysterious: it may not have captured the causal mechanism that determines the task, but only some surface correlation that happens to be stable in the current environment.

So if we raise the requirement from "solvable in the current environment" to "still valid across a family of environmental changes," we must add a new criterion: **causal stability**.

## I. Why The Previous Essay Was Not Enough

The previous essay characterized the following kind of correctness:

> In this particular control task and this particular environment, is the state representation sufficient to support exact recursive decision making?

This is a local correctness. It is strong, but it still allows a state representation to depend on variables that are only accidentally correlated.

For example, suppose the true driver of reward is a hidden variable $C$, but in the training environment the observable variable $W$ happens always to match $C$. Then using $W$ as the state is entirely sufficient. The value function, the optimal policy, and Bellman recursion can all hold.

The problem is that this does not show that $W$ has captured the truly stable structure. It has only captured a proxy that happens to look like a state in the current environment.

## II. A Simple Counterexample

Consider a one-step decision task. There is a hidden state

$$
C \in \{0,1\},
$$

an action

$$
A \in \{0,1\},
$$

and reward defined by

$$
R = \mathbf 1\{A = C\}.
$$

That is, you get reward only when your action equals the true state $C$.

Now suppose that in the training environment $e=0$, we observe a variable $W$ such that

$$
W = C.
$$

Then in that environment, using $W$ as the state is entirely fine. Since $W$ equals the variable that truly determines reward, the policy $A=W$ is optimal.

But now consider another environment $e=1$, where only the observation mechanism changes:

$$
W = 1 - C.
$$

The reward mechanism is unchanged. The action space is unchanged. The true task structure is unchanged. What changed is only the relation between the observed variable and the hidden state. If you still treat $W$ as the state, the formerly optimal policy now fails systematically.

What does this show? It shows that $W$ is sufficient in a single environment, but not stable. It did not capture the mechanism that truly determines the task. It captured only a proxy feature that happened to work in one environment.

## III. Therefore Causal Stability Is Not An Unconditional Requirement For Single-Environment Control

This must be stated carefully, otherwise the claim gets overstretched.

In a fixed single environment, the criterion of the previous essay is already enough. You can absolutely use a purely correlational representation that works perfectly in the current environment to achieve optimal control. There is no mathematical contradiction.

So the following sentence is false:

> Causal stability is a necessary condition for exact control in a single environment.

The correct statement is:

> Causal stability is a necessary condition for robust control across environments.

In other words, causal stability is forced only when we ask that a problem formulation remain valid after environmental change, distribution shift, or intervention.

## IV. How To Formalize "Causal Stability"

Suppose we face not just one environment, but a family of environments $e \in \mathcal E$. In each environment the observation distribution may change, but we hope there exists some deeper task-relevant state $C_t$ such that the following structure remains unchanged across all environments:

$$
(C_{t+1}, R_t) \perp H_t \mid C_t, A_t,
$$

and its transition kernel does not depend on the environment:

$$
P_e(C_{t+1}, R_t \mid C_t, A_t)
=
P(C_{t+1}, R_t \mid C_t, A_t).
$$

This means that $C_t$ is the true causal state. Different environments may change how you observe it, may change surface statistical relations, but may not change how it and the action jointly generate future task-relevant results.

We then say that a representation $\phi$ is intervention-stable if there exists an environment-independent kernel $K_t$ such that for every environment $e$,

$$
\mathcal L_e(R_t, \phi_{t+1}(H_{t+1}) \mid H_t=h, A_t=a)
=
K_t(\cdot \mid \phi_t(h), a).
$$

This definition is stronger than the previous notion of closure. The earlier condition only asked for a closure kernel in a single environment. This one asks for the same closure kernel to hold in all environments.

## V. Why This Forces A Causal Requirement

If your state representation factors through the causal state $C_t$, namely

$$
\phi_t(H_t) = f_t(C_t),
$$

then as long as the structural kernel of $C_t$ is invariant across environments, $\phi$ is naturally much more likely to remain closed across environments. It depends on variables that remain stable under intervention, rather than on some accidental observational proxy.

Conversely, if your representation captures only a surface correlation from one environment, then it is usually easy to construct another environment that changes that correlation without changing the real task structure, and your representation breaks. The earlier variable $W$ is the simplest example.

So the role of causal stability is not to improve fit in the current environment. It is to ensure that the problem formulation still preserves the correct structure under change.

## VI. The Upgraded Conclusion

We can now state the whole criterion in layers.

For **exact control problems in a fixed environment**, the mathematical criterion of a good question is:

- minimal sufficiency
- closure under control

For **problem formulations that must remain robust across environments and interventions**, we must add:

- causal stability

So we should not collapse causal stability into the previous two conditions. It is not an unconditional requirement for fixed single-environment control. It is the stronger requirement that appears only when the target is upgraded to structural transfer.

This distinction matters a great deal. Otherwise we make one of two opposite mistakes: either we overstate causality and imagine every controllable structure must begin with a causal model, or we understate it and imagine that high performance in one environment already amounts to genuine understanding of the problem.

## VII. Returning To The Main Thread Of "Good Questions"

If we translate this essay back into the language we started with, what it says is:

> A question is asked well not only when it is solvable under current conditions, but, at a stronger level, when the structure it preserves continues to hold after conditions change.

The former corresponds to local correctness; the latter to structural correctness.

The former asks: can you solve it now? The latter asks: is the object you solved actually the stable one?

This also explains why many systems perform brilliantly in the training environment and collapse the moment the environment changes a little. The problem need not lie in optimization ability, nor in the answer itself. It may lie earlier: the problem was never cut at the level of causally stable structure to begin with.

So the full chain can now be stated more completely:

> For fixed control tasks in a single environment, a good question is a state abstraction that is minimally sufficient and closed under control. For robust tasks across environments, a good question must additionally align with causally stable structure.

At this point, "questioning has priority over answering" is no longer rhetoric. It becomes a technically substantive claim. What determines everything downstream is not only whether the value function is learned well, but what you took to be the state in the first place, what you took to be the goal, and whether the structure you preserved is merely local correlation or genuine stable mechanism.
