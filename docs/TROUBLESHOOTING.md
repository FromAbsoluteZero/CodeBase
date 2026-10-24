# Troubleshooting

## `ModuleNotFoundError: No module named 'sklearn'` (or numpy, pandas…)

The virtual environment is not active, or dependencies are not installed.

```bash
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## `ModuleNotFoundError: No module named 'shap'` / `'statsmodels'`

These are optional, used only by Chapters 23, 28 and 29:

```bash
pip install -r requirements-optional.txt
```

## `NameError: name 'X' is not defined`

You ran a block on its own, or out of order. Chapter blocks (`c1.py`, `c2.py`, …) form one continuing
session whose imports and shared objects live in `_lib.py`, so `python c1.py` by itself cannot work.
Run the setup and the blocks together in one interpreter, from the chapter directory — the exact
command is in the chapter's `README.md`:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py']: exec(open(f, encoding='utf-8').read())"
```

## `FileNotFoundError: 'hr.csv'`

Run from inside the chapter directory, and run `_lib.py` first (the chapter README's command does
both): `_lib.py` copies the shipped file from `data/generated/` into the directory if it is not
there. If `data/generated/` itself is missing or damaged, regenerate it:

```bash
python scripts/regenerate_data.py
```

## My number differs from the book

Check in this order:

1. **Package versions** — `pip freeze` against `requirements.txt`. Tree-based results in particular
   shift between library versions.
2. **`docs/REPRODUCIBILITY.md`** — the chapter may be one where exact matching is not expected.

If it still differs at the pinned versions and the chapter is listed as exactly reproducible, that is
a defect worth reporting.

## Chapter 39's Step 3 prints 1.668932 instead of 1.638644

Your NumPy is using a multithreaded BLAS. Step 3's 300 update steps are sensitive to the summation
order inside `Xtr.T @ dH`, so the six losses move in the third decimal. Run with `OMP_NUM_THREADS=1`
(Windows: `set OMP_NUM_THREADS=1` first) and they match the book exactly. Nothing else in the book
is affected.

## A timing line differs from the book

Lines that report milliseconds or seconds (Chapter 4's loop-versus-vectorized comparison, Chapter
21's timing table, Chapter 27's t-SNE line) measure your machine. Everything else on those pages is
deterministic.

## `python` is not recognised (Windows)

Python was installed without "Add Python to PATH". Reinstall with that box ticked, or use the full
path to `python.exe`.

## Chapter 25 is very slow

Expected. Chapter 25's nested cross-validation is the slowest thing here — several minutes on a
laptop. That cost *is* the chapter's point.

## Notebook kernel dies on a deep-learning chapter

Chapters 30–41 are pure NumPy and CPU-only, but some train for many epochs. Reduce the epoch count
in the code if you only want to see it run; the printed numbers will then differ from the book.
