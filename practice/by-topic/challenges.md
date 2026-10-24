# Multi-step challenges

Longer problems on the book's own datasets that combine several chapters, the way a take-home exercise or a case round does.

Track: Multi-step challenges · 8 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: intermediate 6, advanced 2. Types: coding 8.

Answer each question aloud before you open its note.

<a id="q220"></a>

**Q220.** Summarize a year of retail.csv the way a first analysis brief would: net revenue, the cost of cancellations, the best and worst months, the leading category and how much repeat business there is.

<sub>Chapters [1](../by-chapter/ch01.md) · [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) · [12](../by-chapter/ch12.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q220-a-year-of-retail-in-one-function](../exercises/challenges/q220-a-year-of-retail-in-one-function/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

One function returning a dictionary, built from the primitives of the earlier exercises: net revenue is a plain sum because cancellations are negative; the cancellation share is the cancelled revenue against gross; months and categories are groupbys; repeat business is the share of identified customers with more than one distinct invoice. Strong solutions state the grain before every aggregate and say which figures the missing customer IDs cannot support.

</details>

<a id="q221"></a>

**Q221.** Build a logistic-regression baseline for attrition in hr.csv with a proper split, and report what it beats.

<sub>Chapters [14](../by-chapter/ch14.md) · [16](../by-chapter/ch16.md) · [22](../by-chapter/ch22.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q221-an-honest-attrition-baseline](../exercises/challenges/q221-an-honest-attrition-baseline/) · data: `hr.csv`

<details>
<summary>What a strong answer contains</summary>

A stratified 80/20 split with a fixed random_state, a majority-class accuracy on the test set as the floor, and a Pipeline (one-hot for the two text columns, scaling for the numbers, LogisticRegression) fitted on the training rows only. Report accuracy and ROC AUC on the test rows. Strong solutions notice that accuracy barely beats the 88% floor because attrition is rare, and that AUC is the more honest number here.

</details>

<a id="q222"></a>

**Q222.** Train a fraud classifier on transactions.csv and pick the decision threshold that reaches a required recall, then report what it costs in precision.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q222-choosing-a-fraud-threshold](../exercises/challenges/q222-choosing-a-fraud-threshold/) · data: `transactions.csv`

<details>
<summary>What a strong answer contains</summary>

Stratified split, a scaled logistic regression with class_weight='balanced' because fraud is under half a percent of rows, then a search over thresholds on the test-set probabilities: the highest threshold whose recall is at least 0.80, and the precision at that point. The 0.5 default is reported beside it to show that the threshold is a business decision, not a constant (Q98). Strong solutions choose the threshold on a validation set rather than the test set in real work, and say so.

</details>

<a id="q223"></a>

**Q223.** Measure how much a leaky preprocessing step changes a cross-validated score on customers.csv, by running the same model with and without the leak.

<sub>Chapters [16](../by-chapter/ch16.md) · [24](../by-chapter/ch24.md) · [25](../by-chapter/ch25.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q223-leakage-in-preprocessing-measured](../exercises/challenges/q223-leakage-in-preprocessing-measured/) · data: `customers.csv`

<details>
<summary>What a strong answer contains</summary>

Two cross-validations of the same estimator on the same folds: one where imputation and scaling live inside a Pipeline, so each fold fits them on its own training rows, and one where they are fitted once on all the data before cross_val_score sees it. Strong solutions explain why the second is leakage even if the numbers barely move here (Q85), and why the honest version is the only one whose score predicts deployment.

</details>

<a id="q224"></a>

**Q224.** Hold out the last 90 days of daily revenue and measure three baselines any forecasting model has to beat: the training mean, the last value, and the seasonal naive.

<sub>Chapters [28](../by-chapter/ch28.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q224-forecast-baselines-that-must-be-beaten](../exercises/challenges/q224-forecast-baselines-that-must-be-beaten/) · data: `daily_revenue.csv`

<details>
<summary>What a strong answer contains</summary>

A chronological holdout, never a random one (Q46). The mean baseline predicts the training mean everywhere; the naive baseline repeats the last training day; the seasonal naive repeats the last training week in a cycle, because daily revenue has a weekly pattern. Report the MAE of each and which wins. Strong solutions say that a model which does not beat the seasonal naive has learned nothing the calendar did not already know.

</details>

<a id="q225"></a>

**Q225.** Cluster segments.csv with k-means and measure the result two ways: against the true segment labels and without them.

<sub>Chapters [26](../by-chapter/ch26.md) · [27](../by-chapter/ch27.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q225-do-the-clusters-mean-anything](../exercises/challenges/q225-do-the-clusters-mean-anything/) · data: `segments.csv`

<details>
<summary>What a strong answer contains</summary>

Standardize the four features first, because k-means measures Euclidean distance and the columns are on different scales; KMeans(n_clusters=4, n_init=10, random_state=0); then adjusted Rand index against TrueType, which is available only because the data is synthetic, and silhouette score, which is what you have in real work. Strong solutions say why the unclassifiable rows pull both numbers down and why silhouette alone cannot tell you the clusters are meaningful (Q112).

</details>

<a id="q226"></a>

**Q226.** Build an RFM table for the identified customers in retail.csv, score each dimension into quartiles, and count the top segment.

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) · [26](../by-chapter/ch26.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q226-recency-frequency-monetary](../exercises/challenges/q226-recency-frequency-monetary/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

One row per customer: recency as days from the last purchase to the day after the data ends, frequency as distinct invoices, monetary as net revenue; then quartile scores 1 to 4 with pd.qcut on a rank, because many customers tie on frequency and qcut on raw values would fail. Recency scores in reverse: the most recent buyers get 4. Strong solutions justify the reference date, exclude the rows without a CustomerID, and say that segment counts depend entirely on the cut rule.

</details>

<a id="q227"></a>

**Q227.** Compare attrition between employees who work overtime and those who do not, with a confidence interval and a p-value, and say what the numbers do and do not show.

<sub>Chapters [8](../by-chapter/ch08.md) · [15](../by-chapter/ch15.md) · [42](../by-chapter/ch42.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [challenges/q227-is-the-overtime-effect-real](../exercises/challenges/q227-is-the-overtime-effect-real/) · data: `hr.csv`

<details>
<summary>What a strong answer contains</summary>

Two proportions, their difference, a normal-approximation 95% interval for the difference, and a two-sided z-test with a pooled standard error. The interval is the useful output; the p-value only says the difference is unlikely to be zero. Strong solutions say plainly that this is observational: overtime and attrition can share a cause, so the interval is not the effect of overtime (Q36).

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
