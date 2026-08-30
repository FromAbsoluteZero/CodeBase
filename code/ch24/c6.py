# What happens in production when a category appears that training never saw.
Xtr, Xte, ytr, yte = train_test_split(df, y, test_size=0.3,
                                      random_state=0, stratify=y)
Xte = Xte.copy()
Xte.loc[Xte.index[:40], "Channel"] = "kiosk"      # a new channel launches

num = Pipeline([("imp", SimpleImputer(strategy="median")),
                ("sc", StandardScaler())])
for policy in ("error", "ignore"):
    enc = OneHotEncoder(handle_unknown=policy)
    p = Pipeline([("pre", ColumnTransformer([("n", num, NUM),
                                             ("c", enc, LOWCARD)])),
                  ("clf", LogisticRegression(max_iter=2000))]).fit(Xtr, ytr)
    try:
        pred = p.predict_proba(Xte)[:, 1]
        print(f"handle_unknown='{policy}': scored "
              f"{len(pred):,} rows without error")
    except Exception as e:
        print(f"handle_unknown='{policy}': {type(e).__name__} -- "
              f"{str(e).splitlines()[0][:60]}")
