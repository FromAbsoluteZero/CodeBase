# Chapter 32 — Convolutional Networks

Companion code for Chapter 32 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# A convolution slides a small filter across an image, computing a dot` |
| `c2.py` | `# Why convolution instead of a fully connected layer: parameter count,` |
| `c3.py` | `# Pooling shrinks the feature map and buys a little tolerance to small` |
| `c4.py` | `# The backward pass through a convolution, derived and then checked` |
| `c5.py` | `# A minimal CNN trained on the real data: four learned filters, max` |
| `c6.py` | `# Raw accuracy is not the only axis that matters. Shift every test image` |
| `figs.py` | regenerates `fig32_1.png`, `fig32_2.png` |

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

Writes `fig32_1.png`, `fig32_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
