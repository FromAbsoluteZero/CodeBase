# AI systems, evaluation, and agents

Applied rather than theoretical: how would you build it, and how would you know it works.

Track: Modern AI · 10 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 2, intermediate 7, advanced 1. Types: conceptual 7, scenario 3.

Answer each question aloud before you open its note.

<a id="q143"></a>

**Q143.** How would you evaluate a new generative feature?

<sub>Chapters [40](../by-chapter/ch40.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Build a task-specific eval set from real usage including known failures, apply deterministic checks first, add model-based grading calibrated against human labels, and report results with uncertainty rather than as point estimates.

</details>

<a id="q144"></a>

**Q144.** What are the pitfalls of using an LLM as a judge?

<sub>Chapters [40](../by-chapter/ch40.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Position, verbosity, and self-preference bias, plus correlated errors when the judge shares a family with the system under test. Mitigate by randomizing order, using pairwise comparison, and measuring agreement with human raters.

</details>

<a id="q145"></a>

**Q145.** Why not just rely on public benchmarks?

<sub>Chapters [40](../by-chapter/ch40.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

They measure general capability, may be contaminated by pretraining data, and do not reflect your distribution. They are useful for model selection, not for deciding whether your system improved.

</details>

<a id="q146"></a>

**Q146.** How do you measure hallucination in a RAG system?

<sub>Chapters [38](../by-chapter/ch38.md) · [40](../by-chapter/ch40.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Check groundedness — the fraction of claims supported by retrieved context — with claim-level annotation or a calibrated judge, and separately measure retrieval recall, since ungrounded answers often begin as retrieval failures.

</details>

<a id="q147"></a>

**Q147.** What are the common failure modes of agents?

<sub>Chapters [41](../by-chapter/ch41.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Compounding error across steps, infinite loops, hallucinated tool calls, misreading tool output, and prompt injection through retrieved content. Mitigations are structural: fewer steps, validation, step budgets, and scoped permissions.

</details>

<a id="q148"></a>

**Q148.** When would you use an agent rather than a single prompt?

<sub>Chapters [41](../by-chapter/ch41.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

When the task requires external information, exact computation, or actions in other systems, and cannot be decomposed into one deterministic call. If a single well-constructed prompt suffices, the agent adds cost and failure surface.

</details>

<a id="q149"></a>

**Q149.** What is prompt injection and how do you defend against it?

<sub>Chapters [41](../by-chapter/ch41.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Instructions embedded in content the model reads, which it may follow as though from the user. Defenses are architectural: treat retrieved content as untrusted data, apply least-privilege tool permissions, and require confirmation before irreversible actions.

</details>

<a id="q150"></a>

**Q150.** How does per-step reliability affect agent design?

<sub>Chapters [41](../by-chapter/ch41.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Success falls exponentially with step count, so a 95% reliable agent completes a twenty-step task about a third of the time. The response is to reduce steps, validate each one, and move deterministic work into code.

</details>

<a id="q151"></a>

**Q151.** Retrieval recall at k is 0.95, but answers are still wrong. Where do you look next?

<sub>Chapters [38](../by-chapter/ch38.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

With the right chunk present almost every time, the fault is downstream of retrieval: chunk boundaries that cut the answer in half, conflicting or irrelevant chunks retrieved alongside the right one, and a prompt that does not tell the model to answer only from the context and to abstain otherwise. Strong answers read a sample of failures by hand before changing anything, because recall at k shows the chunk was present, not that it was used.

Related: [Q139](../by-topic/llms-modern-ai.md#q139)

*Revised: Reworded from a near-duplicate of Q139, which asks for the order of investigation; this question starts from a retrieval stage that already works.*

</details>

<a id="q152"></a>

**Q152.** Why is a similarity threshold an incomplete defence against answering out-of-scope questions?

<sub>Chapters [38](../by-chapter/ch38.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Because a question can score high against a passage it has nothing to do with. Strong answers note that thresholds catch the obvious failures only, and add required citations, an instruction to state when context is insufficient, and deliberate evaluation on questions the corpus cannot answer.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
