# M05 · Machine learning depth: derivations and training: review sheet

Read this only after you have sat the [mock interview](m05-machine-learning-depth.md).

## 1. Q52

Derive the closed-form solution for ordinary least squares.

<sub>Chapters [13](../by-chapter/ch13.md) · [10](../by-chapter/ch10.md) · [9](../by-chapter/ch09.md)</sub>

**What a strong answer contains.** Write the loss in matrix form, differentiate with respect to w to get minus two X-transpose times (y minus Xw), set to zero, and solve to reach w equals (X-transpose-X) inverse times X-transpose-y. Strong candidates add that in practice you solve rather than invert.

## 2. Q57

Derive the gradient of the logistic loss.

<sub>Chapters [14](../by-chapter/ch14.md)</sub>

**What a strong answer contains.** Differentiating the cross-entropy with respect to w yields X-transpose times (sigma(Xw) minus y), divided by n. Strong candidates note it has the same form as linear regression’s gradient.

## 3. Q65

Why does bagging reduce variance?

<sub>Chapters [20](../by-chapter/ch20.md)</sub>

**What a strong answer contains.** Averaging B models with pairwise correlation rho leaves rho times the variance plus the remainder divided by B. Only decorrelated error shrinks, which is why random forests also subsample features at each split.

## 4. Q73

Write out the Adam update equations.

<sub>Chapters [18](../by-chapter/ch18.md)</sub>

**What a strong answer contains.** Exponentially weighted first and second moments of the gradient, bias-corrected by dividing by one minus beta to the power t, then a step of the learning rate times corrected first moment over the square root of corrected second moment plus epsilon.

## 5. Q77

Explain backpropagation.

<sub>Chapters [30](../by-chapter/ch30.md)</sub>

**What a strong answer contains.** It applies the chain rule backward from the loss, reusing cached forward activations, to obtain the gradient of the loss with respect to every parameter. Each layer receives an incoming error signal, produces its weight gradient, and passes a transformed signal further back.

## 6. Q80

Your gradient check agrees to five decimal places, but the network still does not learn. What did the check prove, and what did it not?

<sub>Chapters [30](../by-chapter/ch30.md) · [10](../by-chapter/ch10.md)</sub>

**What a strong answer contains.** It proved that the backward pass computes the derivative of the loss you wrote, at the points you checked. It did not prove that the loss is the right one, that inputs and labels are aligned, that initialization and learning rate let training move, or that every layer was covered by the check. Strong answers go on to the training-failure checklist: a tiny subset the model should overfit, the loss at initialization, and the size of the updates.

## 7. Q84

Your deep network’s loss does not move at all. What do you check, in order?

<sub>Chapters [31](../by-chapter/ch31.md)</sub>

**What a strong answer contains.** Learning rate, then activation and gradient statistics per layer to find where the signal dies, then initialization scale, then whether the data and labels are correctly aligned, and finally whether the loss and output layer are matched to the task.

## 8. Q90

What is nested cross-validation and why use it?

<sub>Chapters [25](../by-chapter/ch25.md)</sub>

**What a strong answer contains.** An inner loop selects hyperparameters and an outer loop evaluates the entire selection procedure on folds never used for selection. It removes the optimistic bias of reporting the best inner score.

## 9. Q126

Why divide by the square root of the key dimension?

<sub>Chapters [34](../by-chapter/ch34.md)</sub>

**What a strong answer contains.** Dot products of high-dimensional vectors have variance proportional to the dimension, so unscaled scores grow large and saturate the softmax, driving gradients toward zero. The scaling keeps scores near unit variance.

[Back to the mock interview](m05-machine-learning-depth.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
