# Statistics and modelling

One-line definitions that interviewers and reviewers expect you to have straight. Each names the chapter
that earns the line.

| Term | The line | Chapter |
|---|---|---|
| Mean vs median | The mean follows the tail; the median does not. When they diverge, say which you are reporting | 6 |
| Standard deviation | Spread in the units of the data. Variance is its square | 6 |
| Z-score | `(x − mean) / sd` — how many standard deviations from the centre | 6 |
| IQR | `Q3 − Q1`. Robust to outliers in a way the standard deviation is not | 6 |
| Correlation | Linear association only, between −1 and 1. Not causation, and not slope | 6, 15 |
| p-value | P(data at least this extreme \| null true). **Not** the probability the hypothesis is true | 8 |
| Confidence interval | The range of population values consistent with what you observed | 8 |
| Statistical vs practical | A tiny effect can be significant with enough data. Ask if it changes the decision | 8, 15 |
| Multiple comparisons | Test fifteen things at 0.05 and expect one false positive; state how many you tested | 8 |
| Regression coefficient | Associated with, not causes — unless the design supports the stronger word | 13, 15 |
| Log-odds | Logistic regression is linear in log-odds, not in probability | 14 |
| Baseline | The simplest thing that answers the question; a model that does not beat it has learned nothing | 1, 16 |
| Leakage | Any information at fit time that will not exist at prediction time. Fit every preprocessing step inside the split | 16, 24 |
| Validation vs test | Validation guides decisions and can be consulted repeatedly; the test set is spent once | 16 |
| Bias vs variance | Underfit vs overfit. Regularization trades one for the other | 17 |
| Accuracy | Meaningless under class imbalance. Use precision, recall or a cost-weighted metric | 22 |
| Precision vs recall | Precision: of those flagged, how many were right. Recall: of those real, how many were caught | 22 |
| ROC-AUC vs PR-AUC | Prefer precision-recall when positives are rare | 22 |
| Calibration | Whether a predicted 0.7 happens 70% of the time. Separate from ranking | 22 |
| Threshold | A business decision, not a default. 0.5 is rarely the right answer | 23 |
| Drift | Data drift changes the inputs; concept drift changes what the inputs mean. Monitor both | 43 |

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
