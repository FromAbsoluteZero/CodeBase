# Reproducibility

## Environment

| | |
|---|---|
| Python | 3.10 or newer (developed and verified on 3.12) |
| Dependencies | pinned in `requirements.txt` |
| Hardware | **CPU only.** No GPU is required or used anywhere in this book |
| Memory | Under 2 GB for every chapter |
| Network | **None.** No downloads, no APIs, no model weights, no accounts |

Chapters 30–41 implement neural networks, convolutions, attention and transformers in **pure
NumPy**. No PyTorch, TensorFlow or JAX is required to run anything in this repository. That is a
deliberate teaching choice, not a limitation.

---

## Three kinds of reproduction

This distinction matters and is used throughout the book.

### EXACT REPRODUCTION
The printed number should match digit for digit at the pinned versions.

Applies to every seeded experiment in chapters 16–44. Each block creates its own explicitly seeded
generator (`np.random.default_rng(...)`) rather than sharing mutable state, so a block's output does
not depend on which other blocks ran first.

**Verified during production:** across the book's audits, individual chapters were re-executed from
source and compared to the printed page. Chapters checked this way — including 17, 18, 19, 20, 22,
23, 25, 28, 29, 30, 31, 32, 33, 34, 36, 37, 39, 40, 41, 43 and 44 — reproduced their published values
exactly, with no discrepancies found.

### APPROXIMATE REPRODUCTION
Direction and magnitude hold; the final digits may differ.

Expect this when your library versions differ from `requirements.txt`. Tree ensembles and any
algorithm whose tie-breaking or parallelism changed between releases are the usual causes.

### CONCEPTUAL REPRODUCTION
The conclusion holds; the specific number need not.

Applies where you change the setup deliberately — different seed, different sample size, reduced
epochs. The book's conclusions are written to survive this. Several were explicitly tested across
multiple seeds during production, including the fairness threshold result in Chapter 44 and the
ensemble convergence claim in Chapter 20.

---

## Seeds

Every stochastic experiment is seeded explicitly. Chapters 30 onward use a per-block seed rather
than one generator threaded through the chapter — an early draft did the latter and produced output
that silently depended on execution order. If you see a block create its own generator, that is why.

---

## Known nondeterminism

- **Thread count.** Some scikit-learn estimators with `n_jobs=-1` may produce last-digit differences
  across machines. Set `n_jobs=1` for strict determinism.
- **BLAS backend.** Floating-point summation order can differ between NumPy builds, affecting far
  decimal places.
- **Library versions.** The main source of real differences. Pin them.

None of these change a conclusion in this book.

---

## What is *not* reproducible here

Chapters 1–15 have **no separate companion source files** — their code appears inline in the book.
This repository cannot re-execute them, and no claim of exact reproduction is made for them.

Chapters 37, 40 and 41 report results from **disclosed deterministic simulations**, not from real
language models or APIs. They reproduce exactly, but they are simulations, and the book says so in
the first line of each worked example. See `docs/DATA_GUIDE.md`.
