# M04 · Machine learning breadth screen: review sheet

Read this only after you have sat the [mock interview](m04-machine-learning-breadth-screen.md).

## 1. Q42

What is a baseline model and why does it matter?

<sub>Chapters [1](../by-chapter/ch01.md) · [15](../by-chapter/ch15.md)</sub>

**What a strong answer contains.** A trivially simple predictor — majority class, mean, or the incumbent business rule — that establishes the score a real model must beat. It quantifies the value the model actually adds and frequently reveals that a complex model adds nothing.

## 2. Q44

Give three concrete examples of data leakage.

<sub>Chapters [16](../by-chapter/ch16.md) · [11](../by-chapter/ch11.md) · [24](../by-chapter/ch24.md)</sub>

**What a strong answer contains.** Expected answers include a feature populated only after the outcome occurs, fitting a scaler or imputer before splitting, target encoding computed over the full dataset, and duplicate or near-duplicate rows on both sides of the split. Strong answers add that the symptom is implausibly good validation performance.

## 3. Q45

Why cross-validate instead of using a single train-test split?

<sub>Chapters [16](../by-chapter/ch16.md)</sub>

**What a strong answer contains.** A single split gives a high-variance estimate that depends on which rows landed where. Cross-validation averages over k splits, uses all data for both training and validation, and provides a spread across folds that indicates estimate stability.

## 4. Q48

Explain the bias-variance tradeoff.

<sub>Chapters [17](../by-chapter/ch17.md)</sub>

**What a strong answer contains.** Expected error decomposes into squared bias, variance, and irreducible noise; simple models have high bias and low variance, flexible models the reverse. A strong answer ties it to a diagnostic — the gap between training and validation error — rather than reciting the definition.

## 5. Q51

Your model has 99% training accuracy and 71% validation accuracy. What do you do?

<sub>Chapters [16](../by-chapter/ch16.md) · [17](../by-chapter/ch17.md)</sub>

**What a strong answer contains.** Name it as high variance, then act: more data, stronger regularization, less capacity, early stopping, or check for a distribution mismatch. Also verify the split is sound and no duplicate rows inflate the training figure.

## 6. Q55

Two of your features are highly correlated. What happens and what do you do?

<sub>Chapters [13](../by-chapter/ch13.md) · [17](../by-chapter/ch17.md)</sub>

**What a strong answer contains.** Coefficients become unstable and hard to interpret while predictions may remain acceptable. Remedies include dropping one feature, combining them, or applying ridge regularization, which resolves the near-tie by preferring smaller weights.

## 7. Q64

What is the difference between a random forest and gradient boosting?

<sub>Chapters [20](../by-chapter/ch20.md)</sub>

**What a strong answer contains.** Forests train deep trees independently on bootstrap samples and average to reduce variance; boosting trains shallow trees sequentially on residual errors to reduce bias. Forests are robust with little tuning, boosting has a higher ceiling but is tuning-sensitive.

## 8. Q88

Which models require feature scaling and which do not?

<sub>Chapters [21](../by-chapter/ch21.md) · [24](../by-chapter/ch24.md)</sub>

**What a strong answer contains.** Distance-based methods such as kNN and SVM, and gradient-based methods including neural networks and regularized linear models, need scaling. Tree-based models do not, since splits depend only on ordering.

## 9. Q92

You tried 200 configurations and the best validation accuracy is 0.91. What do you report?

<sub>Chapters [25](../by-chapter/ch25.md)</sub>

**What a strong answer contains.** Not 0.91. That is the maximum of 200 noisy estimates and is biased upward; report a nested CV estimate or the score on a test set that played no part in selection.

## 10. Q96

Your model has AUC 0.92 but is useless in production. What could explain that?

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) · [43](../by-chapter/ch43.md)</sub>

**What a strong answer contains.** A threshold that has never been tuned, severe imbalance making precision poor despite good ranking, miscalibrated probabilities feeding a downstream decision, distribution shift, or optimizing a metric that does not match the business cost.

## 11. Q98

Where should you set the decision threshold?

<sub>Chapters [23](../by-chapter/ch23.md)</sub>

**What a strong answer contains.** At the break-even point implied by the costs: false positive cost divided by the sum of false positive and false negative costs. Tune it on validation data, never on the test set.

[Back to the mock interview](m04-machine-learning-breadth-screen.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
