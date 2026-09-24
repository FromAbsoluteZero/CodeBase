# M03 · Statistics and experimentation: review sheet

Read this only after you have sat the [mock interview](m03-statistics-and-experimentation.md).

## 1. Q28

What does a p-value actually mean?

<sub>Chapters [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** The probability of data at least as extreme as observed, assuming the null hypothesis is true. Strong answers explicitly reject the common misreading and note that a p-value says nothing about effect size or practical importance.

## 2. Q31

What does a 95% confidence interval mean?

<sub>Chapters [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** That the procedure producing it captures the true value in 95% of repeated samples. Strong answers explicitly reject the common reading — it is not a 95% probability that this particular interval contains the parameter — and note the interval says nothing about practical importance.

## 3. Q34

A test is 95% accurate for a condition affecting 1 in 500. Someone tests positive. What is the chance they have it?

<sub>Chapters [7](../by-chapter/ch07.md) · [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md)</sub>

**What a strong answer contains.** Around 3.7%, and the reasoning matters more than the figure. Strong answers work in counts: out of 100,000 people, 200 have it and about 190 test positive, while 99,800 do not and about 4,990 test positive anyway. False positives swamp true ones whenever the base rate is low.

## 4. Q35

Why is the central limit theorem the reason inference works?

<sub>Chapters [7](../by-chapter/ch07.md) · [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** Because it makes the sampling distribution of the mean approximately normal regardless of the population's shape, given enough observations, which is what licenses standard errors and confidence intervals on data that is not itself normal. Strong answers note it applies to the statistic, not the data, and that heavy tails slow the convergence.

## 5. Q37

You test 15 segments and two come back significant. What do you conclude?

<sub>Chapters [8](../by-chapter/ch08.md)</sub>

**What a strong answer contains.** Probably nothing. At a 5% threshold, testing 15 independent segments gives a greater than 50% chance of at least one false positive. Strong answers name a correction, or better, propose treating the finding as a hypothesis to be confirmed on fresh data.

## 6. Q38

How do you determine the sample size for an A/B test?

<sub>Chapters [15](../by-chapter/ch15.md)</sub>

**What a strong answer contains.** From the minimum effect worth detecting, the baseline rate, the tolerance for false positives and false negatives, and the variance. Strong answers stress that the effect size is a business decision made before the test, and that computing it afterward to justify a result is meaningless.

## 7. Q39

Why is checking test results daily a problem?

<sub>Chapters [15](../by-chapter/ch15.md)</sub>

**What a strong answer contains.** Because stopping the moment the result crosses significance inflates the false positive rate far above the nominal level — a random walk crosses any boundary eventually. Strong answers name a fixed horizon set in advance, or a sequential method designed to permit peeking.

## 8. Q177

A model would improve conversion by 0.02 percentage points, significantly. Ship it?

<sub>Chapters [8](../by-chapter/ch08.md) · [15](../by-chapter/ch15.md)</sub>

**What a strong answer contains.** Significance is not importance. Strong answers multiply the effect by the volume to get an absolute value, weigh it against build and maintenance cost and the risk of another system to monitor, and note that a very large sample makes trivial effects detectable.

## 9. Q36

What is the difference between correlation and causation, in practice?

<sub>Chapters [15](../by-chapter/ch15.md) · [13](../by-chapter/ch13.md)</sub>

**What a strong answer contains.** Correlation is a measurable property of data; causation is a claim about what would happen under intervention. Strong answers name the practical routes to the second — randomization, or a design exploiting quasi-random variation — and note that controlling for observed confounders does not establish it.

## 10. Q107

Your backtest gives MAEs of 180, 195, 172, 188, and 910. What do you report?

<sub>Chapters [28](../by-chapter/ch28.md)</sub>

**What a strong answer contains.** The median or typical range, with the outlier named rather than averaged in — the mean of those is 329 and describes none of them. Strong answers ask what was happening in the fifth window before assuming the model is at fault.

[Back to the mock interview](m03-statistics-and-experimentation.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
