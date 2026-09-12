# Chapter 37 — Alignment / RLHF

Companion code for Chapter 37 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `import numpy as np` |
| `c2.py` | `# Show a labeller two replies; they pick one. Bradley-Terry says the` |
| `c3.py` | `# Fit a reward model: one number per reply, learned only from the choices.` |
| `c4.py` | `# RLHF: raise expected reward, but stay near the pretrained model.` |
| `c5.py` | `# Labellers are human. Suppose they mildly enjoy being flattered,` |
| `c6.py` | `# DPO: no reward model, no sampling. Train the policy straight on the pairs.` |
| `figs.py` | regenerates `fig37_1.png` |

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

Writes `fig37_1.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.

Note: the book's Step 3 output box begins by repeating four lines of Step 2's output. `c3.py`
prints only the reward table and the correlation line.
See `docs/REPRODUCIBILITY.md` if a number does not match.
