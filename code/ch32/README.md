# Chapter 32 — Convolutional Networks

Companion code for Chapter 32 of *From Absolute Zero*.

## Running it

Run the blocks **in order** — later blocks use variables defined by earlier ones, exactly as
the book presents them as one continuing session.

```bash
python c1.py
python c2.py
python c3.py
python c4.py
python c5.py
python c6.py
```

**6 code blocks**, matching the worked-example steps in the book.

## Figures

```bash
python figs.py
```

## Note

This chapter is implemented in **pure NumPy**. No PyTorch, TensorFlow or JAX is required.
That is deliberate: the point is that the gradients and tensor shapes stay inspectable.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book. See `docs/REPRODUCIBILITY.md` if it does not.
