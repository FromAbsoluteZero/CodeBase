import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
mask = ((df.Category == "Beans") & (df.Quantity >= 10)) | (df.Country == "France")
c = Checker("Q200 · Filter with & and |", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.bulk_beans_or_france(df)
c.check(f"{int(mask.sum())} rows selected", lambda: len(got) == int(mask.sum()) or f"got {len(got)}")
c.check("exactly the right rows, in order", lambda: list(got.index) == list(df.index[mask]))
c.check("no other rows slipped in", lambda: bool(((got.Category == 'Beans') & (got.Quantity >= 10) | (got.Country == 'France')).all()))
c.done()
