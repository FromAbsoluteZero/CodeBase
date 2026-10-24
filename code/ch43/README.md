# Chapter 43 — Production: Serving, Drift, MLOps

Companion code for Chapter 43 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Data drift: the distribution of an input feature shifts after` |
| `c2.py` | `# The Population Stability Index bins both distributions the same way` |
| `c3.py` | `# The trap: concept drift changes the relationship between features and` |
| `c4.py` | `# The fix for concept drift is to monitor what the model actually gets` |
| `c5.py` | `# Serving cost has its own tradeoff: batching several requests together` |
| `c6.py` | `# Persisting and serving a model: every model this book has trained so far was` |
| `serve.py` | the ~20-line Flask app `c6.py` starts and queries: loads `churn_pipeline.joblib`, answers `POST /predict` |
| `figs.py` | regenerates `fig43_1.png`, `fig43_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them, plus `serve.py`, the
standalone server `c6.py` starts as a subprocess and `c6.py`'s own request is made against.

`c6.py` needs `flask` and `requests`, in `requirements-optional.txt`
(`pip install -r requirements-optional.txt`); every other block needs only `requirements.txt`.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it. `c6.py` writes `customers.csv` and `churn_pipeline.joblib` into this directory
(reusing Chapter 24's dataset and engineered-features pipeline pattern) and starts `serve.py` as
a background process for the length of one request, then stops it; nothing is left running
afterward. To run the server yourself in a separate terminal instead, see `serve.py`'s own
docstring for the exact `curl` command.

## Figures

```bash
python figs.py
```

Writes `fig43_1.png`, `fig43_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.

## Practice

Interview questions that draw on this chapter: [`practice/by-chapter/ch43.md`](../../practice/by-chapter/ch43.md).
