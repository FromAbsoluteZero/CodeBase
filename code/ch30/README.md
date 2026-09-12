# Chapter 30 — Neural Networks from Scratch

Companion code for Chapter 30 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# A single neuron is a dot product plus a nonlinearity. Nothing more.` |
| `c2.py` | `# Without a nonlinearity, stacking layers is pointless: two linear layers` |
| `c3.py` | `# The forward pass through a real two-layer network, on one digit.` |
| `c4.py` | `# Backpropagation is the chain rule from Chapter 10, applied layer by` |
| `c5.py` | `# Train on the real data: forward, backward, update, repeat.` |
| `c6.py` | `# The baseline discipline from Chapter 1: before trusting the network,` |
| `figs.py` | regenerates `fig30_1.png`, `fig30_2.png` |

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

Writes `fig30_1.png`, `fig30_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
