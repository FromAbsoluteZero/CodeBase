# Mathematics and statistics

Heaviest for data science and applied science; lighter for engineering and product.

Track: Mathematics and statistics · 21 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 7, intermediate 13, advanced 1. Types: conceptual 18, scenario 3.

Answer each question aloud before you open its note.

<a id="q19"></a>

**Q19.** Explain broadcasting in NumPy.

<sub>Chapters [9](../by-chapter/ch09.md) · [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

NumPy aligns shapes from the trailing dimension backward; dimensions are compatible if equal or if one is 1, and size-1 dimensions are stretched. A strong answer gives an example of the silent (3,1) plus (1,3) producing (3,3), and notes that broadcasting avoids materializing large intermediate arrays.

</details>

<a id="q20"></a>

**Q20.** What is a dot product, geometrically?

<sub>Chapters [9](../by-chapter/ch09.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The product of the two vectors’ magnitudes times the cosine of the angle between them — a measure of alignment. Strong answers connect it to cosine similarity for embeddings and note that a zero dot product means orthogonality.

</details>

<a id="q21"></a>

**Q21.** What is the computational complexity of multiplying two n by n matrices?

<sub>Chapters [9](../by-chapter/ch09.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The naive algorithm is O(n^3). Candidates may mention Strassen’s algorithm and subsequent theoretical improvements, but the practical answer is that libraries use highly optimized blocked O(n^3) implementations.

</details>

<a id="q22"></a>

**Q22.** Why should you avoid explicitly inverting a matrix in code?

<sub>Chapters [9](../by-chapter/ch09.md) · [13](../by-chapter/ch13.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Inversion is slower and numerically unstable, particularly when the matrix is ill-conditioned. Solving the system directly with a factorization is both faster and more accurate; scikit-learn and NumPy solvers do this internally.

</details>

<a id="q23"></a>

**Q23.** What is a gradient, and why do we move against it?

<sub>Chapters [10](../by-chapter/ch10.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It is the vector of partial derivatives, pointing in the direction of steepest increase of the loss. Since the goal is to reduce loss, updates move in the negative gradient direction, scaled by the learning rate.

</details>

<a id="q24"></a>

**Q24.** State the chain rule and explain its role in neural networks.

<sub>Chapters [10](../by-chapter/ch10.md) · [30](../by-chapter/ch30.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The derivative of f(g(x)) is f’(g(x)) times g’(x). A network is a composition of layers, so the chain rule propagates the loss derivative backward through each layer; backpropagation is its systematic application with intermediate values cached.

</details>

<a id="q25"></a>

**Q25.** How would you check whether your gradient implementation is correct?

<sub>Chapters [10](../by-chapter/ch10.md) · [30](../by-chapter/ch30.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Compare against a numerical finite-difference estimate, preferably central difference with a step around 1e-5, and confirm agreement to within a small tolerance. Strong answers mention that too small a step introduces rounding error.

Related: [Q80](../by-topic/optimization-training.md#q80)

</details>

<a id="q26"></a>

**Q26.** What is the difference between a local minimum and a saddle point, and which matters more in deep learning?

<sub>Chapters [10](../by-chapter/ch10.md) · [18](../by-chapter/ch18.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Both have zero gradient; a saddle increases in some directions and decreases in others. In high dimensions saddles dominate, and much of modern optimizer design is about escaping them efficiently.

</details>

<a id="q27"></a>

**Q27.** Explain Bayes’ theorem and give a concrete example.

<sub>Chapters [7](../by-chapter/ch07.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Posterior equals likelihood times prior over evidence. The expected example is a rare-disease test where most positives are false because the prior is tiny; reasoning with hypothetical counts rather than percentages is the clearest presentation.

</details>

<a id="q28"></a>

**Q28.** What does a p-value actually mean?

<sub>Chapters [8](../by-chapter/ch08.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The probability of data at least as extreme as observed, assuming the null hypothesis is true. Strong answers explicitly reject the common misreading and note that a p-value says nothing about effect size or practical importance.

</details>

<a id="q29"></a>

**Q29.** What is maximum likelihood estimation, and how does it relate to loss functions?

<sub>Chapters [7](../by-chapter/ch07.md) · [14](../by-chapter/ch14.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Choose parameters maximizing the probability of the observed data. Taking the negative log-likelihood produces a loss; Gaussian noise yields squared error and a Bernoulli outcome yields cross-entropy, which is why those losses appear everywhere.

</details>

<a id="q30"></a>

**Q30.** Likelihood and probability sound interchangeable. What separates them?

<sub>Chapters [7](../by-chapter/ch07.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Probability fixes parameters and varies data; likelihood fixes data and varies parameters. The likelihood function is not a distribution over parameters and does not integrate to one.

</details>

<a id="q31"></a>

**Q31.** What does a 95% confidence interval mean?

<sub>Chapters [8](../by-chapter/ch08.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

That the procedure producing it captures the true value in 95% of repeated samples. Strong answers explicitly reject the common reading — it is not a 95% probability that this particular interval contains the parameter — and note the interval says nothing about practical importance.

</details>

<a id="q32"></a>

**Q32.** A test returns p = 0.12. Your manager concludes the two options are identical. Respond.

<sub>Chapters [8](../by-chapter/ch08.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Absence of evidence is not evidence of absence. Strong answers ask what effect size the test could have detected: with a small sample, p = 0.12 is consistent with a large real difference. Report the confidence interval, which shows the range of effects still compatible with the data.

</details>

<a id="q33"></a>

**Q33.** When does the mean mislead, and what do you report instead?

<sub>Chapters [6](../by-chapter/ch06.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Under skew or heavy tails, where a few extreme values pull it away from any typical case. Strong answers name the median plus a spread measure, and note that the mean is still correct for totals — revenue per customer times customers is a real number even when no customer is average.

</details>

<a id="q34"></a>

**Q34.** A test is 95% accurate for a condition affecting 1 in 500. Someone tests positive. What is the chance they have it?

<sub>Chapters [7](../by-chapter/ch07.md) · [14](../by-chapter/ch14.md) · [22](../by-chapter/ch22.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Around 3.7%, and the reasoning matters more than the figure. Strong answers work in counts: out of 100,000 people, 200 have it and about 190 test positive, while 99,800 do not and about 4,990 test positive anyway. False positives swamp true ones whenever the base rate is low.

</details>

<a id="q35"></a>

**Q35.** Why is the central limit theorem the reason inference works?

<sub>Chapters [7](../by-chapter/ch07.md) · [8](../by-chapter/ch08.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Because it makes the sampling distribution of the mean approximately normal regardless of the population's shape, given enough observations, which is what licenses standard errors and confidence intervals on data that is not itself normal. Strong answers note it applies to the statistic, not the data, and that heavy tails slow the convergence.

</details>

<a id="q36"></a>

**Q36.** What is the difference between correlation and causation, in practice?

<sub>Chapters [15](../by-chapter/ch15.md) · [13](../by-chapter/ch13.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Correlation is a measurable property of data; causation is a claim about what would happen under intervention. Strong answers name the practical routes to the second — randomization, or a design exploiting quasi-random variation — and note that controlling for observed confounders does not establish it.

</details>

<a id="q37"></a>

**Q37.** You test 15 segments and two come back significant. What do you conclude?

<sub>Chapters [8](../by-chapter/ch08.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Probably nothing. At a 5% threshold, testing 15 independent segments gives a greater than 50% chance of at least one false positive. Strong answers name a correction, or better, propose treating the finding as a hypothesis to be confirmed on fresh data.

</details>

<a id="q38"></a>

**Q38.** How do you determine the sample size for an A/B test?

<sub>Chapters [15](../by-chapter/ch15.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

From the minimum effect worth detecting, the baseline rate, the tolerance for false positives and false negatives, and the variance. Strong answers stress that the effect size is a business decision made before the test, and that computing it afterward to justify a result is meaningless.

</details>

<a id="q39"></a>

**Q39.** Why is checking test results daily a problem?

<sub>Chapters [15](../by-chapter/ch15.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Because stopping the moment the result crosses significance inflates the false positive rate far above the nominal level — a random walk crosses any boundary eventually. Strong answers name a fixed horizon set in advance, or a sequential method designed to permit peeking.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
