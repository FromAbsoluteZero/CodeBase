import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("transactions.csv"))
exp = pd.DataFrame({"transactions": df.groupby("Hour").size(), "fraud_rate": df.groupby("Hour").Fraud.mean()})
c = Checker("Q207 · Fraud rate by hour", which_file(HERE, ".py"))
m = load_module(c.target)
c.check(f"base_rate = {df.Fraud.mean():.5f}", lambda: close(m.base_rate(df), df.Fraud.mean(), 1e-9))
got = m.fraud_rate_by_hour(df)
c.check("24 hours, columns transactions and fraud_rate", lambda: len(got) == 24 and list(got.columns) == ["transactions", "fraud_rate"] or f"{len(got)} rows, columns {list(got.columns)}")
c.check("counts and rates match", lambda: list(got.transactions) == list(exp.transactions) and np.allclose(got.fraud_rate, exp.fraud_rate))
c.check(f"riskiest hour is {int(exp.fraud_rate.idxmax())}", lambda: int(m.riskiest_hour(df)) == int(exp.fraud_rate.idxmax()) or f"got {m.riskiest_hour(df)}")
c.done()
