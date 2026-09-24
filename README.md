# From Absolute Zero: Companion Repository

Companion code, data, figures, practice and reference material for **From Absolute Zero: Data science, machine learning, and AI
from no code to transformers and production** by Shanmukh Behara (First Edition, 2026).

> Companion material for the book. ISBN 9798170522552. See `docs/BOOK_METADATA.md`.

**Start here:** [run a chapter's code](#quick-start) · [practise a chapter](practice/by-chapter/README.md) · [sit a mock interview](practice/mock-interviews/README.md) · [cheat sheets, prompts and templates](reference/README.md) · [errata](docs/ERRATA.md)

---

## About the Book

Forty-five chapters running from a first line of Python to transformers, retrieval, agents and
production monitoring. The book assumes no programming, no calculus and no prior statistics.

Its central discipline: **every program in the book was executed and its real output printed on the
page.** This repository is how you run that code yourself instead of taking the book's word for it.

The book and this repository are designed to be used together and do different jobs. The book is for
learning and understanding: the reasoning, the explanations, the worked examples with their real output,
and the core practice at the end of every chapter. The repository is for running, practising, searching
and reusing: the code, the datasets, the figures, the interview question bank, the coding exercises,
the cheat sheets, the prompt library and the templates, kept current and corrected over time while the
printed teaching stays stable.

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
| **Interview practice** | `practice/` — the question bank (Q1 to Q185 from the book, Q186 on added here), organised by chapter, topic, level and type, with mock interviews, coding exercises on the book's datasets that check themselves, and a progress tracker. See `practice/README.md` |
| **Reference** | `reference/` — the full cheat sheets, the complete AI-assistant prompt library, Git help, portfolio guidance and templates to copy into your own projects. See `reference/README.md` |
| **Errata** | `docs/ERRATA.md` — corrections to the printed book |

**11 chapters have no companion code directory** (1, 2, 3, 5, 6, 8, 11, 12, 15, 42, 45). Chapters 1 and
45 print no code; the other nine print short blocks that run as printed (Chapters 5, 6, 8, 11 and 12
read `retail.csv` and Chapter 42 reads `hr.csv`, both in `data/generated/`) and are not packaged here.
Every chapter, including those eleven, has a practice page under `practice/by-chapter/`.
`docs/CHAPTER_MAP.md` states all of this per chapter rather than leaving you to discover it.

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
├── practice/             interview question bank, mock interviews, coding exercises, tracker
├── reference/            cheat sheets, AI-assistant prompts, Git help, portfolio guide, templates
├── tests/                repository validation (including the practice bank and exercises)
├── docs/                 guides (start with HOW_TO_USE.md); ERRATA.md for corrections
├── LICENSES/             full licence texts; LICENSING.md maps folders to licences
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

See **`docs/CHAPTER_MAP.md`** — every chapter with its code, data, figures, dependencies,
whether it is reproducible, and how many practice questions start there.

---

## Practice and Interview Preparation

`practice/` holds the interview question bank the book's Appendix C points to, and it needs no Python
unless you want the coding exercises: every page reads in the browser or in the downloaded ZIP.

- **By chapter:** `practice/by-chapter/chNN.md`, for example `practice/by-chapter/ch22.md` for
  Chapter 22. Every chapter has a page, even the ones with no code.
- **By topic, level or type:** `practice/by-topic/`, `practice/by-level.md`, `practice/by-type.md`.
- **Mock interviews:** timed sets modelled on real rounds, with the answer notes on a separate sheet.
- **Coding exercises:** Python, pandas and SQL tasks and multi-step challenges on the book's own
  datasets, each with a check that tells you whether your answer is right:
  `python practice/exercises/sql/q208-revenue-by-category/check.py`.
- **Progress:** copy `practice/tracker.csv` and fill it in.

Answer aloud, then open the note. Question numbers are permanent: Q1 to Q185 are the book's, and new
ones continue from Q186. Start at `practice/README.md`.

The code that matches the printed pages is kept at the tag `print-2026-09`; the practice and reference
material is corrected and extended over time, and `practice/CHANGELOG.md` records every change.

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
chapters where a difference is expected and says why, and `docs/ERRATA.md` for known corrections.
If it still differs, please open an issue with the chapter, the block, and both numbers.

---

## Troubleshooting

See **`docs/TROUBLESHOOTING.md`**.

---

## Citation

See `CITATION.cff`. ISBN 9798170522552; self-published via Amazon KDP.

---

## License

Four sets of terms, mapped folder by folder in **`LICENSING.md`**:

- **Code and executable material** (`code/`, `notebooks/`, `bridges/`, `scripts/`, `tests/`, the exercise
  starters, solutions and checks) and the **generated datasets**: MIT.
- **Book-derived text** (the question bank and every page generated from it, the cheat sheets, the
  prompt library, the guides and this documentation): CC BY-NC-SA 4.0.
- **Templates meant to be copied** (`reference/templates/`, `practice/tracker.csv`): CC0.
- **The book's text and figures**, including the figure images here, are all rights reserved; the JWST
  cover image carries its own CC BY 4.0 credit requirement.

Full texts in `LICENSES/`.

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
