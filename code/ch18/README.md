# Chapter 18 — Gradient Descent in Practice

Companion code for Chapter 18 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# The learning rate is the one setting that decides whether training` |
| `c2.py` | `# Why plain descent is slow: it is not the learning rate, it is the shape.` |
| `c3.py` | `# Momentum accumulates a velocity, so consistent directions build speed` |
| `c4.py` | `# Full-batch descent uses every row per step. Mini-batches use a sample,` |
| `c5.py` | `# Schedules earn their place when the gradient is noisy. With mini-batches` |
| `figs.py` | regenerates `fig18_1.png`, `fig18_2.png` |

**5 printed blocks** (`c1.py` … `c5.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Figures

```bash
python figs.py
```

Writes `fig18_1.png`, `fig18_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
