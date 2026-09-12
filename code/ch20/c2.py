# Bagging by hand: resample the rows with replacement, fit a tree on each,
# average the predicted probabilities.
def bag(n_trees, max_features=None, seed=0):
    r = np.random.default_rng(seed)
    preds = np.zeros((n_trees, len(Xte)))
    left_out = []
    for i in range(n_trees):
        idx = r.integers(0, len(Xtr), len(Xtr))       # bootstrap sample
        left_out.append(1 - len(np.unique(idx)) / len(Xtr))
        t = DecisionTreeClassifier(max_features=max_features,
                                   random_state=i)
        t.fit(Xtr.values[idx], ytr[idx])
        preds[i] = t.predict_proba(Xte.values)[:, 1]
    return preds, float(np.mean(left_out))

single = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)
p1 = single.predict_proba(Xte)[:, 1]
print(f"one unpruned tree        AUC {roc_auc_score(yte, p1):.4f}")
preds, oob = bag(200)
for k in (1, 5, 25, 200):
    print(f"bagged, {k:>3} trees        AUC "
          f"{roc_auc_score(yte, preds[:k].mean(0)):.4f}")
print(f"\neach bootstrap sample leaves out {oob:.1%} of the rows on average")
print(f"theory says 1/e = {1/np.e:.1%}   (these are the out-of-bag rows)")
