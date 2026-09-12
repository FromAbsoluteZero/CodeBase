# Chapter 31 — Making Deep Networks Train

Companion code for Chapter 31 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Stack many layers with the naive initialization every tutorial starts` |
| `c2.py` | `# He initialization scales each layer's weights by the width it is` |
| `c3.py` | `# Sigmoid saturates: its gradient is near zero almost everywhere except` |
| `c4.py` | `# Train a genuinely deep network two ways: naive initialization against` |
| `c5.py` | `# Batch normalization rescales each layer's output to zero mean, unit` |
| `c6.py` | `# The BN implementation above never updates gamma and beta: computing` |
| `figs.py` | regenerates `fig31_1.png`, `fig31_2.png` |

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

Writes `fig31_1.png`, `fig31_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
