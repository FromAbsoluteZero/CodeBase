# Machine learning system design

The open-ended round. There is no correct answer; there is a correct way to reason.

Track: Production, responsibility, and design · 5 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: intermediate 1, advanced 4. Types: scenario 5.

Answer each question aloud before you open its note.

<a id="q163"></a>

**Q163.** Design a system to recommend products to users.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) · [42](../by-chapter/ch42.md) · [43](../by-chapter/ch43.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Clarify the objective and constraints first, then cover candidate generation and ranking, features and labels, cold start, offline and online metrics, latency budget, and feedback loops that can entrench popular items.

</details>

<a id="q164"></a>

**Q164.** Design a fraud detection system for card transactions.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) · [43](../by-chapter/ch43.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Cover extreme imbalance, cost-asymmetric thresholds, real-time latency, label delay from chargebacks, feature freshness, adversarial drift requiring frequent retraining, and a review queue for borderline cases.

</details>

<a id="q165"></a>

**Q165.** Design a retrieval-augmented question answering system over company documents.

<sub>Chapters [38](../by-chapter/ch38.md) · [40](../by-chapter/ch40.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Cover chunking strategy, embedding choice and re-indexing cost, vector store, retrieval evaluation with recall at k, reranking, grounding and citations, abstention when context is thin, and cost and latency per query.

</details>

<a id="q166"></a>

**Q166.** How would you serve a model with a 50 millisecond latency budget?

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Budget the whole path, not just inference: network, feature retrieval, model, and overhead. Levers include caching, precomputed features, batching, quantization, distillation, and dropping to a smaller model with a fallback.

</details>

<a id="q167"></a>

**Q167.** How do you decide between batch and online inference?

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Batch when predictions can be precomputed and freshness in hours is acceptable; online when inputs are only known at request time. Batch is cheaper and simpler to monitor, so it should be the default.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
