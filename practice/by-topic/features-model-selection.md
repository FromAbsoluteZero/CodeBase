# Data, features, and model selection

Where most real projects succeed or fail, and where experienced candidates separate themselves.

Track: Machine learning · 8 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 2, intermediate 5, advanced 1. Types: conceptual 7, scenario 1.

Answer each question aloud before you open its note.

<a id="q85"></a>

**Q85.** How do you prevent data leakage during preprocessing?

<sub>Chapters [24](../by-chapter/ch24.md) · [16](../by-chapter/ch16.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Fit every transformation on training data only and apply it unchanged elsewhere, which in practice means wrapping preprocessing and model in a pipeline so cross-validation refits inside each fold.

</details>

<a id="q86"></a>

**Q86.** When would you use target encoding instead of one-hot?

<sub>Chapters [24](../by-chapter/ch24.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

When cardinality is high enough that one-hot would explode the feature space. It must be computed within folds and smoothed toward the global mean, or it leaks the label into the feature.

</details>

<a id="q87"></a>

**Q87.** How do you handle missing values?

<sub>Chapters [11](../by-chapter/ch11.md) · [24](../by-chapter/ch24.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Ask first why they are missing. Then impute with a simple statistic or a model, add a binary missingness indicator so the absence itself is usable, and fit the imputer inside the pipeline.

</details>

<a id="q88"></a>

**Q88.** Which models require feature scaling and which do not?

<sub>Chapters [21](../by-chapter/ch21.md) · [24](../by-chapter/ch24.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Distance-based methods such as kNN and SVM, and gradient-based methods including neural networks and regularized linear models, need scaling. Tree-based models do not, since splits depend only on ordering.

</details>

<a id="q89"></a>

**Q89.** Compare grid, random, and Bayesian search.

<sub>Chapters [25](../by-chapter/ch25.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Grid is exhaustive over a lattice and scales exponentially; random samples independently and covers important dimensions better per unit budget; Bayesian methods model the objective and propose promising points, paying more per proposal for fewer evaluations.

</details>

<a id="q90"></a>

**Q90.** What is nested cross-validation and why use it?

<sub>Chapters [25](../by-chapter/ch25.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

An inner loop selects hyperparameters and an outer loop evaluates the entire selection procedure on folds never used for selection. It removes the optimistic bias of reporting the best inner score.

</details>

<a id="q91"></a>

**Q91.** Why sample learning rates on a log scale?

<sub>Chapters [25](../by-chapter/ch25.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

They act multiplicatively and span orders of magnitude, so uniform sampling concentrates almost all draws in the largest decade and barely explores small values.

</details>

<a id="q92"></a>

**Q92.** You tried 200 configurations and the best validation accuracy is 0.91. What do you report?

<sub>Chapters [25](../by-chapter/ch25.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Not 0.91. That is the maximum of 200 noisy estimates and is biased upward; report a nested CV estimate or the score on a test set that played no part in selection.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
