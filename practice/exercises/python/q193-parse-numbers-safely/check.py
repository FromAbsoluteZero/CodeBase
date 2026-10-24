import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv, math

path = data_path("retail.csv")
tot = {}
for r in csv.DictReader(open(path, newline="")):
    if not r["InvoiceNo"].startswith("C"):
        tot[r["InvoiceNo"]] = tot.get(r["InvoiceNo"], 0.0) + int(r["Quantity"]) * float(r["UnitPrice"])
exp = sum(tot.values()) / len(tot)
c = Checker("Q193 · Parse numbers safely", which_file(HERE, ".py"))
m = load_module(c.target)
c.check("to_float('12.5') is 12.5", lambda: close(m.to_float("12.5"), 12.5))
c.check("to_float('') returns the default (None)", lambda: m.to_float("") is None or f"got {m.to_float('')!r}")
c.check("to_float('n/a', default=0.0) returns 0.0 without raising", lambda: m.to_float("n/a", default=0.0) == 0.0)
c.check("to_float(None, default=-1) returns -1", lambda: m.to_float(None, default=-1) == -1)
c.check(f"mean_invoice_total over {len(tot)} non-cancelled invoices", lambda: close(m.mean_invoice_total(path), exp, 1e-6) or f"got {m.mean_invoice_total(path)!r}, expected {exp!r}")
c.done()
