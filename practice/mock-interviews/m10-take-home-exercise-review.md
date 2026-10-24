# M10 · Take-home exercise: review sheet

Read this only after you have sat the [mock interview](m10-take-home-exercise.md).

## 1. Q220

Summarize a year of retail.csv the way a first analysis brief would: net revenue, the cost of cancellations, the best and worst months, the leading category and how much repeat business there is.

<sub>Chapters [1](../by-chapter/ch01.md) · [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) · [12](../by-chapter/ch12.md)</sub>

Check your code: `python practice/exercises/challenges/q220-a-year-of-retail-in-one-function/check.py`

**What a strong answer contains.** One function returning a dictionary, built from the primitives of the earlier exercises: net revenue is a plain sum because cancellations are negative; the cancellation share is the cancelled revenue against gross; months and categories are groupbys; repeat business is the share of identified customers with more than one distinct invoice. Strong solutions state the grain before every aggregate and say which figures the missing customer IDs cannot support.

## 2. Q224

Hold out the last 90 days of daily revenue and measure three baselines any forecasting model has to beat: the training mean, the last value, and the seasonal naive.

<sub>Chapters [28](../by-chapter/ch28.md)</sub>

Check your code: `python practice/exercises/challenges/q224-forecast-baselines-that-must-be-beaten/check.py`

**What a strong answer contains.** A chronological holdout, never a random one (Q46). The mean baseline predicts the training mean everywhere; the naive baseline repeats the last training day; the seasonal naive repeats the last training week in a cycle, because daily revenue has a weekly pattern. Report the MAE of each and which wins. Strong solutions say that a model which does not beat the seasonal naive has learned nothing the calendar did not already know.

## 3. Q227

Compare attrition between employees who work overtime and those who do not, with a confidence interval and a p-value, and say what the numbers do and do not show.

<sub>Chapters [8](../by-chapter/ch08.md) · [15](../by-chapter/ch15.md) · [42](../by-chapter/ch42.md)</sub>

Check your code: `python practice/exercises/challenges/q227-is-the-overtime-effect-real/check.py`

**What a strong answer contains.** Two proportions, their difference, a normal-approximation 95% interval for the difference, and a two-sided z-test with a pooled standard error. The interval is the useful output; the p-value only says the difference is unlikely to be zero. Strong solutions say plainly that this is observational: overtime and attrition can share a cause, so the interval is not the effect of overtime (Q36).

## 4. Q222

Train a fraud classifier on transactions.csv and pick the decision threshold that reaches a required recall, then report what it costs in precision.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md)</sub>

Check your code: `python practice/exercises/challenges/q222-choosing-a-fraud-threshold/check.py`

**What a strong answer contains.** Stratified split, a scaled logistic regression with class_weight='balanced' because fraud is under half a percent of rows, then a search over thresholds on the test-set probabilities: the highest threshold whose recall is at least 0.80, and the precision at that point. The 0.5 default is reported beside it to show that the threshold is a business decision, not a constant (Q98). Strong solutions choose the threshold on a validation set rather than the test set in real work, and say so.

[Back to the mock interview](m10-take-home-exercise.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
