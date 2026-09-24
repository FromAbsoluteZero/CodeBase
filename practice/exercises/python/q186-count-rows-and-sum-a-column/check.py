import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv

path = data_path("retail.csv")
rows = list(csv.DictReader(open(path, newline="")))
c = Checker("Q186 · Count rows and sum a column", which_file(HERE, ".py"))
m = load_module(c.target)
c.check("row_count is the number of data rows", lambda: (m.row_count(path) == len(rows)) or f"got {m.row_count(path)}, expected {len(rows)}")
c.check("total_quantity is an int", lambda: isinstance(m.total_quantity(path), int) or "return an int, not a float or a string")
exp = sum(int(r["Quantity"]) for r in rows)
c.check("total_quantity is the sum of Quantity (cancellations count as negative)", lambda: (m.total_quantity(path) == exp) or f"got {m.total_quantity(path)}, expected {exp}")
c.done()
