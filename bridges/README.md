# Framework bridges

Six notebooks, one for each chapter from 30 to 35. Each one takes **that chapter's own code, its
own weights and its own data**, hands them to PyTorch, and compares the chapter's hand-derived
gradients against autograd.

Nothing here is reimplemented. Each notebook executes the chapter's files directly, so what is
checked is the code you run, not a second copy of it.

These notebooks are optional. Everything in the book, in the 34 chapter directories and in the 28
chapter notebooks runs in pure NumPy; PyTorch is needed only here.

## Checks and measurements

Two kinds of number appear, and they are counted separately.

An **asserted check** compares a hand-derived quantity against autograd, and the notebook fails if
the two disagree beyond the stated tolerance.

A **reported measurement** is a number the notebook prints without asserting, because there is no
single right answer to assert against — the size of a deliberate approximation, or a tie-breaking
convention where two answers are equally defensible.

| Notebook | Chapter | Asserted checks | Reported measurements |
|---|---|---|---|
| `ch30_bridge.ipynb` | 30 | forward loss, `dW1 db1 dW2 db2`, and the ReLU subgradient at exactly zero — 6 | — |
| `ch31_bridge.ipynb` | 31 | one step of the chapter's own `train()`: the five layers' `W` and `b` after the update — 10 | how far the chapter's deliberately partial batch-norm backward sits from the full one, along a random direction — 1 |
| `ch32_bridge.ipynb` | 32 | convolution forward and backward, max pooling forward, and pooling backward on windows with a unique maximum — 4 | the share of tied windows, and the gradient on them — 2 |
| `ch33_bridge.ipynb` | 33 | backpropagation through time (`dWx dWh dbh`), and one step of the chapter's own `train_recall_attention()`: all six parameters after the update — 9 | — |
| `ch34_bridge.ipynb` | 34 | self-attention forward, `dWq dWk dWv`, the gradient to the input, and the softmax Jacobian alone — 6 | — |
| `ch35_bridge.ipynb` | 35 | the frozen feature extractor's convolution and pooling, and one step of the chapter's own `train_head()` — 4 | that the transfer-versus-scratch verdict is a single-seed result, and so is deliberately not asserted — 1 |

That is **39 asserted checks** and 4 reported measurements. Every hand-derived gradient agrees
with autograd to a relative difference of 2.4e-11 or better, and most to 1e-16, which is float64
rounding.

## How a chapter's code reaches the check

A bridge that retyped a chapter's arithmetic would agree with itself rather than with the chapter,
so each notebook reads the function it checks **out of the chapter file at run time** — that is
what `one_step()` does. Change a gradient in `code/chNN/` and the corresponding check moves with
it.

## Tolerances

Every check reports a **relative** difference against the size of the quantity compared, because an
absolute threshold means nothing without a scale. Gradients are compared at 1e-9 relative, forward
values at 1e-12. Nothing is rounded or hardcoded to bring a check inside its tolerance.

Two differences are real, expected, and reported rather than absorbed:

- **The loss.** The book writes `log(p + 1e-12)` to keep the logarithm away from zero; torch's
  `cross_entropy` has no such guard, so comparing the two directly shows a gap of about 1e-12 —
  that epsilon and nothing else. Each notebook therefore builds torch's loss with the **chapter's
  own formula**, guard included, so like is compared with like.
- **Max pooling at a tie.** When two cells in a window hold the same maximum, the gradient has no
  single right destination: the chapter's mask feeds every tied cell, PyTorch feeds one.
  `ch32_bridge.ipynb` splits the check — windows with a unique maximum must agree **exactly**, and
  tied windows are counted and reported separately. In the batch tested, 0.69% of windows are tied.

`torch.set_default_dtype(torch.float64)` is set at the top of every notebook, because the book
works in float64 and comparing against float32 would manufacture a disagreement that is not there.

## Running them

```bash
pip install -r ../requirements.txt -r requirements-bridges.txt
jupyter lab            # then run each notebook top to bottom from a fresh kernel
```

Each notebook ends with an assertion, so a bridge that stops agreeing with autograd fails loudly
rather than printing a smaller number.
