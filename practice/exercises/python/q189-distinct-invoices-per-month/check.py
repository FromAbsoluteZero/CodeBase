import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv
from datetime import date

path = data_path("retail.csv")
exp = {}
for r in csv.DictReader(open(path, newline="")):
    d = date.fromisoformat(r["InvoiceDate"])
    exp.setdefault(f"{d.year}-{d.month:02d}", set()).add(r["InvoiceNo"])
exp = {k: len(v) for k, v in exp.items()}
lines = {}
for r in csv.DictReader(open(path, newline="")):
    lines[r["InvoiceDate"][:7]] = lines.get(r["InvoiceDate"][:7], 0) + 1
c = Checker("Q189 · Distinct invoices per month", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.invoices_per_month(path)
c.check("keys are the twelve months of 2024 as YYYY-MM", lambda: set(got) == set(exp) or f"keys {sorted(got)}")
c.check("counts invoices, not order lines", lambda: dict(got) != lines or "these are row counts; count distinct InvoiceNo values")
c.check("every month matches", lambda: all(got.get(k) == v for k, v in exp.items()) or str({k: (got.get(k), v) for k, v in exp.items() if got.get(k) != v}))
c.check(f"the year totals {sum(exp.values())} invoices", lambda: sum(got.values()) == sum(exp.values()))
c.done()
