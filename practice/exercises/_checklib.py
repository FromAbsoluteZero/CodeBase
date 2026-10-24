"""Shared helpers for the exercise checks. MIT licence, like the rest of the code.

Each exercise folder holds a README.md (the task), a starter file you complete, a solution file,
and check.py. Run check.py from anywhere:

    python practice/exercises/<area>/<exercise>/check.py              checks your starter file
    python practice/exercises/<area>/<exercise>/check.py --solution   checks the reference solution

The Python exercises need only the standard library. The pandas, SQL and challenge exercises need the
versions pinned in requirements.txt.
"""
from __future__ import annotations

import importlib.util
import math
import sys
import traceback
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data" / "generated"


def data_path(name: str) -> Path:
    p = DATA / name
    if not p.exists():
        raise SystemExit(f"{p} is missing. Run python scripts/regenerate_data.py from the repository root.")
    return p


def which_file(here: Path, suffix: str) -> Path:
    """The file to check: the starter by default, the solution with --solution."""
    name = "solution" if "--solution" in sys.argv else "starter"
    return here / f"{name}{suffix}"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem + "_under_check", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def close(a, b, tol=1e-6) -> bool:
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


class Checker:
    """Collects named checks, prints one line each, and exits 1 if any failed."""

    def __init__(self, title: str, target: Path):
        self.title, self.target, self.failed, self.n = title, target, 0, 0
        print(f"{title}\nchecking {target.relative_to(REPO)}\n")

    def check(self, label: str, fn):
        self.n += 1
        try:
            ok = fn()
            if isinstance(ok, str):
                ok, msg = False, ok
            else:
                ok, msg = (ok is None) or bool(ok), ""
        except NotImplementedError:
            ok, msg = False, "not written yet (the function still raises NotImplementedError)"
        except AssertionError as e:
            ok, msg = False, str(e) or "assertion failed"
        except Exception as e:  # show the reader their own error, briefly
            ok, msg = False, f"{type(e).__name__}: {e}"
            if "--verbose" in sys.argv:
                traceback.print_exc()
        self.failed += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"\n        {msg}" if msg and not ok else ""))
        return ok

    def done(self):
        print()
        if self.failed:
            print(f"{self.failed} of {self.n} checks failed.")
            sys.exit(1)
        print(f"All {self.n} checks passed.")
        sys.exit(0)


# ----------------------------------------------------------------------------- SQL

def orders_connection():
    """The in-memory database Chapter 5 builds: retail.csv as the table `orders`, with Revenue added."""
    import sqlite3

    import pandas as pd

    df = pd.read_csv(data_path("retail.csv"))
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    con = sqlite3.connect(":memory:")
    df.to_sql("orders", con, index=False, if_exists="replace")
    return con


def run_sql_file(con, path: Path):
    """Run the single query in a .sql file and return a DataFrame."""
    import pandas as pd

    sql = "\n".join(line for line in path.read_text(encoding="utf-8").splitlines()
                    if not line.strip().startswith("--")).strip()
    if not sql or sql.rstrip(";").strip().upper() == "SELECT NULL":
        raise NotImplementedError
    return pd.read_sql(sql, con)


def frame_equal(got, expected, sort_by=None, tol=1e-6):
    """Compare two DataFrames by columns and values, ignoring the index. Returns True or a message."""
    import pandas as pd

    if list(got.columns) != list(expected.columns):
        return f"columns are {list(got.columns)}; expected {list(expected.columns)}"
    if len(got) != len(expected):
        return f"{len(got)} rows; expected {len(expected)}"
    g, e = got.reset_index(drop=True), expected.reset_index(drop=True)
    if sort_by:
        g = g.sort_values(sort_by, kind="mergesort").reset_index(drop=True)
        e = e.sort_values(sort_by, kind="mergesort").reset_index(drop=True)
    for c in expected.columns:
        for i, (a, b) in enumerate(zip(g[c], e[c])):
            if pd.isna(a) and pd.isna(b):
                continue
            if isinstance(b, (int, float)) and not isinstance(b, bool):
                if pd.isna(a) or not close(a, b, tol):
                    return f"row {i}, column {c}: got {a!r}, expected {b!r}"
            elif str(a) != str(b):
                return f"row {i}, column {c}: got {a!r}, expected {b!r}"
    return True
