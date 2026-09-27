# Deep learning and architectures

Core for machine learning engineering and research; skimmed for analytics roles.

Track: Deep learning · 16 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 3, intermediate 12, advanced 1. Types: conceptual 15, scenario 1.

Answer each question aloud before you open its note.

<a id="q117"></a>

**Q117.** Why use convolutions instead of dense layers for images?

<sub>Chapters [32](../by-chapter/ch32.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Local connectivity matches the spatial structure of images and weight sharing reuses each filter across all positions, which cuts parameters enormously and provides translation equivariance.

</details>

<a id="q118"></a>

**Q118.** What problem do residual connections solve?

<sub>Chapters [34](../by-chapter/ch34.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The degradation problem: very deep plain networks trained worse than shallower ones. The identity shortcut carries gradients backward unimpeded and makes the identity mapping easy to represent, so depth stops hurting.

</details>

<a id="q119"></a>

**Q119.** Compute the output size of a convolution.

<sub>Chapters [32](../by-chapter/ch32.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Floor of input size minus filter size plus twice padding, divided by stride, plus one. Candidates should also give the parameter count as filter area times input channels times filter count plus biases.

</details>

<a id="q120"></a>

**Q120.** What is a receptive field and why does it grow with depth?

<sub>Chapters [32](../by-chapter/ch32.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

> **Beyond the book.** The term receptive field is not used in this book. Chapter 32 covers the mechanism: stacked small filters that see a wider region with depth.

<details>
<summary>What a strong answer contains</summary>

The region of the input that influences one unit’s activation. Each layer aggregates neighboring outputs of the previous layer, so the region expands with depth, which is why stacked small filters can see broadly.

</details>

<a id="q121"></a>

**Q121.** Why do recurrent networks struggle with long sequences?

<sub>Chapters [33](../by-chapter/ch33.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Backpropagation through time multiplies one factor per step, the table of derivatives linking one hidden state to the next, so gradients decay or explode exponentially with distance. Exploding is fixable by clipping; vanishing silently prevents long-range learning.

</details>

<a id="q122"></a>

**Q122.** What did attention add to sequence-to-sequence models?

<sub>Chapters [33](../by-chapter/ch33.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It removed the fixed-size context bottleneck by letting the decoder compute a weighted average over all encoder states, with weights learned per output position, so long inputs no longer had to compress into one vector.

</details>

<a id="q123"></a>

**Q123.** Why did attention replace recurrence rather than complement it?

<sub>Chapters [33](../by-chapter/ch33.md) · [34](../by-chapter/ch34.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Attention is parallelizable across the sequence and gives every position a direct path to every other, while recurrence is inherently sequential and attenuates long-range signal. At scale the hardware efficiency was decisive.

</details>

<a id="q124"></a>

**Q124.** How does an LSTM mitigate vanishing gradients?

<sub>Chapters [33](../by-chapter/ch33.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Its cell state is updated additively and regulated by gates, so gradients flow along that path without being repeatedly multiplied by a weight matrix. It reduces attenuation rather than removing it.

</details>

<a id="q125"></a>

**Q125.** Write the scaled dot-product attention formula and explain each term.

<sub>Chapters [34](../by-chapter/ch34.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Softmax of Q times K transposed divided by the square root of d_k, all times V. Queries ask, keys advertise, values carry content; the softmax produces weights summing to one, and the output is a weighted average of values.

</details>

<a id="q126"></a>

**Q126.** Why divide by the square root of the key dimension?

<sub>Chapters [34](../by-chapter/ch34.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Dot products of high-dimensional vectors have variance proportional to the dimension, so unscaled scores grow large and saturate the softmax, driving gradients toward zero. The scaling keeps scores near unit variance.

</details>

<a id="q127"></a>

**Q127.** How does a transformer know the order of tokens?

<sub>Chapters [34](../by-chapter/ch34.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It does not inherently: self-attention is permutation-equivariant, so shuffling the input just shuffles the outputs in the same way. Position must be injected explicitly, through sinusoidal, learned, or rotary positional encodings.

</details>

<a id="q128"></a>

**Q128.** What is the computational complexity of self-attention and why does it matter?

<sub>Chapters [34](../by-chapter/ch34.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Quadratic in sequence length for both time and memory, because all pairs of positions are scored. It is the binding constraint on context length and the motivation for efficient attention variants.

</details>

<a id="q129"></a>

**Q129.** What is the difference between feature extraction and fine-tuning?

<sub>Chapters [35](../by-chapter/ch35.md) · [39](../by-chapter/ch39.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Feature extraction freezes the pretrained weights and trains only a new head, suiting small datasets. Fine-tuning updates all weights at a small learning rate, reaching higher performance with more data but risking catastrophic forgetting.

</details>

<a id="q130"></a>

**Q130.** What is an embedding, and why use cosine similarity?

<sub>Chapters [35](../by-chapter/ch35.md) · [9](../by-chapter/ch09.md) · [38](../by-chapter/ch38.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A dense vector representation where semantically similar items lie close together. Cosine ignores magnitude, which varies for reasons unrelated to meaning such as document length, and compares direction alone.

</details>

<a id="q131"></a>

**Q131.** What is catastrophic forgetting and how do you reduce it?

<sub>Chapters [35](../by-chapter/ch35.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Loss of previously learned capability when adapting to a narrow new task. Mitigations include small learning rates, fewer epochs, mixing in general data, freezing early layers, and parameter-efficient tuning such as LoRA.

</details>

<a id="q132"></a>

**Q132.** When would you not fine-tune at all?

<sub>Chapters [35](../by-chapter/ch35.md) · [39](../by-chapter/ch39.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

When off-the-shelf embeddings with a simple classifier, or a well-designed prompt, already meet the requirement. Establishing that baseline first avoids substantial cost and complexity for no measured gain.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
