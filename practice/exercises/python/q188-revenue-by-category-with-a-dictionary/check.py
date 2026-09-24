import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv
from collections import defaultdict

path = data_path("retail.csv")
exp = defaultdict(float)
for r in csv.DictReader(open(path, newline="")):
    exp[r["Category"]] += int(r["Quantity"]) * float(r["UnitPrice"])
c = Checker("Q188 · Revenue by category with a dictionary", which_file(HERE, ".py"))
m = load_module(c.target)
got = {}
c.check("returns a dict", lambda: isinstance((got.update(m.revenue_by_category(path)) or got), dict))
c.check(f"one key per category ({len(exp)})", lambda: set(got) == set(exp) or f"keys {sorted(got)}; expected {sorted(exp)}")
for k in sorted(exp):
    c.check(f"{k}: {exp[k]:.2f}", lambda k=k: close(got.get(k, float('nan')), exp[k], 1e-6) or f"got {got.get(k)!r}")
c.done()
