# A tree left alone memorizes. Pruning is not optional.
print(f"{'setting':<26}{'leaves':>8}{'train':>9}{'CV AUC':>9}{'sd':>8}")
settings = [("unlimited", {}),
            ("max_depth=3", {"max_depth": 3}),
            ("max_depth=4", {"max_depth": 4}),
            ("min_samples_leaf=20", {"min_samples_leaf": 20}),
            ("min_samples_leaf=50", {"min_samples_leaf": 50}),
            ("ccp_alpha=0.002", {"ccp_alpha": 0.002})]
for name, kw in settings:
    m = DecisionTreeClassifier(random_state=0, **kw).fit(Xtr, ytr)
    s = cross_val_score(DecisionTreeClassifier(random_state=0, **kw),
                        Xtr, ytr, cv=cv, scoring="roc_auc")
    tr = roc_auc_score(ytr, m.predict_proba(Xtr)[:, 1])
    print(f"{name:<26}{m.get_n_leaves():>8}{tr:>9.4f}"
          f"{s.mean():>9.4f}{s.std():>8.4f}")
