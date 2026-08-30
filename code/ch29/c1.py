import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"), drop_first=True)
y = hr["Attrition"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                      random_state=0, stratify=y)

rf = RandomForestClassifier(n_estimators=400, min_samples_leaf=8,
                            random_state=0).fit(Xtr, ytr)
print(f"columns: {list(X.columns)}")
print(f"test ROC AUC: {roc_auc_score(yte, rf.predict_proba(Xte)[:, 1]):.3f}")
