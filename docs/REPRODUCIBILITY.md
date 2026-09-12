# Reproducibility

## Environment

| | |
|---|---|
| Python | 3.11 or newer, up to 3.14 (the printed output was produced on 3.11; the pinned set has also been installed and run on 3.13). 3.10 cannot install the pinned NumPy, pandas, SciPy or scikit-learn |
| Dependencies | pinned in `requirements.txt` |
| Hardware | **CPU only.** No GPU is required or used anywhere in this book |
| Memory | Under 2 GB for every chapter |
| Network | **None.** No downloads, no APIs, no model weights, no accounts. `load_digits` and `load_breast_cancer` are real datasets, but they ship inside scikit-learn and are not fetched |

Chapters 30–41 implement neural networks, convolutions, attention and transformers in **pure
NumPy**. No PyTorch, TensorFlow or JAX is required to run anything in the book, in the 34 chapter
code directories or in the 28 notebooks.

The **optional** `bridges/` notebooks are the one exception: they exist to check the book's
hand-derived gradients against PyTorch's autograd, so they need PyTorch, pinned separately in
`bridges/requirements-bridges.txt`. Nothing else in this repository imports it. That is a
deliberate teaching choice, not a limitation.

---

## Three kinds of reproduction

### EXACT REPRODUCTION
The printed number should match digit for digit at the pinned versions.

Applies to every seeded experiment in the 34 chapter directories. Each block creates its own
explicitly seeded generator (`np.random.default_rng(...)`) rather than sharing mutable state, so a
block's output does not depend on which other blocks ran first. (Chapter 17 is the one place a
generator is shared across blocks; the book reseeds it at the top of Steps 2, 3 and 4, and the
repository does the same.)

### APPROXIMATE REPRODUCTION
Direction and magnitude hold; the final digits may differ.

Expect this when your library versions differ from `requirements.txt`, and on the handful of
lines listed in the table below even at the pinned versions.

### CONCEPTUAL REPRODUCTION
The conclusion holds; the specific number need not.

Applies where you change the setup deliberately (a different seed, sample size or number of
epochs). The book's conclusions are written to survive this.

---

## What to expect, line by line: the one current table

This is the only table you need. It was measured on **one complete run of every chapter
directory in README order, and of every printed block of the nine chapters that have no
directory, at the pinned versions**, and diffed against the book's output boxes.

| Measured on | |
|---|---|
| Book | the First Edition as corrected through 2026-09-12 (Georgia 818 pp / Typography 736 pp); the repository commit is named in the release package's `README.md` |
| Machine | macOS 27 on Apple Silicon (arm64, Apple Accelerate BLAS), Python 3.11.16 |
| Libraries | exactly `requirements.txt` and `requirements-optional.txt` |
| Settings | `OMP_NUM_THREADS=1`, `MPLBACKEND=Agg` |

**Every printed line of every chapter matched exactly, except the lines in this table.** If
your result differs on a line that is *not* listed here, treat it as a real discrepancy and open
an issue with the chapter, the block and both figures.

| Chapter | Lines that may differ | Kind | Note |
|---|---|---|---|
| 4 (`c7.py`), 21 (`c6.py`), 27 (`c5.py`) | elapsed-time lines (`… took 3.7s`, the timing table) | expected on every machine | they measure your machine |
| 9 | the three conditioning residuals (`1.5e+07`, `1.6e+13`, `3.7e+17`) | far-decimal float behaviour | deliberately ill-conditioned inputs at the edge of float64 |
| 13 | `residual mean: -0.000000` vs `0.000000` | sign of a zero | a sum that is zero to six places either way |
| 18 | the one diverged learning-rate row | overflow magnitude | the row exists to show divergence; its magnitude is not meaningful |
| 20 | 10 AUC lines, 3rd–4th decimal | tree ensembles | parallel accumulation and tie-breaking inside scikit-learn |
| 27 | t-SNE ARI 0.781 vs 0.771 | stochastic embedding | t-SNE settles differently across BLAS builds |
| 29 | 17 permutation-importance and SHAP lines, 3rd–4th decimal | resampling | the standard deviations printed beside each value are wider than the differences |
| 33 (Steps 5 and 6) | the sequence-length-40 rows of both tables, and Step 6's averaged attention weights | unstable runs, decided by the last bit | Step 5: the book prints `0.3250`, the pinned environment's value (NumPy 2.4.4 with Apple's Accelerate BLAS, any thread count); NumPy 1.26.4 with OpenBLAS prints `0.3350`; the author's original machine printed `0.3050`; scaling one initial weight matrix by (1 + 2^-52), a single unit in the last place, turns 0.3250 into 0.3050. Inside the trained network the gradient reaching the first step at length 40 is about 1e-08 (Step 2's untrained toy network prints 3.97e-06), so a few test sequences are decided by rounding and the BLAS summation order moves them. Step 6: the attention accuracy at length 40 is `0.9950` here and `1.0000` under OpenBLAS, and the averaged first-step attention weight is 0.084 here, 0.074 under OpenBLAS, and 0.65 after the same one-ulp change, so the flatness of the printed weights is a property of this rounding, not of the seed; the accuracy is what is stable. Lengths 2 to 20 are identical in every build. The plain-RNN values are all chance on three classes (200 test sequences, one standard error 0.033), and the book says so beside both tables. Step 6 reads Step 5's plain-RNN value rather than restating it |
| 39 (Steps 3 and 5) | the six-row rank table and the `lora4_loss` reference | BLAS summation order | see the note below; the conclusion (the 0.131 loss at rank 4) holds either way |

Everything else, including the corrected Chapters 2, 12, 15, 22, 31, 36 and 39 Step 4, matched
digit for digit.

**Chapter 39, Step 3, in detail.** The block's `Xtr.T @ dH` is summed in an order that depends on
the BLAS library, and the difference compounds over 300 steps. With single-threaded OpenBLAS
(`OMP_NUM_THREADS=1` on Linux or Windows) the book's digits reproduce; with multithreaded OpenBLAS
the same code prints 1.668932, 0.901586, 0.131302, 0.125756, 0.127224, 0.123091; on Apple
Silicon (Accelerate) it prints 1.612329, 0.910876, 0.131243, 0.130267, 0.126094, 0.124392 at any
thread count, against the book's 1.638644, 0.912279, 0.130881, 0.126387, 0.127997, 0.124838. Steps
1, 2, 4 and 5 are unaffected; Step 5 carries Step 3's computed value forward rather than
restating it.

**Notebooks.** All 28 execute top to bottom in the same environment (kernel `faz311` in the
release package's `6_Validation/`), and their stored outputs come from that run. A notebook's
"Create the data" cell is the printed block of the chapter that creates the file, so it prints
that chapter's line first (for example `1,470 employees, attrition rate 12.2%` at the top of the
Chapter 16, 19, 20 and 29 notebooks).

**Figures.** Regenerating all 53 chapter figures and the 22 reconstructions in the same
environment reproduces 74 of 75 byte for byte. `fig41_1` renders 6 pixels wider and 5 taller than
the shipped image (a text-extent difference in the bounding box), with the same content. Eight
figures (`fig17_1`, `fig20_2`, `fig23_1`, `fig27_2`, `fig28_2`, `fig29_1`, `fig29_2`, `fig39_1`)
contain a step that is sensitive to library versions and may differ marginally on newer
libraries; see `figures/README.md`.

Wall-clock times worth knowing: Chapter 25 about 7–9 minutes, Chapter 31 about 3–5 minutes,
Chapter 39 about 1 minute single-threaded (3–4 minutes multithreaded), everything else under a
minute.

---

## Seeds

Every stochastic experiment is seeded explicitly. Chapters 30 onward use a per-block seed rather
than one generator threaded through the chapter: an early draft did the latter and produced output
that silently depended on execution order. If you see a block create its own generator, that is why.

---

## Known sources of platform differences

- **BLAS backend and thread count.** Floating-point summation order differs between NumPy builds
  and between thread counts, affecting far decimal places. Chapter 39 Step 3 is where this reaches
  the printed digits. Chapter 33's length-40 row is an unstable run whose last-bit sensitivity makes the BLAS
  build visible (the table above gives the measured values), and the Chapter 20 and 29 rows are
  library-internal tie-breaking or resampling.
- **Thread count in scikit-learn.** Estimators with `n_jobs=-1` may produce last-digit differences
  across machines. Set `n_jobs=1` for strict determinism.
- **Library versions.** The main source of real differences. Pin them.

None of these change a conclusion in this book.

---

## Corrections made before publication, and the tests that guard them

The first-edition draft was audited at the pinned versions and the confirmed defects repaired
before printing. The ones that touch this repository, each with a regression test in `tests/`:

| Where | Defect | Fix | Test |
|---|---|---|---|
| `code/ch39/c4.py` | `train_cnn_source` never updated the convolution filters, so Step 4 measured LoRA on random features | Chapter 35's filter gradient added; Step 4 re-run (LoRA rank 1/2/4/8: 0.5242 / 0.8030 / 0.9517 / 0.9554) | `test_ch39_source_filters_train.py` |
| `code/ch39/c2.py`, `c3.py`, `c5.py` | the updates are the gradient of the squared error summed over the 256 outputs, 256 times the elementwise MSE the tables report: a constant rescaling of every step (an effective learning rate of 256), not a different direction | stated in the text; code unchanged | `test_ch39_loss_convention.py` |
| `code/ch36/c4.py` | top-k and top-p ranked tied probabilities with an unstable sort, so sampled words depended on the platform | `kind="stable"` | `test_stable_sort_ties.py` |
| `code/ch22/c4.py`, `figs.py` | the decile calibration table binned tied probabilities with an unstable sort | `kind="stable"`; Figure 22.2 regenerated | `test_stable_sort_ties.py` |
| `code/ch31/c3.py` | the printed "backward signal" multiplied only the maximum sigmoid slope per layer and called the product the gradient reaching the first layer; the weight matrices multiply the gradient too | the block now also propagates a gradient of 1.0 at every output back through the network's weights (5.28e-05 here, against the slopes-only 1.53e-05), checked against finite differences | `test_ch31_backward_signal.py` |
| `figures/sources/fig15_1.py` | Chapter 15 sized its experiment on the company-wide 12% attrition, but the experiment runs on the employees Chapter 14 flags, whose attrition is 33% | curves recomputed at 33%; the Chapter 15 and 42 blocks carry the corrected sizes (1,328 per arm) | evidence in the release package |
| Chapter 28, Step 7 (text) | the forest's lag features use actual values from inside the test window, which the chapter discloses; under the baselines' own single-origin protocol its MAE is about 909, not 795 | stated in the text; code unchanged | `test_ch28_matched_origin.py` |
| Chapter 5, Step 3 (printed block) | `SUM(rev) OVER (ORDER BY rev DESC)` uses SQLite's default RANGE frame, which adds every tied customer at once, so a top-N running total could include more than N customers | deterministic tie-breaker and `ROWS UNBOUNDED PRECEDING`; the printed table is unchanged | `test_ch05_window_frame.py` |
| Chapter 3, exercises (printed) | three snippets squeezed compound statements onto one line and did not parse | printed as indented code blocks | `test_ch03_exercises.py` |
| Chapter 10, Solution 1 (text) | inferred a loss decrease from the derivative alone | corrected | `test_ch10_finite_step.py` |
| Chapter 2 (printed block) | `int(a // b) + 1` rounded an exact division up by one | `math.ceil` | `test_ch02_breakeven.py` |
| Chapter 33, Step 6 | the attention backward pass had no numerical check in the text | checked against finite differences here | `test_ch33_attention_gradient.py` |
| Chapters 22 and 23 | the six-dollar review cost is charged per review in Chapter 22 and per false positive in Chapter 23's p* and `total_cost()`; the book now says so | text only | `test_ch23_cost_conventions.py` |

Run them all with `pytest tests/` (or `python tests/test_repository.py` for the structural
checks alone).

---

## What is *not* reproducible here

Chapters 1, 2, 3, 5, 6, 8, 11, 12, 15, 42 and 45 have **no companion directory**: Chapters 1 and 45
print no code, and the other nine print short blocks that run as printed (five of them read
`retail.csv`, Chapter 42 reads `hr.csv`). This repository does not package them; the release
package's validation run executes them from the book's own text.

Chapters 37, 40 and 41 report results from **disclosed deterministic simulations**, not from real
language models or APIs. They reproduce exactly, but they are simulations, and the book says so in
the first line of each worked example. See `docs/DATA_GUIDE.md`.
