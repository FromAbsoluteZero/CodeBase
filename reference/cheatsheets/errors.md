# Reading an error message

Read a traceback **from the bottom up**. The last line names the error and is the one that matters; the
lines above it are the path the interpreter took to get there. The first line that refers to your own
file is where to look.

| Error | What it usually means | Chapter |
|---|---|---|
| `NameError` | Used before defined, or a typo. In a notebook, often a cell run out of order | 2 |
| `TypeError` | Wrong kind of thing — commonly a string where a number was expected, such as a value read from a CSV | 2 |
| `ValueError` | Right type, impossible value — `int("abc")`, or mismatched array shapes | 2 |
| `KeyError` | Dictionary key or DataFrame column that is not there. Print the keys, or `df.columns` | 3, 4 |
| `IndexError` | Position past the end of a list | 3 |
| `AttributeError` | Method that does not exist on that object — often the object is not what you think it is; print `type(x)` | 3 |
| `IndentationError` | Mixed tabs and spaces, or a block that does not line up | 2 |
| `FileNotFoundError` | Wrong path, or running from the wrong directory. Check with `os.getcwd()` | 4 |
| `ZeroDivisionError` | A group or denominator that is empty. Guard the division | 3 |
| `MergeError` | `validate=` caught a key that is not unique on the side you said it was. That is the check working | 4 |
| `SettingWithCopyWarning` | Older pandas only. In pandas 3 a filter always returns a copy and there is no warning; assign with `.loc` on the original frame | 4 |
| `ConvergenceWarning` | The optimizer stopped early. Scale the features or raise `max_iter` | 14 |
| `ModuleNotFoundError` | The package is not installed in the environment that is running, or the wrong environment is active | 2 |

More, with the fixes this repository needs: [docs/TROUBLESHOOTING.md](../../docs/TROUBLESHOOTING.md).

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
