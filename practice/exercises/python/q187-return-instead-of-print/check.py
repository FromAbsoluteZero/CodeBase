import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv, io, contextlib

rows = list(csv.DictReader(open(data_path("retail.csv"), newline="")))
inv = [r for r in rows if r["InvoiceNo"] == "536001"]
c = Checker("Q187 · Return instead of print", which_file(HERE, ".py"))
m = load_module(c.target)
c.check("line_revenue(3, 31.0) returns 93.0", lambda: close(m.line_revenue(3, 31.0), 93.0) or f"got {m.line_revenue(3, 31.0)!r}")
c.check("line_revenue accepts the strings a CSV reader gives you", lambda: close(m.line_revenue("4", "12.5"), 50.0) or f"got {m.line_revenue('4', '12.5')!r}")
exp = sum(float(r["Quantity"]) * float(r["UnitPrice"]) for r in inv)
c.check(f"invoice_total of invoice 536001 ({len(inv)} lines)", lambda: close(m.invoice_total(inv), exp) or f"got {m.invoice_total(inv)!r}, expected {exp}")
def silent():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        v = m.invoice_total(inv)
    return (v is not None and buf.getvalue() == "") or "the function printed instead of (or as well as) returning"
c.check("nothing is printed; the value comes back", silent)
c.done()
