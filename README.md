# From Absolute Zero: Companion Code

Companion code, data and figures for **From Absolute Zero: Data science, machine learning, and AI
from no code to transformers and production** by Shanmukh Behara (First Edition, 2026).

> Companion material for the book. ISBN 9798170522552. See `docs/BOOK_METADATA.md`.

---

## About the Book

Forty-five chapters running from a first line of Python to transformers, retrieval, agents and
production monitoring. The book assumes no programming, no calculus and no prior statistics.

Its central discipline: **every program in the book was executed and its real output printed on the
page.** This repository is how you run that code yourself instead of taking the book's word for it.

---

## What This Repository Contains

| | |
|---|---|
| **34 chapters of runnable code** | `code/ch04/` … `code/ch44/` — every code block printed in those chapters, block for block |
| **28 Jupyter notebooks** | `notebooks/` — chapters 16 to 41, 43 and 44, one notebook per chapter (Chapter 42's five short blocks are not packaged as a notebook) |
| **6 generated datasets** | `data/generated/` — synthetic, each written by the printed block that creates it. Two further datasets, `load_digits` and `load_breast_cancer`, are real research data bundled inside scikit-learn; see `DATA_MANIFEST.csv` |
| **75 figures** | `figures/` — all of the book's figures at 400 DPI: 53 produced by the chapter generators, and 22 diagrams with runnable scripts in `figures/sources/`. See `figures/README.md` |
| **Validation tests** | `tests/` — check the repository is intact and consistent |
| **6 framework bridges** | `bridges/` — chapters 30 to 35, each comparing that chapter's hand-derived gradients against PyTorch's autograd. Optional; PyTorch is not needed anywhere else. See `bridges/README.md` |

**11 chapters have no companion directory** (1, 2, 3, 5, 6, 8, 11, 12, 15, 42, 45). Chapters 1 and
45 print no code; the other nine print short blocks that run as printed (Chapters 5, 6, 8, 11 and 12
read `retail.csv` and Chapter 42 reads `hr.csv`, both in `data/generated/`) and are not packaged here.
`docs/CHAPTER_MAP.md` states this per chapter rather than leaving you to discover it.

---

## Repository Structure

```
.
├── code/ch04 … ch44/     one directory per chapter that has companion code
├── data/generated/       the six synthetic datasets (created by gen_*.py in the chapter that makes them)
├── notebooks/            one notebook per chapter, 16–41, 43, 44
├── figures/              all 75 figures, with the diagram scripts in figures/sources/
├── scripts/              helper scripts (regenerate data, verify install)
├── bridges/              optional PyTorch gradient checks for chapters 30-35
├── tests/                repository validation
├── docs/                 guides (start with HOW_TO_USE.md)
└── DATA_MANIFEST.csv     provenance for every dataset
```

---

## Quick Start

```bash
git clone https://github.com/FromAbsoluteZero/CodeBase
cd CodeBase
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/verify_install.py
```

Then open any notebook, or run a chapter's code directly. A chapter's blocks are fragments of one
continuing session, so they are run together, in order, after the shared setup in `_lib.py`
(`python c1.py` on its own stops with a `NameError` — the imports live in `_lib.py`):

```bash
cd code/ch30
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

Every chapter's `README.md` gives this command for that chapter, with the data step first where the
chapter creates its own data.

New to Git or Python? **Read `docs/HOW_TO_USE.md` first** — it starts from installing Python.

---

## Installation

Python **3.11 or newer** (3.11 to 3.14; the pinned NumPy, pandas, SciPy and scikit-learn do not
support 3.10). Dependencies are pinned in `requirements.txt` to the versions the book's
printed output was produced under; the pinned set has been installed and run on 3.11 and 3.13.

```bash
pip install -r requirements.txt
```

`requirements-optional.txt` holds packages needed by only three chapters (`imbalanced-learn` for
Chapter 23, `statsmodels` for Chapter 28, `shap` for Chapter 29). Install it only if you need those
chapters.

---

## Running the Examples

Each chapter directory holds the chapter's printed code blocks as `c1.py`, `c2.py`, `c3.py` … in the
order the book prints them, plus:

- `_lib.py` — the shared setup (imports and the objects the blocks assume), which the book shows once
  at the start of the chapter's session. It must run before the blocks.
- `gen_*.py` — where the chapter's own first block creates a dataset (`retail.csv` in Chapter 4,
  `hr.csv` in Chapter 14, and Step 1 of Chapters 22, 24, 26 and 28), that block is stored under this
  name and is run first. Chapters that read a dataset created elsewhere use the copy in
  `data/generated/` automatically.
- `figs.py` — regenerates the chapter's figures.

Run the blocks **in order** within a chapter, in one interpreter — later blocks assume earlier ones
have defined their variables, exactly as the book presents them. The one-line command in each
chapter's README does exactly that.

---

## Chapter-by-Chapter Guide

See **`docs/CHAPTER_MAP.md`** — every chapter with its code, data, figures, dependencies and
whether it is reproducible.

---

## Data

The six CSV files this repository ships are synthetic and generated by code you can read. Two datasets are **not**: `load_digits` (chapters 27, 30, 31, 32, 33, 35, 39 — the backbone of Part VI) and `load_breast_cancer` (chapter 16) are real, de-identified public research datasets that ship inside scikit-learn. Nothing is downloaded and no account is needed, but they were not built here.

Nothing is downloaded, no account is needed, no personal or private data appears anywhere, and
nothing can rot behind a dead link.

Full provenance is in **`DATA_MANIFEST.csv`** and **`docs/DATA_GUIDE.md`**.

Regenerate everything from scratch:

```bash
python scripts/regenerate_data.py
```

---

## Reproducibility

Every experiment is explicitly seeded. The lines that differ from the book are the ones that
measure elapsed time, and Chapter 39's Step 3, which needs `OMP_NUM_THREADS=1` (single-threaded
BLAS) to match digit for digit. See **`docs/REPRODUCIBILITY.md`**, which distinguishes:

- **Exact reproduction** — the printed number should match digit for digit
- **Approximate reproduction** — small differences are expected and acceptable
- **Conceptual reproduction** — the direction and conclusion hold, the number may not

That distinction matters and the guide is explicit about which chapters fall where.

---

## Expected Results

The book prints the output of every program. If a number you get differs from the page, check your
package versions against `requirements.txt` first, then `docs/TROUBLESHOOTING.md`, which lists the
chapters where a difference is expected and says why. If it still differs, please open an issue
with the chapter, the block, and both numbers.

---

## Troubleshooting

See **`docs/TROUBLESHOOTING.md`**.

---

## Citation

See `CITATION.cff`. ISBN 9798170522552; self-published via Amazon KDP.

---

## License

**Code:** MIT (see `LICENSE`).
**Book text, figures and cover artwork:** *not* covered by the MIT licence. See `LICENSE` for the
distinction, and note the JWST cover image carries its own CC BY 4.0 terms and credit requirement.

---

## Disclaimer

This is educational material. The code is written for clarity and to be read, not for production
deployment. Chapters 30–41 deliberately implement neural networks, attention and transformers in
pure NumPy so the mechanics are visible; these are teaching implementations, not optimised ones.

Regulatory material in Chapter 44 was accurate at the time of writing and is explicitly dated in the
text. Verify current obligations against official sources before relying on it.

---

## Author

Shanmukh Behara. See `docs/AUTHOR_BIO.md`.
