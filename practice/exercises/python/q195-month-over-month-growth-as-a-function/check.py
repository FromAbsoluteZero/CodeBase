import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv

path = data_path("daily_revenue.csv")
exp = {}
for r in csv.DictReader(open(path, newline="")):
    exp[r["Date"][:7]] = exp.get(r["Date"][:7], 0.0) + float(r["Revenue"])
c = Checker("Q195 · Month-over-month growth as a function", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.monthly_revenue(path)
c.check(f"{len(exp)} months", lambda: set(got) == set(exp) or f"keys {sorted(got)[:3]}…")
c.check("monthly totals match", lambda: all(close(got[k], v, 1e-6) for k, v in exp.items()))
toy = {"2024-03": 300.0, "2024-01": 100.0, "2024-02": 200.0}
g = m.mom_growth(toy)
c.check("first month is None even when the dictionary is out of order", lambda: g.get("2024-01", 0) is None or f"got {g.get('2024-01')!r}")
c.check("2024-02 grew 100%", lambda: close(g["2024-02"], 1.0))
c.check("2024-03 grew 50%", lambda: close(g["2024-03"], 0.5))
months = sorted(exp); full = m.mom_growth(exp)
e2 = (exp[months[1]] - exp[months[0]]) / exp[months[0]]
c.check(f"on the real data, {months[1]} growth is {e2:+.4f}", lambda: close(full[months[1]], e2, 1e-9))
c.done()
