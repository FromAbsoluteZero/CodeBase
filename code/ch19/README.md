# Chapter 19 — Decision Trees

Companion code for Chapter 19 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `def entropy(p):` |
| `c2.py` | `# Is overtime really the best available split? Check every feature.` |
| `c3.py` | `# The criterion must match what you computed. sklearn defaults to gini.` |
| `c4.py` | `# A tree left alone memorizes. Pruning is not optional.` |
| `c5.py` | `t = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)` |
| `c6.py` | `t = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)` |
| `figs.py` | regenerates `fig19_1.png`, `fig19_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
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

Writes `fig19_1.png`, `fig19_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
