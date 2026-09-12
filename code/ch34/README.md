# Chapter 34 — Transformers: Self-Attention

Companion code for Chapter 34 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Self-attention: every position produces a query, a key, and a value.` |
| `c2.py` | `# Why divide the scores by sqrt(d_k): the same variance-control argument` |
| `c3.py` | `# Self-attention has no built-in sense of order. Shuffle the input` |
| `c4.py` | `# Multi-head attention runs several smaller attention operations in` |
| `c5.py` | `# The self-attention backward pass. Every position is simultaneously a` |
| `c6.py` | `# A minimal transformer block: self-attention, a residual connection,` |
| `figs.py` | regenerates `fig34_1.png`, `fig34_2.png` |

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

## Figures

```bash
python figs.py
```

Writes `fig34_1.png`, `fig34_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
