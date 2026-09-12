cands = {
  "single tree (depth 4)": DecisionTreeClassifier(max_depth=4,
                                                 random_state=0),
  "bagged trees":          BaggingClassifier(n_estimators=300,
                                             random_state=0),
  "random forest":         RandomForestClassifier(n_estimators=300,
                                                  min_samples_leaf=5,
                                                  random_state=0),
  "gradient boosting":     GradientBoostingClassifier(n_estimators=200,
                                                      learning_rate=0.05,
                                                      max_depth=3,
                                                      random_state=0),
  "logistic regression":   make_pipeline(StandardScaler(),
                                         LogisticRegression(max_iter=1000)),
}
print(f"{'model':<24}{'CV AUC':>9}{'sd':>8}{'test AUC':>11}")
for name, m in cands.items():
    s = cross_val_score(m, Xtr, ytr, cv=cv, scoring="roc_auc")
    m.fit(Xtr, ytr)
    te = roc_auc_score(yte, m.predict_proba(Xte)[:, 1])
    print(f"{name:<24}{s.mean():>9.4f}{s.std():>8.4f}{te:>11.4f}")
