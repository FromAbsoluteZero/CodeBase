import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import roc_auc_score
# hr.csv is created by Chapter 14 (code/ch14/gen_hr.py). The blocks read it from the
# working directory exactly as the book does; if it is not here yet, use the copy shipped in
# data/generated/ (byte-identical to what the generator writes).
import os as _os, shutil as _shutil
if not _os.path.exists("hr.csv"):
    for _d in ("../../data/generated", "../data/generated", "data/generated"):
        if _os.path.exists(_os.path.join(_d, "hr.csv")):
            _shutil.copy(_os.path.join(_d, "hr.csv"), "hr.csv"); break
hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"),
                   columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3,
                                      random_state=7, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
