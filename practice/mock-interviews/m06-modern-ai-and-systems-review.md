# M06 · Modern AI and AI systems: review sheet

Read this only after you have sat the [mock interview](m06-modern-ai-and-systems.md).

## 1. Q123

Why did attention replace recurrence rather than complement it?

<sub>Chapters [33](../by-chapter/ch33.md) · [34](../by-chapter/ch34.md)</sub>

**What a strong answer contains.** Attention is parallelizable across the sequence and gives every position a direct path to every other, while recurrence is inherently sequential and attenuates long-range signal. At scale the hardware efficiency was decisive.

## 2. Q127

How does a transformer know the order of tokens?

<sub>Chapters [34](../by-chapter/ch34.md)</sub>

**What a strong answer contains.** It does not inherently: self-attention is permutation-equivariant, so shuffling the input just shuffles the outputs in the same way. Position must be injected explicitly, through sinusoidal, learned, or rotary positional encodings.

## 3. Q133

What is the Chinchilla finding and why did it matter?

<sub>Chapters [36](../by-chapter/ch36.md)</sub>

**What a strong answer contains.** That compute-optimal training balances parameters and tokens at roughly twenty tokens per parameter, showing prevailing models were undertrained. A 70B model on 1.4T tokens beat the 280B Gopher on the same compute budget: four times fewer parameters, trained on nearly five times as much data (1.4T tokens against Gopher's 300B).

## 4. Q134

Explain temperature and top-p sampling.

<sub>Chapters [36](../by-chapter/ch36.md)</sub>

**What a strong answer contains.** Temperature divides logits before the softmax, sharpening below one and flattening above. Top-p keeps the smallest token set whose cumulative probability exceeds p, adapting the candidate count to model confidence rather than fixing it.

## 5. Q137

RAG or fine-tuning — how do you decide?

<sub>Chapters [38](../by-chapter/ch38.md) · [39](../by-chapter/ch39.md)</sub>

**What a strong answer contains.** RAG for knowledge that changes, needs citation, or is too specific to bake into weights; fine-tuning for behavior, format, and style. They are complementary, and many systems need neither once prompting is done well.

## 6. Q139

Your RAG system gives wrong answers. How do you debug it?

<sub>Chapters [38](../by-chapter/ch38.md)</sub>

**What a strong answer contains.** Measure retrieval first with recall at k — the generator cannot use what was never retrieved. Then examine chunking, embedding quality, and reranking, and only then the generation prompt and abstention instructions.

## 7. Q144

What are the pitfalls of using an LLM as a judge?

<sub>Chapters [40](../by-chapter/ch40.md)</sub>

**What a strong answer contains.** Position, verbosity, and self-preference bias, plus correlated errors when the judge shares a family with the system under test. Mitigate by randomizing order, using pairwise comparison, and measuring agreement with human raters.

## 8. Q147

What are the common failure modes of agents?

<sub>Chapters [41](../by-chapter/ch41.md)</sub>

**What a strong answer contains.** Compounding error across steps, infinite loops, hallucinated tool calls, misreading tool output, and prompt injection through retrieved content. Mitigations are structural: fewer steps, validation, step budgets, and scoped permissions.

## 9. Q149

What is prompt injection and how do you defend against it?

<sub>Chapters [41](../by-chapter/ch41.md)</sub>

**What a strong answer contains.** Instructions embedded in content the model reads, which it may follow as though from the user. Defenses are architectural: treat retrieved content as untrusted data, apply least-privilege tool permissions, and require confirmation before irreversible actions.

## 10. Q150

How does per-step reliability affect agent design?

<sub>Chapters [41](../by-chapter/ch41.md)</sub>

**What a strong answer contains.** Success falls exponentially with step count, so a 95% reliable agent completes a twenty-step task about a third of the time. The response is to reduce steps, validate each one, and move deterministic work into code.

## 11. Q152

Why is a similarity threshold an incomplete defence against answering out-of-scope questions?

<sub>Chapters [38](../by-chapter/ch38.md)</sub>

**What a strong answer contains.** Because a question can score high against a passage it has nothing to do with. Strong answers note that thresholds catch the obvious failures only, and add required citations, an instruction to state when context is insufficient, and deliberate evaluation on questions the corpus cannot answer.

[Back to the mock interview](m06-modern-ai-and-systems.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
