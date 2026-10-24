import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv

path = data_path("retail.csv")
tot = {}
for r in csv.DictReader(open(path, newline="")):
    tot[r["Description"]] = tot.get(r["Description"], 0) + int(r["Quantity"])
exp = sorted(tot.items(), key=lambda kv: (-kv[1], kv[0]))
c = Checker("Q192 · Top products by quantity", which_file(HERE, ".py"))
m = load_module(c.target)
c.check("top 3 are right, in order", lambda: [tuple(x) for x in m.top_products(path, 3)] == exp[:3] or f"got {m.top_products(path, 3)}; expected {exp[:3]}")
c.check("n larger than the number of products returns them all", lambda: [tuple(x) for x in m.top_products(path, 50)] == exp or "should return all products when n exceeds their number")
c.check("n = 1 returns one tuple", lambda: len(m.top_products(path, 1)) == 1)
c.done()
