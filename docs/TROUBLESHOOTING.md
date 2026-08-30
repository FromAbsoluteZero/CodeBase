# Troubleshooting

## `ModuleNotFoundError: No module named 'sklearn'` (or numpy, pandas…)

The virtual environment is not active, or dependencies are not installed.

```bash
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## `ModuleNotFoundError: No module named 'shap'` / `'statsmodels'`

These are optional, used only by Chapters 29 and 28:

```bash
pip install -r requirements-optional.txt
```

## `NameError: name 'X' is not defined`

You ran a block out of order. Chapter blocks (`c1.py`, `c2.py`, …) form one continuing session — run
them in sequence. Alternatively run the self-contained `_`-prefixed version of that block.

## `FileNotFoundError: 'hr.csv'`

Run from inside the chapter directory, or regenerate the data:

```bash
python scripts/regenerate_data.py
```

## My number differs from the book

Check in this order:

1. **Package versions** — `pip freeze` against `requirements.txt`. Tree-based results in particular
   shift between library versions.
2. **`docs/REPRODUCIBILITY.md`** — the chapter may be one where exact matching is not expected.
3. **`ERRATA.md`** — corrections since printing.

If it still differs at the pinned versions and the chapter is listed as exactly reproducible, that is
a defect worth reporting.

## `python` is not recognised (Windows)

Python was installed without "Add Python to PATH". Reinstall with that box ticked, or use the full
path to `python.exe`.

## Chapter 25 is very slow

Expected. Chapter 25's nested cross-validation is the slowest thing here — several minutes on a
laptop. That cost *is* the chapter's point.

## Notebook kernel dies on a deep-learning chapter

Chapters 30–41 are pure NumPy and CPU-only, but some train for many epochs. Reduce the epoch count
in the code if you only want to see it run; the printed numbers will then differ from the book.
