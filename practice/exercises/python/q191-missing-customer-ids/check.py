import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv

path = data_path("retail.csv")
rows = list(csv.DictReader(open(path, newline="")))
exp_n = sum(1 for r in rows if r["CustomerID"].strip() == "")
c = Checker("Q191 · Missing customer IDs", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.missing_customer_ids(path)
c.check("returns a (count, share) tuple", lambda: isinstance(got, tuple) and len(got) == 2 or f"got {got!r}")
c.check(f"count is {exp_n}", lambda: got[0] == exp_n or f"got {got[0]}")
c.check("share is count divided by all rows, as a fraction", lambda: close(got[1], exp_n / len(rows), 1e-9) or f"got {got[1]!r}, expected {exp_n / len(rows)!r}")
c.done()
