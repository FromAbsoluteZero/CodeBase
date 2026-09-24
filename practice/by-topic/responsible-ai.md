# Responsible AI and governance

Once a formality, now a substantive round at any company with regulatory exposure.

Track: Production, responsibility, and design · 6 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 1, intermediate 4, advanced 1. Types: conceptual 4, scenario 2.

Answer each question aloud before you open its note.

<a id="q157"></a>

**Q157.** Name several fairness metrics and explain why you cannot satisfy them all.

<sub>Chapters [44](../by-chapter/ch44.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Demographic parity, equal opportunity, equalized odds, and calibration within groups. When base rates differ these are provably incompatible, so the choice must be justified against the specific harm.

</details>

<a id="q158"></a>

**Q158.** How do SHAP and LIME differ, and when would you reach for each?

<sub>Chapters [29](../by-chapter/ch29.md) · [45](../by-chapter/ch45.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** Chapter 29 teaches SHAP-style attribution; LIME is only named, in the further reading of Chapter 45.

<details>
<summary>What a strong answer contains</summary>

SHAP uses Shapley values with a local accuracy guarantee, so attributions sum exactly to prediction minus baseline, and is exact and fast for trees. LIME fits a local surrogate: quicker, less consistent.

</details>

<a id="q159"></a>

**Q159.** A model does not use race as a feature. Can it still be discriminatory?

<sub>Chapters [44](../by-chapter/ch44.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Yes. Correlated features such as geography or purchase history act as proxies, so disparate outcomes persist. Fairness must be measured on outcomes, not inferred from the feature list.

</details>

<a id="q160"></a>

**Q160.** How would you govern a machine learning system in production?

<sub>Chapters [44](../by-chapter/ch44.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Keep an inventory with risk tiers, document lineage and intended use, measure performance and fairness on a schedule, monitor drift, and assign accountability with a rollback path. NIST’s four functions structure this.

</details>

<a id="q161"></a>

**Q161.** A model declines someone's application. What do you owe them, and which method provides it?

<sub>Chapters [29](../by-chapter/ch29.md) · [44](../by-chapter/ch44.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

A local explanation, not a global one: SHAP decomposes their individual prediction into per-feature contributions summing exactly to their score. Strong answers stress that this explains the model rather than the world, and that presenting a SHAP value as a cause is a mistake with a polished appearance.

</details>

<a id="q162"></a>

**Q162.** Two of your features are correlated at 0.95. What will importance methods report?

<sub>Chapters [29](../by-chapter/ch29.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Both will look unimportant: permuting one leaves the other carrying the signal, so the measured drop is small in each direction, while the pair may be jointly essential. Strong answers permute or drop them as a group and report the pair.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
