# Chapter 27 — Dimensionality Reduction

Companion code for Chapter 27 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# PCA finds directions of maximum variance. On four correlated behavioural` |
| `c2.py` | `# 64 pixels per digit. How many directions does that really occupy?` |
| `c3.py` | `# Does compressing cost accuracy? Fit inside a pipeline so PCA is` |
| `c4.py` | `# PCA is fitted on data, so it leaks like any other transformation.` |
| `c5.py` | `# t-SNE preserves neighbourhoods, not distances. It is a viewing tool.` |
| `c6.py` | `# Chapter 26 clustered in the original space. Does reducing first help?` |
| `figs.py` | regenerates `fig27_1.png`, `fig27_2.png` |

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

`segments.csv` is created by Chapter 26 (`code/ch26/gen_seg.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/segments.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig27_1.png`, `fig27_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
The one exception is the `t-SNE took …s` line in `c5.py`: it measures your machine and will differ.
See `docs/REPRODUCIBILITY.md` if a number does not match.
