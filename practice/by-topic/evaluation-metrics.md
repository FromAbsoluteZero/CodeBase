# Evaluation and metrics

The most common source of a confidently wrong answer. Know what each metric hides.

Track: Machine learning · 16 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 6, intermediate 10. Types: conceptual 11, scenario 5.

Answer each question aloud before you open its note.

<a id="q93"></a>

**Q93.** When does precision matter more than recall, and vice versa?

<sub>Chapters [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Precision when false alarms are costly, as in spam filtering or automated account suspension; recall when misses are costly, as in disease screening or fraud detection. The right answer names the cost asymmetry explicitly.

</details>

<a id="q94"></a>

**Q94.** When would you report PR AUC instead of ROC AUC?

<sub>Chapters [22](../by-chapter/ch22.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

ROC plots true positive rate against false positive rate and is insensitive to class balance; PR plots precision against recall and reflects performance on the rare positive class. Under heavy imbalance, PR AUC is the more informative summary.

</details>

<a id="q95"></a>

**Q95.** What does calibration mean and how would you check it?

<sub>Chapters [22](../by-chapter/ch22.md) · [44](../by-chapter/ch44.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

That predicted probabilities match observed frequencies — of cases predicted at 0.7, about seventy percent should be positive. Check with a reliability diagram or Brier score; fix with Platt scaling or isotonic regression.

</details>

<a id="q96"></a>

**Q96.** Your model has AUC 0.92 but is useless in production. What could explain that?

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) · [43](../by-chapter/ch43.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

A threshold that has never been tuned, severe imbalance making precision poor despite good ranking, miscalibrated probabilities feeding a downstream decision, distribution shift, or optimizing a metric that does not match the business cost.

</details>

<a id="q97"></a>

**Q97.** How do you handle imbalanced data?

<sub>Chapters [23](../by-chapter/ch23.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Start by rejecting accuracy as the metric, then apply class weights, tune the threshold from a cost matrix, and evaluate with precision-recall. Resampling is a later option, and any resampling requires recalibration before probabilities are used.

</details>

<a id="q98"></a>

**Q98.** Where should you set the decision threshold?

<sub>Chapters [23](../by-chapter/ch23.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

At the break-even point implied by the costs: false positive cost divided by the sum of false positive and false negative costs. Tune it on validation data, never on the test set.

</details>

<a id="q99"></a>

**Q99.** What are the drawbacks of SMOTE?

<sub>Chapters [23](../by-chapter/ch23.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It synthesizes examples by interpolation in regions no real process populates, blurs the boundary, and distorts calibration. Applying it before splitting also leaks information across folds.

</details>

<a id="q100"></a>

**Q100.** Your fraud model has 99.5% accuracy. Is it good?

<sub>Chapters [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Unknown until compared with the majority-class baseline, which is probably about 99.5% as well. Ask for precision, recall at the operating threshold, PR AUC, and the cost of each error type.

</details>

<a id="q101"></a>

**Q101.** Why is 88% accuracy a bad result at a 12% base rate?

<sub>Chapters [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Because predicting the majority class every time scores 88% while identifying nobody. Strong answers move immediately to precision, recall, and the confusion matrix, and ask what a flag is worth relative to a miss.

</details>

<a id="q102"></a>

**Q102.** What is AUC, in one sentence?

<sub>Chapters [22](../by-chapter/ch22.md) · [14](../by-chapter/ch14.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The probability that a randomly chosen positive case is scored above a randomly chosen negative one. Strong answers add that it summarizes ranking across all thresholds, is unaffected by class balance, and for that reason can look healthy on a rare-event problem where precision is poor.

</details>

<a id="q103"></a>

**Q103.** What does R-squared not tell you?

<sub>Chapters [13](../by-chapter/ch13.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Whether the model is correctly specified, whether it predicts new data, whether any relationship is causal, or whether the assumptions hold. Strong answers add that it never falls when predictors are added, which is why adjusted R-squared and out-of-sample scoring exist.

</details>

<a id="q104"></a>

**Q104.** A colleague reports test accuracy after a week of tuning against the test set. What is wrong with the number?

<sub>Chapters [16](../by-chapter/ch16.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Each look followed by a change fits the choices to that set, so the score drifts upward by an amount no one can measure; the number is now a validation score. Strong answers prescribe a validation set or cross-validation for every decision, describe a test set as spent once it has been used to choose, and ask for a fresh holdout if one can be had.

Related: [Q47](../by-topic/ml-fundamentals.md#q47)

*Revised: Reworded from a near-duplicate of Q47, which asks why a project keeps both a validation and a test set; this question applies the rule to a report.*

</details>

<a id="q105"></a>

**Q105.** How would you explain overfitting to a non-technical stakeholder?

<sub>Chapters [16](../by-chapter/ch16.md) · [17](../by-chapter/ch17.md) · [42](../by-chapter/ch42.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Memorizing the answers to last year's exam rather than learning the subject: perfect on the questions already seen, poor on new ones. Strong answers follow the analogy with the business consequence — the reported accuracy is not what will be achieved in production — and name the check that catches it.

</details>

<a id="q106"></a>

**Q106.** A forecasting model scored well on a random split and badly in production. Explain the gap.

<sub>Chapters [16](../by-chapter/ch16.md) · [28](../by-chapter/ch28.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A random split trains partly on the future, so the model interpolates between known neighbours rather than forecasting, and the score reflects a task no deployment faces. The fix is a chronological split at several successive cut points, which measures what forecasting actually achieves.

Related: [Q46](../by-topic/ml-fundamentals.md#q46)

*Revised: Reworded from a near-duplicate of Q46, which asks how to split time-series data; this question diagnoses the symptom.*

</details>

<a id="q107"></a>

**Q107.** Your backtest gives MAEs of 180, 195, 172, 188, and 910. What do you report?

<sub>Chapters [28](../by-chapter/ch28.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

The median or typical range, with the outlier named rather than averaged in — the mean of those is 329 and describes none of them. Strong answers ask what was happening in the fifth window before assuming the model is at fault.

</details>

<a id="q108"></a>

**Q108.** What is wrong with the feature importance a tree model gives you for free?

<sub>Chapters [29](../by-chapter/ch29.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It is computed on training data, so overfitted features look useful, and it favours features with many split points, so continuous variables are inflated and binary flags suppressed. Strong answers propose permutation importance on held-out data, reported with its spread across repeats.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
