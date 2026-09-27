import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv
from collections import Counter

path = data_path("retail.csv")
exp = Counter(r["InvoiceNo"] for r in csv.DictReader(open(path, newline="")))
c = Checker("Q194 · Lines per invoice", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.lines_per_invoice(path)
c.check(f"one key per invoice ({len(exp)})", lambda: len(got) == len(exp) or f"got {len(got)} keys")
c.check("counts match for every invoice", lambda: all(got.get(k) == v for k, v in exp.items()) or "some invoice counts differ")
for k in (1, 3, 5):
    e = sum(1 for v in exp.values() if v > k)
    c.check(f"invoices with more than {k} lines: {e}", lambda k=k, e=e: m.invoices_with_more_than(path, k) == e or f"got {m.invoices_with_more_than(path, k)}")
c.done()
