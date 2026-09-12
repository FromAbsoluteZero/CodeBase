# Chapter 41 — Agents and Tool Use

Companion code for Chapter 41 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# An agent completes a task by taking several steps in sequence: plan,` |
| `c2.py` | `# Retrying a failed step raises the effective per-step success rate, at` |
| `c3.py` | `# A transparent toy router: it picks a tool by keyword match against a` |
| `c4.py` | `# Chain the router into a multi-step task: each step must pick the` |
| `c5.py` | `# An agent must also decide WHEN to stop: continuing after the real` |
| `figs.py` | regenerates `fig41_1.png`, `fig41_2.png` |

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

Writes `fig41_1.png`, `fig41_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
