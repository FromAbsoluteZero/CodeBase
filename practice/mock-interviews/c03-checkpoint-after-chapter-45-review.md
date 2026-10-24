# C03 · Checkpoint: after Chapter 45: review sheet

Read this only after you have sat the [mock interview](c03-checkpoint-after-chapter-45.md).

## 1. Q78

Why do neural networks need nonlinear activation functions?

<sub>Chapters [30](../by-chapter/ch30.md)</sub>

**What a strong answer contains.** Because a composition of affine transformations is itself affine, so without nonlinearity any depth of network collapses to a single linear layer and gains no representational power.

## 2. Q79

What is the vanishing gradient problem?

<sub>Chapters [31](../by-chapter/ch31.md) · [33](../by-chapter/ch33.md)</sub>

**What a strong answer contains.** When derivatives smaller than one multiply across many layers, the gradient reaching early layers becomes negligible and those layers stop learning. Saturating activations such as sigmoid cause it; ReLU, residual connections, and normalization mitigate it.

## 3. Q117

Why use convolutions instead of dense layers for images?

<sub>Chapters [32](../by-chapter/ch32.md)</sub>

**What a strong answer contains.** Local connectivity matches the spatial structure of images and weight sharing reuses each filter across all positions, which cuts parameters enormously and provides translation equivariance.

## 4. Q125

Write the scaled dot-product attention formula and explain each term.

<sub>Chapters [34](../by-chapter/ch34.md)</sub>

**What a strong answer contains.** Softmax of Q times K transposed divided by the square root of d_k, all times V. Queries ask, keys advertise, values carry content; the softmax produces weights summing to one, and the output is a weighted average of values.

## 5. Q129

What is the difference between feature extraction and fine-tuning?

<sub>Chapters [35](../by-chapter/ch35.md) · [39](../by-chapter/ch39.md)</sub>

**What a strong answer contains.** Feature extraction freezes the pretrained weights and trains only a new head, suiting small datasets. Fine-tuning updates all weights at a small learning rate, reaching higher performance with more data but risking catastrophic forgetting.

## 6. Q135

What is byte pair encoding and why do models use subword tokens?

<sub>Chapters [36](../by-chapter/ch36.md)</sub>

**What a strong answer contains.** An algorithm that builds a vocabulary by repeatedly merging the most frequent adjacent pairs. Subwords balance vocabulary size against sequence length and handle unseen words gracefully by decomposing them.

## 7. Q140

How do you reduce hallucination in a generative system?

<sub>Chapters [38](../by-chapter/ch38.md) · [40](../by-chapter/ch40.md)</sub>

**What a strong answer contains.** Ground answers in retrieved sources, require citations, instruct abstention when context is insufficient, constrain output format, and evaluate against a fixed set with human review. No single measure eliminates it.

## 8. Q146

How do you measure hallucination in a RAG system?

<sub>Chapters [38](../by-chapter/ch38.md) · [40](../by-chapter/ch40.md)</sub>

**What a strong answer contains.** Check groundedness — the fraction of claims supported by retrieved context — with claim-level annotation or a calibrated judge, and separately measure retrieval recall, since ungrounded answers often begin as retrieval failures.

## 9. Q153

How do you detect that a deployed model is degrading?

<sub>Chapters [43](../by-chapter/ch43.md)</sub>

**What a strong answer contains.** Monitor leading indicators continuously — input and prediction distributions, stability indices such as PSI, and business metrics — because labels arrive late. Confirm with measured performance once labels mature.

## 10. Q159

A model does not use race as a feature. Can it still be discriminatory?

<sub>Chapters [44](../by-chapter/ch44.md)</sub>

**What a strong answer contains.** Yes. Correlated features such as geography or purchase history act as proxies, so disparate outcomes persist. Fairness must be measured on outcomes, not inferred from the feature list.

## 11. Q161

A model declines someone's application. What do you owe them, and which method provides it?

<sub>Chapters [29](../by-chapter/ch29.md) · [44](../by-chapter/ch44.md)</sub>

**What a strong answer contains.** A local explanation, not a global one: SHAP decomposes their individual prediction into per-feature contributions summing exactly to their score. Strong answers stress that this explains the model rather than the world, and that presenting a SHAP value as a cause is a mistake with a polished appearance.

[Back to the mock interview](c03-checkpoint-after-chapter-45.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
