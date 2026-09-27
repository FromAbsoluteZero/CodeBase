# Production and MLOps

Asked of anyone whose model will meet real traffic.

Track: Production, responsibility, and design · 4 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: intermediate 4. Types: conceptual 4.

Answer each question aloud before you open its note.

<a id="q153"></a>

**Q153.** How do you detect that a deployed model is degrading?

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Monitor leading indicators continuously — input and prediction distributions, stability indices such as PSI, and business metrics — because labels arrive late. Confirm with measured performance once labels mature.

</details>

<a id="q154"></a>

**Q154.** Distinguish data drift from concept drift, and say why the distinction matters.

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Data drift changes the input distribution while the input-output relationship holds; concept drift changes that relationship. The first often needs recalibration or a refresh, the second may need new features or a reframed target.

</details>

<a id="q155"></a>

**Q155.** What is training-serving skew and how do you prevent it?

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** Training-serving skew and feature stores are not named in this book. Chapter 43 covers the production problems they address.

<details>
<summary>What a strong answer contains</summary>

A mismatch between how features are computed in training and in serving, which degrades live performance invisibly. Prevent it with one shared implementation, such as a feature store, rather than two kept in sync manually.

</details>

<a id="q156"></a>

**Q156.** How would you deploy a new model safely?

<sub>Chapters [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** Shadow and canary deployment are not covered in this book. Chapter 43 covers serving, drift and monitoring.

<details>
<summary>What a strong answer contains</summary>

Shadow it against live traffic first, then canary a small share while watching metrics and guardrails, expand gradually, and keep rollback to the previous registered version a one-step operation.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
