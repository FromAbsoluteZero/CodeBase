import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("daily_revenue.csv"))
s = df.set_index(pd.to_datetime(df.Date)).Revenue
exp = s.resample("W").mean()
c = Checker("Q205 · Weekly resample", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.weekly_mean(df)
c.check(f"{len(exp)} weekly bins", lambda: len(got) == len(exp) or f"got {len(got)}")
c.check("indexed by week-ending date (Sundays)", lambda: got.index.equals(exp.index) or "index differs; use resample('W') on a DatetimeIndex")
c.check("weekly means match", lambda: np.allclose(got.values, exp.values))
bw = m.best_week(df)
c.check(f"best week ends {exp.idxmax().date()} at {exp.max():.2f}", lambda: pd.Timestamp(bw[0]) == exp.idxmax() and close(bw[1], exp.max()))
c.done()
