pipe = Pipeline([("scale", StandardScaler()),
                 ("model", LogisticRegression(max_iter=1000))])
best_depth = 4
cands = {"tree (depth 4)": DecisionTreeClassifier(max_depth=best_depth,
                                                 random_state=0),
         "logistic":       pipe}
for name, m in cands.items():
    s = cross_val_score(m, Xtr, ytr, cv=cv, scoring="roc_auc")
    print(f"{name:<16} CV AUC {s.mean():.4f} +/- {s.std():.4f}")
