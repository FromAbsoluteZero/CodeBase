# Python you will forget and look up

Chapters 2 and 3 teach these; they come up in every chapter after.

| Task | Idiom | Chapter |
|---|---|---|
| f-string | `f"{name}: {value:.2f}"` · `{x:,}` for thousands separators · `{p:.1%}` for percent | 2 |
| Floor division / modulo | `7 // 2 == 3` · `7 % 2 == 1` · useful together for whole groups and remainder | 2 |
| Slice | `xs[0:2]` excludes the end · `xs[-1]` is the last · `xs[::-1]` reverses | 3 |
| Dictionary get | `d.get(key, default)` — no `KeyError` if the key is missing · `d.setdefault(key, [])` creates and returns | 3 |
| Counting | `from collections import Counter; Counter(items).most_common(3)` | 3 |
| Comprehension | `[f(x) for x in xs if cond(x)]` · `{k: v for k, v in pairs}` | 3 |
| Enumerate / zip | `for i, x in enumerate(xs)` · `for a, b in zip(xs, ys)` | 3 |
| Sort by key | `sorted(xs, key=lambda r: r["score"], reverse=True)` · ties: `key=lambda r: (-r["score"], r["name"])` | 3 |
| Float equality | Never use `==`. `math.isclose(a, b, rel_tol=1e-9)`, or compare `abs(a - b) < tol` | 2 |
| Parse safely | `try: x = float(s) except ValueError: x = default` | 3 |
| Read a CSV without pandas | `with open(path, newline="") as f: for row in csv.DictReader(f): ...` — every value is a string | 3 |
| Return, don't print | A function that prints hands back `None`; return the value so it can be stored, tested and composed | 3 |
| Mutable default | `def f(x, acc=None): acc = [] if acc is None else acc` — never `acc=[]` | 3 |
| Copy vs reference | `b = a[:]` or `list(a)` copies a list; `b = a` does not | 3 |
| Run a file from the terminal | `python script.py` · check where you are with `import os; os.getcwd()` | 2 |

Practise: [Q186](../../practice/by-topic/python-pandas-data.md#q186) to
[Q195](../../practice/by-topic/python-pandas-data.md#q195), standard library only.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
