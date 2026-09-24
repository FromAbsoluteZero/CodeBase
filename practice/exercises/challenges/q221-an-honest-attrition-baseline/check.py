import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv(data_path("hr.csv"))
X, y = df.drop(columns="Attrition"), df.Attrition
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
cat = ["Department", "OverTime"]; num = [c for c in X.columns if c not in cat]
pipe = Pipeline([("prep", ColumnTransformer([("cat", OneHotEncoder(), cat), ("num", StandardScaler(), num)])), ("clf", LogisticRegression(max_iter=1000))]).fit(Xtr, ytr)
exp = {"majority_accuracy": (yte == ytr.mode()[0]).mean(), "model_accuracy": accuracy_score(yte, pipe.predict(Xte)), "model_auc": roc_auc_score(yte, pipe.predict_proba(Xte)[:, 1])}
c = Checker("Q221 · An honest attrition baseline", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.attrition_baseline(df)
for k, v in exp.items():
    c.check(f"{k} = {v:.4f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 2e-3) or f"got {got.get(k)!r}")
c.check("the model's AUC is well above 0.5, and accuracy is close to the majority floor", lambda: got["model_auc"] > 0.7 and abs(got["model_accuracy"] - got["majority_accuracy"]) < 0.06)
c.done()
