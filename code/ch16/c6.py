pipe = Pipeline([("scale", StandardScaler()),
                 ("model", LogisticRegression(max_iter=1000))])
p_test = pipe.fit(Xtr, ytr).predict_proba(Xte)[:, 1]

budget = 60
order = np.argsort(p_test)[::-1][:budget]
caught = yte[order].sum()
expected = budget * yte.mean()
print(f"AUC {roc_auc_score(yte, p_test):.3f} on {len(yte)} held-out employees")
print(f"calling the top {budget}: finds {caught} of {yte.sum()} leavers")
print(f"random {budget}: would find {expected:.1f}")
print(f"lift: {caught/expected:.1f}x")
