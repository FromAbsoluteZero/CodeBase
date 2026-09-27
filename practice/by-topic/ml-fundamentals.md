# Machine learning fundamentals

The screening layer. Asked in nearly every role family, including non-technical ones.

Track: Machine learning · 12 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 8, intermediate 4. Types: conceptual 11, scenario 1.

Answer each question aloud before you open its note.

<a id="q40"></a>

**Q40.** When would you choose not to use machine learning?

<sub>Chapters [1](../by-chapter/ch01.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Strong answers name concrete conditions: the rules are already known and stable, data is scarce, errors are intolerable or must be fully explained, or latency and cost budgets rule out a model. The best answers add that a rules-based or statistical solution is easier to audit and maintain.

</details>

<a id="q41"></a>

**Q41.** Explain the difference between supervised, unsupervised, and reinforcement learning.

<sub>Chapters [1](../by-chapter/ch01.md) · [37](../by-chapter/ch37.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Supervised has labeled input-output pairs and learns a predictor; unsupervised has inputs only and finds structure such as clusters or low-dimensional representations; reinforcement learning has an environment and reward signal and learns a policy through interaction. Naming one real use case for each is expected.

</details>

<a id="q42"></a>

**Q42.** What is a baseline model and why does it matter?

<sub>Chapters [1](../by-chapter/ch01.md) · [15](../by-chapter/ch15.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A trivially simple predictor — majority class, mean, or the incumbent business rule — that establishes the score a real model must beat. It quantifies the value the model actually adds and frequently reveals that a complex model adds nothing.

</details>

<a id="q43"></a>

**Q43.** What does it mean for a model to generalize?

<sub>Chapters [16](../by-chapter/ch16.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

That it performs well on data drawn from the same distribution but not used in training. Strong answers distinguish memorization from generalization and mention held-out evaluation as the only way to estimate it.

</details>

<a id="q44"></a>

**Q44.** Give three concrete examples of data leakage.

<sub>Chapters [16](../by-chapter/ch16.md) · [11](../by-chapter/ch11.md) · [24](../by-chapter/ch24.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Expected answers include a feature populated only after the outcome occurs, fitting a scaler or imputer before splitting, target encoding computed over the full dataset, and duplicate or near-duplicate rows on both sides of the split. Strong answers add that the symptom is implausibly good validation performance.

</details>

<a id="q45"></a>

**Q45.** Why cross-validate instead of using a single train-test split?

<sub>Chapters [16](../by-chapter/ch16.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A single split gives a high-variance estimate that depends on which rows landed where. Cross-validation averages over k splits, uses all data for both training and validation, and provides a spread across folds that indicates estimate stability.

</details>

<a id="q46"></a>

**Q46.** How do you split time-series data, and why is random k-fold invalid?

<sub>Chapters [16](../by-chapter/ch16.md) · [28](../by-chapter/ch28.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Split chronologically, training on the past and validating on the future, often with forward-chaining or expanding windows. Random folds let the model learn from future observations, which inflates performance and cannot be reproduced at prediction time.

Related: [Q106](../by-topic/evaluation-metrics.md#q106)

</details>

<a id="q47"></a>

**Q47.** Why keep a validation set and a test set rather than one holdout?

<sub>Chapters [16](../by-chapter/ch16.md) · [25](../by-chapter/ch25.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Validation guides decisions — hyperparameters, features, model choice — and can be consulted repeatedly. The test set estimates final performance and should be used once, because every look spends some of its independence.

Related: [Q104](../by-topic/evaluation-metrics.md#q104)

</details>

<a id="q48"></a>

**Q48.** Explain the bias-variance tradeoff.

<sub>Chapters [17](../by-chapter/ch17.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Expected error decomposes into squared bias, variance, and irreducible noise; simple models have high bias and low variance, flexible models the reverse. A strong answer ties it to a diagnostic — the gap between training and validation error — rather than reciting the definition.

</details>

<a id="q49"></a>

**Q49.** What is the difference between L1 and L2 regularization?

<sub>Chapters [17](../by-chapter/ch17.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

L1 penalizes absolute values, producing sparsity and implicit feature selection; L2 penalizes squared values, shrinking smoothly and handling correlated features better. Bonus for explaining why L1’s corner yields exact zeros, or the Laplace-versus-Gaussian prior framing.

</details>

<a id="q50"></a>

**Q50.** Name five ways to combat overfitting.

<sub>Chapters [17](../by-chapter/ch17.md) · [16](../by-chapter/ch16.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

More data, stronger regularization, fewer features, early stopping, dropout, data augmentation, ensembling. The best answers first ask whether training error is low — if it is not, the problem is bias, not variance.

</details>

<a id="q51"></a>

**Q51.** Your model has 99% training accuracy and 71% validation accuracy. What do you do?

<sub>Chapters [16](../by-chapter/ch16.md) · [17](../by-chapter/ch17.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Name it as high variance, then act: more data, stronger regularization, less capacity, early stopping, or check for a distribution mismatch. Also verify the split is sound and no duplicate rows inflate the training figure.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
