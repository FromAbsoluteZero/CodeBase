# Classical algorithms and trade-offs

The breadth round. Interviewers are checking that you can compare methods, not recite one.

Track: Machine learning · 21 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 5, intermediate 12, advanced 4. Types: conceptual 19, scenario 2.

Answer each question aloud before you open its note.

<a id="q52"></a>

**Q52.** Derive the closed-form solution for ordinary least squares.

<sub>Chapters [13](../by-chapter/ch13.md) · [10](../by-chapter/ch10.md) · [9](../by-chapter/ch09.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Write the loss in matrix form, differentiate with respect to w to get minus two X-transpose times (y minus Xw), set to zero, and solve to reach w equals (X-transpose-X) inverse times X-transpose-y. Strong candidates add that in practice you solve rather than invert.

</details>

<a id="q53"></a>

**Q53.** When would you prefer gradient descent over the normal equation?

<sub>Chapters [13](../by-chapter/ch13.md) · [18](../by-chapter/ch18.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

When the feature count is large enough that forming or factorizing the d-by-d matrix is impractical, when data arrives in streams or does not fit in memory, or when the model has no closed form. The crossover is usually somewhere in the thousands of features.

</details>

<a id="q54"></a>

**Q54.** What are the assumptions of linear regression?

<sub>Chapters [13](../by-chapter/ch13.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Linearity in the parameters, independent errors, homoscedasticity, and approximately normal residuals for valid inference. A strong answer notes that prediction can survive mild violations while confidence intervals and p-values do not.

</details>

<a id="q55"></a>

**Q55.** Two of your features are highly correlated. What happens and what do you do?

<sub>Chapters [13](../by-chapter/ch13.md) · [17](../by-chapter/ch17.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Coefficients become unstable and hard to interpret while predictions may remain acceptable. Remedies include dropping one feature, combining them, or applying ridge regularization, which resolves the near-tie by preferring smaller weights.

</details>

<a id="q56"></a>

**Q56.** Why use cross-entropy rather than mean squared error for classification?

<sub>Chapters [14](../by-chapter/ch14.md) · [30](../by-chapter/ch30.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Cross-entropy is the negative log-likelihood of a Bernoulli outcome and is convex in the weights, while squared error through a sigmoid is non-convex and produces vanishing gradients on confidently wrong predictions.

</details>

<a id="q57"></a>

**Q57.** Derive the gradient of the logistic loss.

<sub>Chapters [14](../by-chapter/ch14.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Differentiating the cross-entropy with respect to w yields X-transpose times (sigma(Xw) minus y), divided by n. Strong candidates note it has the same form as linear regression’s gradient.

</details>

<a id="q58"></a>

**Q58.** Is the decision boundary of logistic regression linear?

<sub>Chapters [14](../by-chapter/ch14.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Yes, in the feature space provided. The sigmoid is nonlinear but monotone, so the set where probability equals one half is where the linear score is zero. Curved boundaries require engineered nonlinear features.

</details>

<a id="q59"></a>

**Q59.** How do you interpret a logistic regression coefficient?

<sub>Chapters [14](../by-chapter/ch14.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

As the change in log-odds per unit increase in that feature, holding others fixed; exponentiating gives the odds multiplier. The key precision is that it multiplies odds, not probability.

</details>

<a id="q60"></a>

**Q60.** Entropy or Gini: does the choice of impurity measure change the tree?

<sub>Chapters [19](../by-chapter/ch19.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Both measure node impurity: entropy is the information-theoretic measure in bits, Gini is the probability that two random members differ in label. They select similar splits; Gini is slightly cheaper and is scikit-learn’s default.

</details>

<a id="q61"></a>

**Q61.** How does a decision tree choose a split?

<sub>Chapters [19](../by-chapter/ch19.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It evaluates candidate feature and threshold pairs, computes the size-weighted impurity of the resulting children, and picks the split with the greatest impurity reduction. The procedure is greedy and never revisits earlier splits.

</details>

<a id="q62"></a>

**Q62.** How do you stop a decision tree from overfitting?

<sub>Chapters [19](../by-chapter/ch19.md) · [20](../by-chapter/ch20.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Limit depth, require minimum samples per split or per leaf, cap the number of leaves, or grow fully and prune back using cost-complexity pruning. Ensembling, covered next, is the other standard answer.

</details>

<a id="q63"></a>

**Q63.** When do decision trees perform poorly?

<sub>Chapters [19](../by-chapter/ch19.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

When the true boundary is diagonal or smooth, since axis-aligned splits approximate it as a staircase; also with strongly linear relationships, which a linear model captures with one coefficient and a tree needs many splits for.

</details>

<a id="q64"></a>

**Q64.** What is the difference between a random forest and gradient boosting?

<sub>Chapters [20](../by-chapter/ch20.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Forests train deep trees independently on bootstrap samples and average to reduce variance; boosting trains shallow trees sequentially on residual errors to reduce bias. Forests are robust with little tuning, boosting has a higher ceiling but is tuning-sensitive.

</details>

<a id="q65"></a>

**Q65.** Why does bagging reduce variance?

<sub>Chapters [20](../by-chapter/ch20.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Averaging B models with pairwise correlation rho leaves rho times the variance plus the remainder divided by B. Only decorrelated error shrinks, which is why random forests also subsample features at each split.

</details>

<a id="q66"></a>

**Q66.** What does the learning rate do in gradient boosting?

<sub>Chapters [20](../by-chapter/ch20.md) · [25](../by-chapter/ch25.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It shrinks each tree’s contribution, so more trees are needed but the ensemble generalizes better. Learning rate and number of trees are tuned jointly, usually with early stopping on a validation set.

</details>

<a id="q67"></a>

**Q67.** Why is a random forest relatively insensitive to the number of trees?

<sub>Chapters [20](../by-chapter/ch20.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Each tree is trained independently, so adding more refines the average toward its expectation rather than fitting new error. Boosting differs because each added tree deliberately fits remaining residuals, including noise.

</details>

<a id="q68"></a>

**Q68.** Explain the kernel trick.

<sub>Chapters [21](../by-chapter/ch21.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The optimization depends on the data only through inner products, so replacing each inner product with a kernel function computes the result of an implicit mapping to a higher-dimensional space without constructing it. The RBF kernel corresponds to an infinite-dimensional space.

</details>

<a id="q69"></a>

**Q69.** Why do support vector machines maximize the margin?

<sub>Chapters [21](../by-chapter/ch21.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A wider margin makes the boundary more robust to sampling variation and supports better generalization bounds. Only the closest points, the support vectors, determine the solution.

</details>

<a id="q70"></a>

**Q70.** What is the computational cost of kNN at prediction time?

<sub>Chapters [21](../by-chapter/ch21.md) · [38](../by-chapter/ch38.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Naively order n times d per query, since it computes distance to every stored point. Approximate nearest-neighbor indexes reduce this and are what production vector search relies on.

</details>

<a id="q71"></a>

**Q71.** How do you choose k in k-nearest neighbors?

<sub>Chapters [21](../by-chapter/ch21.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

By cross-validation, using odd values to avoid ties in binary problems. Small k gives high variance and a jagged boundary; large k smooths toward the majority class and raises bias.

</details>

<a id="q72"></a>

**Q72.** Why do tree models struggle on a trending time series?

<sub>Chapters [28](../by-chapter/ch28.md) · [19](../by-chapter/ch19.md) · [20](../by-chapter/ch20.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

A tree predicts the average of training targets in a leaf, so its output cannot exceed the range it was trained on. A trending series puts the test period above everything seen, and the model cannot reach it at any depth. Strong answers propose removing the trend first, or predicting a difference rather than a level.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
