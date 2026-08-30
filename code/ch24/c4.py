# Constructed features: a ratio the model cannot form on its own, and
# dates turned into something a model can use.
def add_features(d):
    d = d.copy()
    d["TenureDays"] = (pd.Timestamp("2025-01-01") - d["SignupDate"]).dt.days
    d["SignupMonth"] = d["SignupDate"].dt.month
    d["BasketPerIncome"] = d["AvgBasket"] / (d["AnnualIncome"] / 1000)
    d["SessionsPerMonth"] = d["Sessions"] / (d["TenureDays"] / 30 + 1)
    return d.drop(columns=["SignupDate", "City"])

NUM2 = NUM + ["TenureDays", "SignupMonth", "BasketPerIncome",
              "SessionsPerMonth"]

def build(cols):
    num = Pipeline([("imp", SimpleImputer(strategy="median")),
                    ("sc", StandardScaler())])
    return Pipeline([("pre", ColumnTransformer([
                        ("n", num, cols),
                        ("c", OneHotEncoder(handle_unknown="ignore"), LOWCARD)])),
                     ("clf", LogisticRegression(max_iter=2000))])

d2 = add_features(df)
base = cross_val_score(build(NUM), d2, y, cv=cv, scoring="roc_auc")
full = cross_val_score(build(NUM2), d2, y, cv=cv, scoring="roc_auc")
print(f"raw columns only          AUC {base.mean():.4f} +/- {base.std():.4f}")
print(f"with constructed features AUC {full.mean():.4f} +/- {full.std():.4f}")
print(f"gain {full.mean() - base.mean():+.4f}")
