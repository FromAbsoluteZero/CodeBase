# How to Use This Repository

Written for someone who has never used GitHub. If you already know Git and virtual environments,
skip to §6.

---

## 1. Install Python

Download Python **3.10 or newer** from <https://www.python.org/downloads/>.

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

Two chapters need extras (Ch28 `statsmodels`, Ch29 `shap`):

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

Chapter code lives in `code/chNN/`, split into numbered blocks matching the book's worked-example
steps.

```bash
cd code/ch30
python c1.py
python c2.py
```

**Run the blocks in order.** Later blocks assume variables defined by earlier ones — the same way
the book presents them as one continuing session.

Files starting with `_` are self-contained duplicates used to regenerate the book's printed output.
Ignore them unless you are rebuilding the book.

---

## 8. Run notebooks

```bash
pip install jupyterlab
jupyter lab
```

Then open `notebooks/chapter_30.ipynb`. Run cells top to bottom with **Shift+Enter**.

Notebooks exist for chapters 16–44.

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

Chapters with figures include a `figs.py`:

```bash
cd code/ch32
python figs.py
```

Pre-generated versions are in `figures/`.

---

## 12. Understanding small numerical differences

Some differences are expected and are **not** errors. `docs/REPRODUCIBILITY.md` explains which
chapters should match exactly, which should match approximately, and which only reproduce
conceptually. Read it before concluding a number is wrong.

---

## 13. Troubleshooting dependency problems

Most problems are one of three things:

1. **Virtual environment not activated** — your prompt should show `(.venv)`.
2. **Wrong Python** — `python` may point at 3.9 or older; try `python3`.
3. **Version mismatch** — `pip install -r requirements.txt` again; results are pinned to those
   versions.

More in `docs/TROUBLESHOOTING.md`.
