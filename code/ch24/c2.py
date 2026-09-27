# Three ways to encode a category, compared on the same folds.
def build(cat_step, cat_cols):
    num = Pipeline([("imp", SimpleImputer(strategy="median")),
                    ("sc", StandardScaler())])
    return Pipeline([
        ("pre", ColumnTransformer([("n", num, NUM),
                                   ("c", cat_step, cat_cols)],
                                  remainder="drop")),
        ("clf", LogisticRegression(max_iter=2000))])

opts = {
  "drop City entirely":  (OneHotEncoder(handle_unknown="ignore"), LOWCARD),
  "one-hot everything":  (OneHotEncoder(handle_unknown="ignore"),
                          LOWCARD + ["City"]),
  "ordinal-code City":   (OrdinalEncoder(handle_unknown="use_encoded_value",
                          unknown_value=-1), LOWCARD + ["City"]),
  "target-encode City":  (TargetEncoder(random_state=0), LOWCARD + ["City"]),
}
print(f"{'encoding':<22}{'CV AUC':>9}{'sd':>8}{'columns':>10}")
for name, (step, cols) in opts.items():
    p = build(step, cols)
    s = cross_val_score(p, df, y, cv=cv, scoring="roc_auc")
    p.fit(df, y)
    ncol = p.named_steps["pre"].transform(df).shape[1]
    print(f"{name:<22}{s.mean():>9.4f}{s.std():>8.4f}{ncol:>10}")
