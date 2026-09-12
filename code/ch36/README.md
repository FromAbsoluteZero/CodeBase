# Chapter 36 — Large Language Models

Companion code for Chapter 36 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Byte-pair encoding builds a vocabulary bottom-up: start from individual` |
| `c2.py` | `# A larger vocabulary means fewer tokens per sentence, at the cost of a` |
| `c3.py` | `# A next-token distribution to decode from. A trigram model: predict the` |
| `c4.py` | `# Four ways to turn a probability distribution into an actual next word.` |
| `c5.py` | `# Quantify what "repetitive" actually means: the fraction of generated` |
| `c6.py` | `# Scaling laws, at a scale small enough to run in seconds rather than` |
| `c7.py` | `# Capacity interacts with data. A higher-order model (more context,` |
| `figs.py` | regenerates `fig36_1.png`, `fig36_2.png`, `fig36_3.png` |

**7 printed blocks** (`c1.py` … `c7.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Figures

```bash
python figs.py
```

Writes `fig36_1.png`, `fig36_2.png`, `fig36_3.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
