# Chapter 16 — Generalization: Splits, Validation, and Leakage

Companion code for Chapter 16 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `hr = pd.read_csv("hr.csv")` |
| `c2.py` | `print(f"{'depth':>6}{'train AUC':>11}{'test AUC':>10}{'leaves':>8}")` |
| `c3.py` | `cv = StratifiedKFold(5, shuffle=True, random_state=0)` |
| `c4.py` | `from sklearn.datasets import load_breast_cancer` |
| `c5.py` | `# 600 tickets triaged by four agents. Each agent has their own habit: some` |
| `c6.py` | `pipe = Pipeline([("scale", StandardScaler()),` |
| `c7.py` | `pipe = Pipeline([("scale", StandardScaler()),` |
| `c8.py` | `pipe = Pipeline([("scale", StandardScaler()),` |
| `figs.py` | regenerates `fig16_2.png`, `fig16_3.png` |

**8 printed blocks** (`c1.py` … `c8.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`hr.csv` is created by Chapter 14 (`code/ch14/gen_hr.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/hr.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig16_2.png`, `fig16_3.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
