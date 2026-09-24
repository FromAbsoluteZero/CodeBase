# C01 · Checkpoint: after Chapter 15: review sheet

Read this only after you have sat the [mock interview](c01-checkpoint-after-chapter-15.md).

## 1. Q3

Explain .loc versus .iloc.

<sub>Chapters [4](../by-chapter/ch04.md)</sub>

**What a strong answer contains.** .loc selects by label, .iloc by integer position. Strong answers note that they coincide on a default RangeIndex, which is exactly why the confusion survives until an index is filtered or sorted and the two silently diverge.

## 2. Q7

What is the grain of a table, and why does it matter?

<sub>Chapters [4](../by-chapter/ch04.md) · [1](../by-chapter/ch01.md) · [5](../by-chapter/ch05.md) · [11](../by-chapter/ch11.md)</sub>

**What a strong answer contains.** The grain is what a single row represents — one order, one order line, one customer-month. Strong answers explain that joining tables of different grain silently fans out rows, and that every aggregate is wrong in a way no null check will catch.

## 3. Q10

What is a window function, and when would you use one instead of GROUP BY?

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

**What a strong answer contains.** It computes across a set of rows while preserving row-level detail. Use it for running totals, rankings, and period-over-period comparisons where collapsing rows would lose the information you need.

## 4. Q15

Why can you not filter on a column alias in WHERE?

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

**What a strong answer contains.** WHERE is evaluated before SELECT, so the alias does not yet exist. Strong answers give the logical order of evaluation — FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY — and note that ORDER BY can use the alias precisely because it runs last.

## 5. Q27

Explain Bayes’ theorem and give a concrete example.

<sub>Chapters [7](../by-chapter/ch07.md)</sub>

**What a strong answer contains.** Posterior equals likelihood times prior over evidence. The expected example is a rare-disease test where most positives are false because the prior is tiny; reasoning with hypothetical counts rather than percentages is the clearest presentation.

## 6. Q28

What does a p-value actually mean?

<sub>Chapters [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** The probability of data at least as extreme as observed, assuming the null hypothesis is true. Strong answers explicitly reject the common misreading and note that a p-value says nothing about effect size or practical importance.

## 7. Q33

When does the mean mislead, and what do you report instead?

<sub>Chapters [6](../by-chapter/ch06.md)</sub>

**What a strong answer contains.** Under skew or heavy tails, where a few extreme values pull it away from any typical case. Strong answers name the median plus a spread measure, and note that the mean is still correct for totals — revenue per customer times customers is a real number even when no customer is average.

## 8. Q36

What is the difference between correlation and causation, in practice?

<sub>Chapters [15](../by-chapter/ch15.md) · [13](../by-chapter/ch13.md)</sub>

**What a strong answer contains.** Correlation is a measurable property of data; causation is a claim about what would happen under intervention. Strong answers name the practical routes to the second — randomization, or a design exploiting quasi-random variation — and note that controlling for observed confounders does not establish it.

## 9. Q38

How do you determine the sample size for an A/B test?

<sub>Chapters [15](../by-chapter/ch15.md)</sub>

**What a strong answer contains.** From the minimum effect worth detecting, the baseline rate, the tolerance for false positives and false negatives, and the variance. Strong answers stress that the effect size is a business decision made before the test, and that computing it afterward to justify a result is meaningless.

## 10. Q174

Revenue is down 8%. How do you investigate?

<sub>Chapters [1](../by-chapter/ch01.md) · [12](../by-chapter/ch12.md)</sub>

**What a strong answer contains.** Decompose before theorizing: price against volume, new against returning, by segment, region, and channel, and check whether the comparison period is fair. Strong answers rule out measurement causes — a tracking change, a pipeline failure, a calendar effect — before reaching for commercial explanations.

[Back to the mock interview](c01-checkpoint-after-chapter-15.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
