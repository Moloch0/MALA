# Questioning As An Algorithm

If the earlier essays merely separated the problem from language, this step goes further: we no longer treat questioning as a speech act, but as a solvable structure.

This is a key turn. Once we look at it this way, many judgments that previously seemed abstract suddenly become concrete. Why does a good question make people "know what to do next"? Why does a bad question make discussion keep diffusing without ever progressing? Why do some questions, once clearly stated, almost produce their own method? All of these phenomena suggest that questioning is not merely requesting information from outside; it is in fact organizing a search process.

A real problem contains at least five things implicitly: known conditions, an unknown target, allowed operations, a criterion of judgment, and a termination condition. Without known conditions, nothing can begin. Without an unknown target, one does not know what is to be solved. Without allowed operations, one does not know what transformations are permitted. Without a criterion, one does not know what counts as having solved it. Without a termination condition, one does not know when to stop. As these five things become clearer, thought begins to reveal an algorithmic skeleton.

This is also the point at which questioning departs from ordinary conversation. Ordinary conversation can keep expanding around a theme: more and more information, yet not necessarily more structure. Real questioning is different. It forces you to distinguish relevant information from noise, the current gap from later branches, what needs to be defined from what needs to be verified, and what must be temporarily bracketed. Thought no longer means simply "keep talking"; it begins to appear as a sequence of explicit operations.

Those operations themselves are algorithmic.

When a large problem cannot be solved directly, we break it into subproblems; that is decomposition. When a subproblem resembles the original in its mode of solution, we repeat the same structure; that is recursion. When a candidate answer must be checked against the known conditions for consistency, we are doing verification. When multiple possibilities conflict, we do elimination, refutation, and cancellation. When a problem has several directions of expansion, we compare branches, estimate costs, and decide which path to search first; that is search and pruning.

So what it means to "know how to think" is not merely to know a lot of content. More importantly, it is the ability to rewrite vague confusion into a form that these operations can take over. In other words, questioning does not produce content. It defines a procedure that can keep advancing content.

A helpful analogy here is the search tree. A clear question often looks like a tree that can be unfolded step by step: what the current node is, what branches are available below it, what extra information each branch requires, which branches can be cut early, and which branches are worth pursuing further. In such a structure, questioning is not blindly asking in every direction; it is deciding how the tree unfolds.

But the analogy has limits. For mature problems, such as solving an exercise, proving a lemma, or making a diagnosis, the nodes and branches of the tree are often already clear, and questioning mainly selects a route within them. For genuinely deep problems, however, the difficulty is not even that "the tree is too large," but that "the tree has not grown yet." Then the first thing we must do is often not search, but invent what the nodes are, what the branching rules are, which variations should be preserved, and which details should be ignored. That is, the first step of a deep problem is not search, but the construction of the search space.

At that point the place of answers becomes easier to see as well. An answer usually does not look like a tree, but rather like a compressed residue left by some search. It may be a local conclusion, a rule of thumb, a high-value direction, or an intermediate result that has already been folded up. It matters, because without such compression search cannot accumulate or be transmitted. But it remains a product of the search process, not the search structure itself.

So an answer is more like a cache, while a question is more like a program. The answer stores what has already been obtained; the question specifies how to continue. A person may be very good at caching, which is to say, good at restating, summarizing, and organizing conclusions. But if that person cannot keep rewriting new confusion into structures that can advance, their thinking remains limited.

This has an even deeper implication. If questioning organizes search, then a truly good question must satisfy a stronger condition in the end: it must not only unfold, but unfold recursively. That is, after the problem advances, the subsequent situation should still preserve some kind of structural tractability. Otherwise each step of progress makes the problem itself less controllable, until it falls back into chaos.

This brings us to the next step. What should a problem structure look like if it is to support stable recursive solution? Once we try to write that requirement formally, we quickly enter a familiar and powerful framework: the Markov decision process, or MDP.
