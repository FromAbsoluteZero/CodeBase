print(f"{'depth':>6}{'train AUC':>11}{'test AUC':>10}{'leaves':>8}")
for d in [1, 2, 3, 5, 8, 12, None]:
    t = DecisionTreeClassifier(max_depth=d, random_state=0)
    t.fit(Xtr, ytr)
    a_tr = roc_auc_score(ytr, t.predict_proba(Xtr)[:, 1])
    a_te = roc_auc_score(yte, t.predict_proba(Xte)[:, 1])
    print(f"{str(d):>6}{a_tr:>11.4f}{a_te:>10.4f}{t.get_n_leaves():>8}")
