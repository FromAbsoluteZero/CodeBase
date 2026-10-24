# Optimization and training

Expected for research and deep learning roles; increasingly asked of anyone who trains models.

Track: Deep learning · 12 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 2, intermediate 7, advanced 3. Types: conceptual 10, scenario 2.

Answer each question aloud before you open its note.

<a id="q73"></a>

**Q73.** Write out the Adam update equations.

<sub>Chapters [18](../by-chapter/ch18.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Exponentially weighted first and second moments of the gradient, bias-corrected by dividing by one minus beta to the power t, then a step of the learning rate times corrected first moment over the square root of corrected second moment plus epsilon.

</details>

<a id="q74"></a>

**Q74.** Compare batch, stochastic, and mini-batch gradient descent.

<sub>Chapters [18](../by-chapter/ch18.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

They differ in examples per gradient estimate: the whole set, one example, or a small batch. Mini-batch dominates because it uses vectorized hardware efficiently while keeping useful gradient noise.

</details>

<a id="q75"></a>

**Q75.** What does momentum do, and why does it help?

<sub>Chapters [18](../by-chapter/ch18.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It accumulates a decaying average of past gradients, so consistent directions build velocity and oscillating ones cancel. This is especially valuable in ill-conditioned valleys where plain descent zig-zags.

</details>

<a id="q76"></a>

**Q76.** Your training loss becomes not-a-number after a few steps. What do you check?

<sub>Chapters [18](../by-chapter/ch18.md) · [31](../by-chapter/ch31.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Learning rate too high is the first suspect; then exploding gradients, unnormalized inputs, a logarithm of zero in the loss, or division by a near-zero denominator. Remedies include lowering the rate, clipping gradients, and adding epsilon guards.

</details>

<a id="q77"></a>

**Q77.** Explain backpropagation.

<sub>Chapters [30](../by-chapter/ch30.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It applies the chain rule backward from the loss, reusing cached forward activations, to obtain the gradient of the loss with respect to every parameter. Each layer receives an incoming error signal, produces its weight gradient, and passes a transformed signal further back.

</details>

<a id="q78"></a>

**Q78.** Why do neural networks need nonlinear activation functions?

<sub>Chapters [30](../by-chapter/ch30.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Because a composition of affine transformations is itself affine, so without nonlinearity any depth of network collapses to a single linear layer and gains no representational power.

</details>

<a id="q79"></a>

**Q79.** What is the vanishing gradient problem?

<sub>Chapters [31](../by-chapter/ch31.md) · [33](../by-chapter/ch33.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

When derivatives smaller than one multiply across many layers, the gradient reaching early layers becomes negligible and those layers stop learning. Saturating activations such as sigmoid cause it; ReLU, residual connections, and normalization mitigate it.

</details>

<a id="q80"></a>

**Q80.** Your gradient check agrees to five decimal places, but the network still does not learn. What did the check prove, and what did it not?

<sub>Chapters [30](../by-chapter/ch30.md) · [10](../by-chapter/ch10.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It proved that the backward pass computes the derivative of the loss you wrote, at the points you checked. It did not prove that the loss is the right one, that inputs and labels are aligned, that initialization and learning rate let training move, or that every layer was covered by the check. Strong answers go on to the training-failure checklist: a tiny subset the model should overfit, the loss at initialization, and the size of the updates.

Related: [Q25](../by-topic/maths-statistics.md#q25)

*Revised: Reworded from a near-duplicate of Q25, which asks how to run a gradient check; this question asks what a passing check does and does not establish.*

</details>

<a id="q81"></a>

**Q81.** What does batch normalization do, and how does it behave at inference?

<sub>Chapters [31](../by-chapter/ch31.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It standardizes each feature over the mini-batch, then applies a learned scale and shift. At inference it uses running averages collected during training, since no batch statistics exist. The commonly cited covariate-shift explanation is disputed.

</details>

<a id="q82"></a>

**Q82.** Why does dropout behave differently at training and test time?

<sub>Chapters [17](../by-chapter/ch17.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** Chapter 17 names dropout as a regularizer but leaves its mechanism to the further reading in Chapter 45.

<details>
<summary>What a strong answer contains</summary>

It randomly zeroes units only during training. Inverted dropout divides surviving activations by the keep probability so expectations match, letting inference run the full network unchanged. Chapter 17 names dropout as a regularizer this book leaves to the reading in Chapter 45.

</details>

<a id="q83"></a>

**Q83.** What is the dying ReLU problem and how is it addressed?

<sub>Chapters [31](../by-chapter/ch31.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** The dying ReLU problem, Leaky ReLU and GELU are not covered in this book. Chapter 31 covers the training failures they belong to.

<details>
<summary>What a strong answer contains</summary>

A unit driven permanently negative outputs zero and receives zero gradient, so it never recovers. Leaky ReLU, GELU, better initialization, and lower learning rates all reduce the risk.

</details>

<a id="q84"></a>

**Q84.** Your deep network’s loss does not move at all. What do you check, in order?

<sub>Chapters [31](../by-chapter/ch31.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Learning rate, then activation and gradient statistics per layer to find where the signal dies, then initialization scale, then whether the data and labels are correctly aligned, and finally whether the loss and output layer are matched to the task.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
