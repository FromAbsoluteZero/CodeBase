import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(data_path("customers.csv"))
X = pd.DataFrame({"AnnualIncome": df.AnnualIncome, "Sessions": df.Sessions, "AvgBasket": df.AvgBasket, "SignupAge": (pd.Timestamp("2024-12-31") - pd.to_datetime(df.SignupDate)).dt.days})
y = df.Churn; folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
honest = cross_val_score(make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=1000)), X, y, cv=folds, scoring="roc_auc").mean()
leaky = cross_val_score(LogisticRegression(max_iter=1000), make_pipeline(SimpleImputer(strategy="median"), StandardScaler()).fit_transform(X), y, cv=folds, scoring="roc_auc").mean()
exp = {"honest_auc": honest, "leaky_auc": leaky, "gap": leaky - honest}
c = Checker("Q223 · Leakage in preprocessing, measured", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.leakage_comparison(df)
for k, v in exp.items():
    c.check(f"{k} = {v:+.5f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 1e-4) or f"got {got.get(k)!r}")
c.done()
