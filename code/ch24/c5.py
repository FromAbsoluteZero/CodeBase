# Whether a constructed feature helps depends on the model that gets it.
# The churn rule contains a threshold on basket-to-income, which a linear
# model can only approximate and a tree can express exactly.
def add_features(d):
    d = d.copy()
    d["TenureDays"] = (pd.Timestamp("2025-01-01") - d["SignupDate"]).dt.days
    d["SignupMonth"] = d["SignupDate"].dt.month
    d["BasketPerIncome"] = d["AvgBasket"] / (d["AnnualIncome"] / 1000)
    d["SessionsPerMonth"] = d["Sessions"] / (d["TenureDays"] / 30 + 1)
    return d.drop(columns=["SignupDate", "City"])

NUM2 = NUM + ["TenureDays", "SignupMonth", "BasketPerIncome",
              "SessionsPerMonth"]
d2 = add_features(df)

def build(cols, clf):
    num = Pipeline([("imp", SimpleImputer(strategy="median")),
                    ("sc", StandardScaler())])
    return Pipeline([("pre", ColumnTransformer([
                        ("n", num, cols),
                        ("c", OneHotEncoder(handle_unknown="ignore"), LOWCARD)])),
                     ("clf", clf)])

print(f"{'model':<22}{'raw':>9}{'engineered':>13}{'gain':>9}")
for name, clf in [("logistic regression", LogisticRegression(max_iter=2000)),
                  ("gradient boosting",
                   HistGradientBoostingClassifier(random_state=0))]:
    a = cross_val_score(build(NUM, clf), d2, y, cv=cv,
                        scoring="roc_auc").mean()
    b = cross_val_score(build(NUM2, clf), d2, y, cv=cv,
                        scoring="roc_auc").mean()
    print(f"{name:<22}{a:>9.4f}{b:>13.4f}{b-a:>+9.4f}")
