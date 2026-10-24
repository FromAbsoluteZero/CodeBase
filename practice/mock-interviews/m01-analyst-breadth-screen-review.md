# M01 · Analyst breadth screen: review sheet

Read this only after you have sat the [mock interview](m01-analyst-breadth-screen.md).

## 1. Q6

How would you check a file before analysing it?

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md)</sub>

**What a strong answer contains.** Shape, dtypes, head, null counts, duplicate count, and the range of every key numeric column. Strong answers add a grain check — what one row means — and reconcile at least one total against a known figure, because a file that parses cleanly can still be the wrong extract.

## 2. Q7

What is the grain of a table, and why does it matter?

<sub>Chapters [4](../by-chapter/ch04.md) · [1](../by-chapter/ch01.md) · [5](../by-chapter/ch05.md) · [11](../by-chapter/ch11.md)</sub>

**What a strong answer contains.** The grain is what a single row represents — one order, one order line, one customer-month. Strong answers explain that joining tables of different grain silently fans out rows, and that every aggregate is wrong in a way no null check will catch.

## 3. Q9

Explain the difference between INNER, LEFT, and FULL OUTER JOIN.

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

**What a strong answer contains.** Inner keeps only matching rows; left keeps all left rows with nulls where no match exists; full outer keeps unmatched rows from both sides. Watch for row multiplication when the join key is not unique.

## 4. Q14

WHERE or HAVING — how do you decide?

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

**What a strong answer contains.** WHERE filters rows before grouping, HAVING filters groups after aggregation. Strong answers note that anything expressible in WHERE belongs there, because filtering before the aggregation is both correct and cheaper.

## 5. Q16

Why does WHERE x = NULL return nothing?

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

**What a strong answer contains.** NULL means unknown, and any comparison with an unknown is unknown rather than true, so no row qualifies. Strong answers give IS NULL as the fix and mention that the same logic makes NOT IN behave unexpectedly when the subquery contains a NULL.

## 6. Q33

When does the mean mislead, and what do you report instead?

<sub>Chapters [6](../by-chapter/ch06.md)</sub>

**What a strong answer contains.** Under skew or heavy tails, where a few extreme values pull it away from any typical case. Strong answers name the median plus a spread measure, and note that the mean is still correct for totals — revenue per customer times customers is a real number even when no customer is average.

## 7. Q32

A test returns p = 0.12. Your manager concludes the two options are identical. Respond.

<sub>Chapters [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** Absence of evidence is not evidence of absence. Strong answers ask what effect size the test could have detected: with a small sample, p = 0.12 is consistent with a large real difference. Report the confidence interval, which shows the range of effects still compatible with the data.

## 8. Q101

Why is 88% accuracy a bad result at a 12% base rate?

<sub>Chapters [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md)</sub>

**What a strong answer contains.** Because predicting the majority class every time scores 88% while identifying nobody. Strong answers move immediately to precision, recall, and the confusion matrix, and ask what a flag is worth relative to a miss.

## 9. Q174

Revenue is down 8%. How do you investigate?

<sub>Chapters [1](../by-chapter/ch01.md) · [12](../by-chapter/ch12.md)</sub>

**What a strong answer contains.** Decompose before theorizing: price against volume, new against returning, by segment, region, and channel, and check whether the comparison period is fair. Strong answers rule out measurement causes — a tracking change, a pipeline failure, a calendar effect — before reaching for commercial explanations.

## 10. Q173

A stakeholder wants a dashboard showing everything. What do you ask?

<sub>Chapters [42](../by-chapter/ch42.md)</sub>

**What a strong answer contains.** What decision it supports, who makes it, and how often. Strong answers explain that a dashboard showing everything gets read by nobody, and offer to build the three numbers that would change an action, with the rest available on request.

[Back to the mock interview](m01-analyst-breadth-screen.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
