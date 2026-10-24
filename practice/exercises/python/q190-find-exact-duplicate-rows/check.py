import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401

import csv
from collections import Counter

path = data_path("retail.csv")
reader = csv.reader(open(path, newline="")); next(reader)
rows = [tuple(r) for r in reader]
cnt = Counter(rows)
exp_rows = [r for r in dict.fromkeys(rows) if cnt[r] > 1]
exp_extra = sum(n - 1 for n in cnt.values() if n > 1)
c = Checker("Q190 · Find exact duplicate rows", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.duplicate_rows(path)
c.check("rows come back as tuples", lambda: all(isinstance(r, tuple) for r in got) or "each row should be a tuple of strings")
c.check(f"{len(exp_rows)} distinct duplicated rows, in order of first appearance", lambda: list(got) == exp_rows or f"got {len(got)} rows; first {got[:1]}")
c.check(f"extra_copies is {exp_extra}", lambda: m.extra_copies(path) == exp_extra or f"got {m.extra_copies(path)}")
c.done()
