# How to Use This Repository

Written for someone who has never used GitHub. If you already know Git and virtual environments,
skip to §6.

---

## 1. Install Python

Download Python **3.11 or newer** from <https://www.python.org/downloads/>. Any of 3.11, 3.12,
3.13 or 3.14 works; 3.10 does not, because the pinned NumPy, pandas, SciPy and scikit-learn
require 3.11.

On Windows, tick **"Add Python to PATH"** during installation. This one checkbox causes most of the
"python is not recognised" problems people hit later.

Check it worked:

```bash
python --version
```

If that fails, try `python3 --version`. Use whichever works in every command below.

---

## 2. Install Git

From <https://git-scm.com/downloads>. Check:

```bash
git --version
```

You can skip Git entirely by downloading the repository as a ZIP from GitHub ("Code" → "Download
ZIP") and unzipping it. Everything else still works.

---

## 3. Clone the repository

```bash
git clone https://github.com/FromAbsoluteZero/CodeBase
cd CodeBase
```

---

## 4. Create a virtual environment

A virtual environment keeps this book's packages separate from everything else on your machine.

```bash
python -m venv .venv
```

Activate it:

- **macOS / Linux:** `source .venv/bin/activate`
- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **Windows (cmd):** `.venv\Scripts\activate.bat`

Your prompt should now start with `(.venv)`. **Activate it every time** you open a new terminal.

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

Three chapters need extras (Ch23 `imbalanced-learn`, Ch28 `statsmodels`, Ch29 `shap`):

```bash
pip install -r requirements-optional.txt
```

Confirm everything is in place:

```bash
python scripts/verify_install.py
```

---

## 6. Find a chapter

Open **`docs/CHAPTER_MAP.md`**. It lists every chapter with its code directory, data, figures and
dependencies — and states plainly which chapters have no companion code.

---

## 7. Run a script

Chapter code lives in `code/chNN/`, one file per printed block: `c1.py`, `c2.py`, … in the order the
book prints them. The blocks are **fragments of one continuing session**, not standalone scripts:
later blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`, which the book shows once at the top of the chapter. So `python c1.py` on its own fails
with a `NameError`. Run the setup and the blocks together, in one interpreter, from inside the
chapter directory:

```bash
cd code/ch30
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

Each chapter's `README.md` gives that command with the right file list. To stop after a particular
block, shorten the list. Where a chapter's own first block creates its dataset (Chapters 4, 14, 22,
24, 26, 28 and 38), that block is stored as `gen_*.py` and comes first in the list; where a chapter
reads a dataset another chapter created, `_lib.py` uses the copy in `data/generated/` (or the one
you generated yourself, if it is in the directory).

On Windows `cmd`, the same command works as written (the double quotes are for the shell; the
single quotes are Python's).

---

## 8. Run notebooks

```bash
pip install jupyterlab
jupyter lab
```

Then open `notebooks/chapter_30.ipynb`. Run cells top to bottom with **Shift+Enter**. The first
cell installs the pinned requirements and is for Google Colab; skip it when running locally.

Notebooks exist for chapters 16 to 41, 43 and 44 (28 in all). Chapter 42's five short blocks are
not packaged as a notebook, and Chapters 4, 7, 9, 10, 13 and 14 are covered by their `code/`
directories only (the remaining chapters before 16 print short blocks that run as printed).

---

## 9. Find datasets

All in `data/generated/`. All synthetic. `DATA_MANIFEST.csv` says exactly which chapters use each
file and which script produced it.

---

## 10. Regenerate synthetic data

```bash
python scripts/regenerate_data.py
```

Every dataset is seeded, so regenerating produces byte-identical files.

---

## 11. Reproduce figures

Chapters with figures include a `figs.py`, which runs the chapter's setup itself:

```bash
cd code/ch32
python figs.py
```

The files are written into the chapter directory; pre-generated versions are in `figures/`.

---

## 12. Understanding small numerical differences

Some differences are expected and are **not** errors. `docs/REPRODUCIBILITY.md` explains which
chapters should match exactly, which should match approximately, and which only reproduce
conceptually. Read it before concluding a number is wrong. Two things are expected to differ: any line that
reports elapsed time (Chapters 4, 21 and 27), and Chapter 39's Step 3 unless you run it with
`OMP_NUM_THREADS=1`.

---

## 13. Troubleshooting dependency problems

Most problems are one of three things:

1. **Virtual environment not activated** — your prompt should show `(.venv)`.
2. **Wrong Python** — `python` may point at 3.9 or older; try `python3`.
3. **Version mismatch** — `pip install -r requirements.txt` again; results are pinned to those
   versions.

More in `docs/TROUBLESHOOTING.md`.
