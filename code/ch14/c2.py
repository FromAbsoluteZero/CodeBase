import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"),
                   columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.3, random_state=7, stratify=y)

sc = StandardScaler().fit(Xtr)          # fitted on TRAIN only
model = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)

print(f"{'feature':<24}{'coef':>9}{'odds ratio':>13}")
for nm, c in sorted(zip(X.columns, model.coef_[0]),
                    key=lambda t: -abs(t[1])):
    print(f"{nm:<24}{c:>+9.3f}{np.exp(c):>13.3f}")
