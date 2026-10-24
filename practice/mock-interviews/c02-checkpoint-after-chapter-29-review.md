# C02 · Checkpoint: after Chapter 29: review sheet

Read this only after you have sat the [mock interview](c02-checkpoint-after-chapter-29.md).

## 1. Q43

What does it mean for a model to generalize?

<sub>Chapters [16](../by-chapter/ch16.md)</sub>

**What a strong answer contains.** That it performs well on data drawn from the same distribution but not used in training. Strong answers distinguish memorization from generalization and mention held-out evaluation as the only way to estimate it.

## 2. Q47

Why keep a validation set and a test set rather than one holdout?

<sub>Chapters [16](../by-chapter/ch16.md) · [25](../by-chapter/ch25.md)</sub>

**What a strong answer contains.** Validation guides decisions — hyperparameters, features, model choice — and can be consulted repeatedly. The test set estimates final performance and should be used once, because every look spends some of its independence.

## 3. Q50

Name five ways to combat overfitting.

<sub>Chapters [17](../by-chapter/ch17.md) · [16](../by-chapter/ch16.md)</sub>

**What a strong answer contains.** More data, stronger regularization, fewer features, early stopping, dropout, data augmentation, ensembling. The best answers first ask whether training error is low — if it is not, the problem is bias, not variance.

## 4. Q61

How does a decision tree choose a split?

<sub>Chapters [19](../by-chapter/ch19.md)</sub>

**What a strong answer contains.** It evaluates candidate feature and threshold pairs, computes the size-weighted impurity of the resulting children, and picks the split with the greatest impurity reduction. The procedure is greedy and never revisits earlier splits.

## 5. Q64

What is the difference between a random forest and gradient boosting?

<sub>Chapters [20](../by-chapter/ch20.md)</sub>

**What a strong answer contains.** Forests train deep trees independently on bootstrap samples and average to reduce variance; boosting trains shallow trees sequentially on residual errors to reduce bias. Forests are robust with little tuning, boosting has a higher ceiling but is tuning-sensitive.

## 6. Q85

How do you prevent data leakage during preprocessing?

<sub>Chapters [24](../by-chapter/ch24.md) · [16](../by-chapter/ch16.md)</sub>

**What a strong answer contains.** Fit every transformation on training data only and apply it unchanged elsewhere, which in practice means wrapping preprocessing and model in a pipeline so cross-validation refits inside each fold.

## 7. Q94

When would you report PR AUC instead of ROC AUC?

<sub>Chapters [22](../by-chapter/ch22.md)</sub>

**What a strong answer contains.** ROC plots true positive rate against false positive rate and is insensitive to class balance; PR plots precision against recall and reflects performance on the rare positive class. Under heavy imbalance, PR AUC is the more informative summary.

## 8. Q100

Your fraud model has 99.5% accuracy. Is it good?

<sub>Chapters [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md)</sub>

**What a strong answer contains.** Unknown until compared with the majority-class baseline, which is probably about 99.5% as well. Ask for precision, recall at the operating threshold, PR AUC, and the cost of each error type.

## 9. Q109

How do you choose the number of clusters?

<sub>Chapters [26](../by-chapter/ch26.md)</sub>

**What a strong answer contains.** Silhouette score across candidate k, the gap statistic, or external validation against a known outcome. The elbow method is a heuristic on a monotonically decreasing curve and should be described as such.

## 10. Q113

How does PCA work?

<sub>Chapters [27](../by-chapter/ch27.md) · [9](../by-chapter/ch09.md)</sub>

**What a strong answer contains.** Center the data, compute the covariance matrix, take its eigenvectors ordered by eigenvalue, and project onto the leading ones. The eigenvalues give variance explained, which decides how many components to retain.

## 11. Q108

What is wrong with the feature importance a tree model gives you for free?

<sub>Chapters [29](../by-chapter/ch29.md)</sub>

**What a strong answer contains.** It is computed on training data, so overfitted features look useful, and it favours features with many split points, so continuous variables are inflated and binary flags suppressed. Strong answers propose permutation importance on held-out data, reported with its spread across repeats.

[Back to the mock interview](c02-checkpoint-after-chapter-29.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
