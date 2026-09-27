# M08 · Machine learning system design: review sheet

Read this only after you have sat the [mock interview](m08-machine-learning-system-design.md).

## 1. Q164

Design a fraud detection system for card transactions.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) · [43](../by-chapter/ch43.md)</sub>

**What a strong answer contains.** Cover extreme imbalance, cost-asymmetric thresholds, real-time latency, label delay from chargebacks, feature freshness, adversarial drift requiring frequent retraining, and a review queue for borderline cases.

## 2. Q98

Where should you set the decision threshold?

<sub>Chapters [23](../by-chapter/ch23.md)</sub>

**What a strong answer contains.** At the break-even point implied by the costs: false positive cost divided by the sum of false positive and false negative costs. Tune it on validation data, never on the test set.

## 3. Q154

Distinguish data drift from concept drift, and say why the distinction matters.

<sub>Chapters [43](../by-chapter/ch43.md)</sub>

**What a strong answer contains.** Data drift changes the input distribution while the input-output relationship holds; concept drift changes that relationship. The first often needs recalibration or a refresh, the second may need new features or a reframed target.

## 4. Q155

What is training-serving skew and how do you prevent it?

<sub>Chapters [43](../by-chapter/ch43.md)</sub>

**What a strong answer contains.** A mismatch between how features are computed in training and in serving, which degrades live performance invisibly. Prevent it with one shared implementation, such as a feature store, rather than two kept in sync manually.

## 5. Q160

How would you govern a machine learning system in production?

<sub>Chapters [44](../by-chapter/ch44.md)</sub>

**What a strong answer contains.** Keep an inventory with risk tiers, document lineage and intended use, measure performance and fairness on a schedule, monitor drift, and assign accountability with a rollback path. NIST’s four functions structure this.

[Back to the mock interview](m08-machine-learning-system-design.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
