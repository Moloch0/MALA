# More Ask, Less Answer: How Should We Use LLMs Correctly?

If we continue the whole series of earlier essays into today's technical reality, one of the objects that most needs to be re-understood is the large language model.

Large models have made one formerly expensive thing become suddenly cheap: producing a plausible answer.

Explanation, summary, translation, rewriting, induction, preliminary argument, even a surprising amount of analysis that once required substantial training, can now be generated in a very short time. As a result, a natural but dangerous usage pattern has formed: humans ask, the model answers; humans keep asking, the model keeps answering; as if that were the complete form of "intelligent interaction."

But if the earlier discussion stands, then one question must be clarified first:

> If both questioning and answering can be formalized as `context -> output`, where exactly does the special status of questioning lie?

If this is not clarified first, we will easily mistake "the model is better at answering" for "the model is better at thinking," and mistake "human-machine dialogue" for "the problem has already been written; only the answer is missing."

What really needs correction is precisely that default assumption.

## I. The Difference Between Questioning And Answering Is Not In Form, But In Level

At the most abstract level, both questioning and answering can indeed be written as

$$
\text{context} \to \text{output}.
$$

So if we stare only at the input-output form, there is nothing mystical about questioning. Both are conditional outputs.

But the difference is not there. The difference is that although both output something, they output things with **entirely different functional roles**.

An answer is an object-level mapping. It answers:

> Within this question, what is true?

Questioning is a meta-level mapping. It answers:

> What counts as this question at all? What counts as relevant truth for it?

At that point, to say questioning is "more fundamental" than answering is no longer rhetoric. It is a judgment about level.

Stated more rigorously:

> If both questioning and answering can be written as `context -> output`, then the difference between them lies not in form but in the functional role of what they output. An answer outputs one result inside an already specified problem space. Questioning outputs the problem structure itself: object, unknown, criterion, and admissible path of operation. For that reason, the special status of questioning lies first in the way it governs the downstream search space, and only secondarily in the fact that it comes earlier than answering in causal time and produces a different kind of content in semantic terms.

Two misunderstandings should be removed here.

The first misunderstanding is that it is enough to say "questioning outputs questions, answering outputs answers."  
That is still not enough. It is only a naming difference. It does not explain why the output called a "question" is more upstream than the output called an "answer." The key point is that questioning outputs not ordinary content, but the constraint structure of later solving.

The second misunderstanding is that questioning matters more than answering only because it happens earlier in time.  
That is also insufficient. Anything can happen earlier: motivation comes before the problem, confusion before motivation, environmental stimulation before confusion. Being earlier in time does not automatically mean being more structurally fundamental. What matters is that questioning determines what later counts as the object, the unknown, relevant information, and valid progress.

So the conclusion here can be compressed into one sentence:

> Answering takes a value inside a space; questioning generates the space itself.

Or, in a phrasing better suited to this essay:

> An answer produces a result inside search; questioning produces the mechanism by which search can unfold.

That is why the earlier essays kept insisting that the ceiling of answer quality is determined by whether the problem space was cut correctly. A good answer cannot rescue a bad question. But a good question advances understanding even when it does not yet have an answer, because it has already compressed confusion into a structured unknown.

## II. The Default Way We Use LLMs Today Contains An Over-Strong Assumption

If we accept the distinction above, then one premise in mainstream LLM use today, often ignored, comes into view.

That premise is:

> The user knows what they want to ask.  
> The user has already written the problem into an operable structure.  
> The model only needs to produce a good answer inside that structure.

This can be compressed into a very strong task definition:

$$
u \to a,
$$

where `u` is assumed to be an already well-formed problem, and `a` is simply its answer.

This assumption certainly holds in many simple tasks: looking up a definition, translating a paragraph, explaining a piece of code, summarizing an article, solving a clearly specified problem. In such cases, direct answering is entirely reasonable.

But the genuinely difficult and high-value use cases usually do not satisfy this assumption.

Very often, what the user gives is not a problem, but only:

- a confusion;
- an objective that has not been stratified;
- a mixed demand;
- an under-specified input;
- a piece of problem-material that has not yet been cut into shape.

On the surface, the user says something with a question mark. Cognitively, however, they have not yet provided an operable problem.

For example:

- "I've been off lately. What should I do?"
- "I want to do research, but I don't know where the topic is."
- "This theory seems wrong, but I can't say where it is wrong."
- "I want to learn more effectively."

The difficulty of such inputs is not primarily that "the answer is deep." It is that they usually lack a clear object, a fixed criterion, an explicit task objective, a separation of levels, and any account of what would count as progress. If the model still follows the default pattern and answers immediately upon seeing a question mark, what it is doing is often not solving but guessing for the user inside a huge, unconstrained space.

This is how we get one of the most common illusions in human-machine interaction: the model seems to say many things, and often says them in a highly plausible way, yet the problem has not actually advanced. The real difficulty is not "the answer is still not polished enough," but "the problem itself has not yet been written correctly."

So a more reasonable use of LLMs should no longer assume that they are responsible only for answering. They should be allowed to enter a more upstream stage. That means the model should not only be able to:

- answer;

it should also be able to:

- judge whether the current input already constitutes a solvable problem;
- point out how many different levels of goal have been mixed together;
- identify missing key variables, constraints, and criteria;
- ask clarifying questions;
- propose a few candidate formulations of the problem;
- restate, decompose, and retrieve before answering;
- delay answering when necessary rather than closing immediately.

This means the task definition of an LLM has already changed. It is no longer merely `answering`, but closer to:

$$
\text{problem formulation} + \text{solving}.
$$

The old task is:

$$
\text{user gives question } q \to \text{model gives answer } a.
$$

The new task looks more like:

$$
\text{user gives incomplete expression } u
\to
\text{judge whether it already forms a problem}
\to
\text{if not, perform clarification / restatement / decomposition / retrieval}
\to
\text{obtain a solvable problem } q
\to
\text{then produce answer } a.
$$

This is not a small refinement to answer quality. It is a replacement of the task itself.

## III. The Key Theoretical Boundary Is Whether It Is Worth Iterating First

But a limit must be added immediately.  
"More ask, less answer" does not mean that every scenario should begin with clarification, decomposition, or reframing. Otherwise it would become an empty slogan.

The real question is not "asking is always more advanced than answering." It is:

> Under what conditions is the value of a problem-construction move greater than the value of answering immediately?

That is, the key boundary is not one of attitude, but of value function.

Let some step be an action `a_t`. If it is not a direct answer but a clarification, reframing, retrieval, candidate framing, or problem decomposition, then it is useful if and only if:

$$
\mathbb E[\text{quality of later optimal solving} \mid \text{take } a_t]
-
\mathbb E[\text{quality of direct answer}]
>
\text{cost of that action}.
$$

The cost on the right-hand side is not some abstract word "cost." It is a concrete bundle of things:

- time;
- token budget;
- user burden;
- interaction friction;
- annoyance and user drop-off caused by excessive follow-up;
- and the complexity of the system itself.

This means that "using LLMs correctly" is neither making the model always ask more nor making it always answer less. It means enabling it to switch strategically between "answer directly" and "perform problem construction first."

From this angle, the cases in which "more ask" is correct can be stated rather clearly.

When the following conditions hold, it is usually better to ask first, rewrite first, or decompose first:

- the user's goal is latent, vague, or unstated;
- the input mixes multiple levels of problem together;
- a small amount of clarification can greatly compress the search space;
- one extra round of interaction can introduce genuinely new information;
- if the current problem is not restructured first, direct answering can only amount to blind guessing in a huge space.

When the following conditions hold, direct answering is usually better:

- the task is already well-specified;
- object, goal, and criterion are already sufficiently clear;
- extra follow-up brings in no new information;
- the gain from problem restructuring does not cover the interaction cost;
- what the user wants is already a fast, local, low-friction response.

So one important judgment emerges:

> Correct human-machine interaction is not making the model always answer, nor making it always ask follow-up questions, but enabling it to choose reasonably between answering and rewriting the problem.

Once this step is added, the LLM is no longer merely a one-step mapper. It begins to look like a problem-construction system with strategic choice.

## IV. This Path Is Not Mere Intuition; It Is Supported By Actual Research

If the argument above were only an abstract debate, it would not yet justify a new usage paradigm. But over the past few years, quite a lot of work has converged toward the same direction from different levels.

The first line of work focuses on a direct question: when the input itself is ambiguous, under-specified, or underspecified, is asking for clarification before answering better than answering directly? The answer is usually yes.

`CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models` explicitly proposes that a system should first detect whether a question is ambiguous, generate clarifying questions if it is, and then answer after receiving the added information.  
Link: [https://arxiv.org/abs/2212.07769](https://arxiv.org/abs/2212.07769)

`Asking Clarification Questions to Handle Ambiguity in Open-Domain QA` systematizes that pipeline further into ambiguity detection, clarification-question generation, and clarification-based answering.  
Link: [https://arxiv.org/abs/2305.13808](https://arxiv.org/abs/2305.13808)  
ACL link: [https://aclanthology.org/2023.findings-emnlp.772/](https://aclanthology.org/2023.findings-emnlp.772/)

`Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs` goes one step further. It studies not only "how to follow up," but also "when it is worth following up." That is already very close to the value-function perspective from the previous section.  
Link: [https://arxiv.org/abs/2311.09469](https://arxiv.org/abs/2311.09469)  
NAACL PDF: [https://aclanthology.org/anthology-files/pdf/naacl/2025.naacl-findings.306.pdf](https://aclanthology.org/anthology-files/pdf/naacl/2025.naacl-findings.306.pdf)

The second line of work shows that even without changing model parameters, simply letting the model reorganize the problem at test time before answering can help.

`Measuring and Narrowing the Compositionality Gap in Language Models` proposes `self-ask`, letting the model generate follow-up questions for itself and use those subquestions to drive the final answer.  
Link: [https://arxiv.org/abs/2210.03350](https://arxiv.org/abs/2210.03350)

`Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves` is even more direct: the model first rewrites the user's question into a form that is easier for itself to process, then answers.  
Link: [https://arxiv.org/abs/2311.04205](https://arxiv.org/abs/2311.04205)

`Uncertainty of Thoughts: Uncertainty-Aware Planning Enhances Information Seeking in Large Language Models` raises the question of "what should be asked" into an active information-seeking problem based on uncertainty. It is no longer just "ask once and see," but a way of making problem-construction moves serve later reward maximization.  
Link: [https://arxiv.org/abs/2402.03271](https://arxiv.org/abs/2402.03271)

The third line of work supports something even stronger: if "when to ask, what to ask, and when to stop asking" becomes part of the training objective rather than merely a prompting trick, the effect is often more stable.

`STaR-GATE: Teaching Language Models to Ask Clarifying Questions` explicitly trains models to ask more useful clarification questions rather than only training them to answer.  
Link: [https://arxiv.org/abs/2403.19154](https://arxiv.org/abs/2403.19154)

`Eliciting Human Preferences with Language Models` proposes `GATE`, whose core is not answering an already written task, but actively eliciting user preferences and task intent through language interaction.  
Link: [https://arxiv.org/abs/2310.11589](https://arxiv.org/abs/2310.11589)

The fourth line of work shows that this is not only useful in abstract dialogue tasks, but also in very concrete engineering tasks.

`Python Code Generation by Asking Clarification Questions` directly shows that natural-language requirements are often under-specified, and that asking clarifying questions before generating code can improve code-generation quality.  
Link: [https://aclanthology.org/2023.acl-long.799/](https://aclanthology.org/2023.acl-long.799/)

Taken together, these works are still distributed across labels such as clarification, interactive QA, self-ask, information seeking, and task elicitation. But they converge on a more general conclusion:

> LLMs should not be understood only as systems that answer already specified questions. They should be allowed to enter the processes of problem formation, problem revision, and information acquisition.

In other words, current research has not yet fully rewritten the post-training objective of general LLMs into "construct the problem first, then solve it." But it has already shown from multiple directions that this path is not only reasonable, but effective.

## V. More Ask, Less Answer: This Is Not Opposition To Answers, But A Correction Of Their Place

Now we can return to the title itself.

If "more ask, less answer" is misunderstood, it turns into a postural slogan, as though the best future model would be one that gives fewer answers and throws more questions back. That is not the point here.

What it really means is:

> When the problem has not yet taken shape, answering too early is often a kind of pseudo-efficiency;  
> by contrast, appropriately following up, reframing, clarifying, and decomposing is a higher-level form of progress.

So "less answer" does not mean do not answer. It means do not rush to seal the discussion with a smooth answer before the problem space has been cut properly.  
"More ask" does not mean mechanically increasing the number of question marks. It means restoring questioning as a structural move: using it to locate the unknown, compress degrees of freedom, distinguish levels, and organize the search that follows.

This also means the division of labor between human and model must be redefined.

The old division of labor is:

- the human provides the question;
- the model provides the answer.

The new division of labor is closer to this:

- the human provides confusion, goal, background, constraints, and local intuition;
- the model helps judge whether there is already a genuinely formed problem here;
- if not, both sides jointly compress the space through clarification, restatement, decomposition, and retrieval;
- after the problem has been written correctly, the model enters answering;
- finally, the answer is checked again to see whether it solves the original problem or merely glows near it.

Only at that point does human-machine interaction form a complete cycle, rather than a situation where the human keeps asking and the LLM keeps answering.

Otherwise, what we call "dialogue" is still only a one-way pipe: the human keeps disguising under-formed confusion as a problem, and the model keeps disguising badly cut problems as answers. Interaction happens, but the loop never truly closes.

The truly closed structure should be:

$$
\text{confusion and goals}
\to
\text{problem construction}
\to
\text{solving}
\to
\text{substitution-back verification}
\to
\text{continue revising the problem}.
$$

Only with this step does the LLM stop being merely a faster answering machine and become a participant in problem construction. And only with this step does human-machine interaction move from the one-way structure of "human asks, machine answers" to the fuller cycle of "human and machine jointly compress space, jointly define the problem, and jointly advance the solution."

> To use an LLM correctly is not to treat it as a faster answering machine, but to place it inside the cycle of problem construction; not to assume the user already knows what they are asking, but to recognize that the hardest part often lies precisely in the fact that the problem has not yet been written correctly.
