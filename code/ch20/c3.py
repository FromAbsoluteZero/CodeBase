# A random forest is bagging plus one more idea: at every split, consider
# only a random subset of features. That is what decorrelates the trees.
def bag(n_trees, max_features=None, seed=0):
    r = np.random.default_rng(seed)
    preds = np.zeros((n_trees, len(Xte)))
    for i in range(n_trees):
        idx = r.integers(0, len(Xtr), len(Xtr))
        t = DecisionTreeClassifier(max_features=max_features,
                                   random_state=i)
        t.fit(Xtr.values[idx], ytr[idx])
        preds[i] = t.predict_proba(Xte.values)[:, 1]
    return preds

print(f"{'features per split':>20}{'AUC':>9}{'mean pairwise corr':>21}")
for mf, label in [(None, "all 8"), (4, "4"), (3, "sqrt(8) ~ 3"), (2, "2")]:
    p = bag(200, max_features=mf)
    corr = np.corrcoef(p)[np.triu_indices(200, 1)].mean()
    print(f"{label:>20}{roc_auc_score(yte, p.mean(0)):>9.4f}{corr:>21.3f}")
