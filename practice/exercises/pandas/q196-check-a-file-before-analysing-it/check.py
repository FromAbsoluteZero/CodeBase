import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
c = Checker("Q196 · Check a file before analysing it", which_file(HERE, ".py"))
m = load_module(c.target)
p = m.profile(df)
c.check("returns a dict with the six keys", lambda: set(p) == {"rows", "columns", "null_counts", "duplicate_rows", "date_min", "date_max"} or f"keys {sorted(p)}")
c.check(f"rows = {len(df)}", lambda: p["rows"] == len(df))
c.check("columns in file order", lambda: list(p["columns"]) == list(df.columns))
exp_null = {k: int(v) for k, v in df.isna().sum().items() if v}
c.check(f"null_counts lists only columns with missing values: {exp_null}", lambda: dict(p["null_counts"]) == exp_null or f"got {p['null_counts']}")
c.check(f"duplicate_rows = {int(df.duplicated().sum())}", lambda: p["duplicate_rows"] == int(df.duplicated().sum()) or f"got {p['duplicate_rows']}")
c.check("date range as YYYY-MM-DD strings", lambda: (p["date_min"], p["date_max"]) == (df.InvoiceDate.min(), df.InvoiceDate.max()) or f"got {p['date_min']!r}, {p['date_max']!r}")
c.done()
