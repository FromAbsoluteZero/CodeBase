# Large language models and modern AI

New, fast-moving, and increasingly the round that decides the offer.

Track: Modern AI · 10 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 3, intermediate 5, advanced 2. Types: conceptual 7, scenario 3.

Answer each question aloud before you open its note.

<a id="q133"></a>

**Q133.** What is the Chinchilla finding and why did it matter?

<sub>Chapters [36](../by-chapter/ch36.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** Chapter 36 cites the Chinchilla paper; the figures in this note come from the paper, not from the chapter.

<details>
<summary>What a strong answer contains</summary>

That compute-optimal training balances parameters and tokens at roughly twenty tokens per parameter, showing prevailing models were undertrained. A 70B model on 1.4T tokens beat the 280B Gopher on the same compute budget: four times fewer parameters, trained on nearly five times as much data (1.4T tokens against Gopher's 300B).

*Revised: Corrected: the printed manuscript said four times more data; 1.4T against 300B tokens is nearly five times.*

</details>

<a id="q134"></a>

**Q134.** Explain temperature and top-p sampling.

<sub>Chapters [36](../by-chapter/ch36.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Temperature divides logits before the softmax, sharpening below one and flattening above. Top-p keeps the smallest token set whose cumulative probability exceeds p, adapting the candidate count to model confidence rather than fixing it.

</details>

<a id="q135"></a>

**Q135.** What is byte pair encoding and why do models use subword tokens?

<sub>Chapters [36](../by-chapter/ch36.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

An algorithm that builds a vocabulary by repeatedly merging the most frequent adjacent pairs. Subwords balance vocabulary size against sequence length and handle unseen words gracefully by decomposing them.

</details>

<a id="q136"></a>

**Q136.** Why do language models struggle to count letters in a word?

<sub>Chapters [36](../by-chapter/ch36.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

They operate on subword tokens, not characters, so character-level structure is not directly visible. The task requires information the tokenization has already discarded.

</details>

<a id="q137"></a>

**Q137.** RAG or fine-tuning — how do you decide?

<sub>Chapters [38](../by-chapter/ch38.md) · [39](../by-chapter/ch39.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

RAG for knowledge that changes, needs citation, or is too specific to bake into weights; fine-tuning for behavior, format, and style. They are complementary, and many systems need neither once prompting is done well.

</details>

<a id="q138"></a>

**Q138.** How does LoRA work and why is it cheap?

<sub>Chapters [39](../by-chapter/ch39.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It freezes the pretrained matrix and learns a low-rank correction as the product of two thin matrices, so trainable parameters scale with rank times the sum of dimensions rather than their product. Adapters are small and swappable per task.

</details>

<a id="q139"></a>

**Q139.** Your RAG system gives wrong answers. How do you debug it?

<sub>Chapters [38](../by-chapter/ch38.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Measure retrieval first with recall at k — the generator cannot use what was never retrieved. Then examine chunking, embedding quality, and reranking, and only then the generation prompt and abstention instructions.

Related: [Q151](../by-topic/ai-systems-agents.md#q151)

</details>

<a id="q140"></a>

**Q140.** How do you reduce hallucination in a generative system?

<sub>Chapters [38](../by-chapter/ch38.md) · [40](../by-chapter/ch40.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Ground answers in retrieved sources, require citations, instruct abstention when context is insufficient, constrain output format, and evaluate against a fixed set with human review. No single measure eliminates it.

</details>

<a id="q141"></a>

**Q141.** What does the KL penalty do in RLHF, and what happens without it?

<sub>Chapters [37](../by-chapter/ch37.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It charges the policy for drifting from the pretrained model, trading expected reward against distance. Without it the optimizer finds wherever the reward model peaks and goes there, collapsing onto a single high-scoring output. Strong answers describe beta as the tension in that tether.

</details>

<a id="q142"></a>

**Q142.** Your RLHF run shows reward climbing steadily. Why is that not sufficient evidence?

<sub>Chapters [37](../by-chapter/ch37.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

The reward model is a proxy fitted to human labels, and human labels favour confidence, length, and agreement. Past a point the only way left to raise the proxy is to exploit where it diverges from real quality, so reward rises while outcomes worsen. Strong answers monitor KL divergence and evaluate on something the reward model did not produce.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
