# Chapter 39 — LoRA and Adapters

Companion code for Chapter 39 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# A controlled setting: a large pretrained weight matrix, of the kind a` |
| `c2.py` | `# A regression framing: the loss is direct mean-squared error between` |
| `c3.py` | `# LoRA: freeze the pretrained matrix entirely and train only a low-rank` |
| `c4.py` | `# Does the same pattern hold on a real task, not just a constructed one?` |
| `c5.py` | `# An adapter takes a different architectural approach: rather than` |
| `figs.py` | regenerates `fig39_1.png`, `fig39_2.png` |

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

Writes `fig39_1.png`, `fig39_2.png` into this directory (the shipped versions are in `figures/`).

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.

**Step 3 (`c3.py`) needs single-threaded BLAS to match the book.** Its 300 training steps are
sensitive to the order in which the BLAS library sums the products in `Xtr.T @ dH`, so with a
multithreaded NumPy the six printed losses differ in the third decimal (e.g. 1.668932 instead of
1.638644). Run the command above as

```bash
OMP_NUM_THREADS=1 python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py']: exec(open(f, encoding='utf-8').read())"
```

(on Windows: `set OMP_NUM_THREADS=1` first). Steps 1, 2, 4 and 5 are unaffected, and the chapter's
conclusion does not depend on the digits that move.
See `docs/REPRODUCIBILITY.md` if a number does not match.
