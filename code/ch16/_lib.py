import pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import (train_test_split, cross_val_score,
                                     StratifiedKFold, GroupKFold)
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"),
                   columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3,
                                      random_state=7, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
