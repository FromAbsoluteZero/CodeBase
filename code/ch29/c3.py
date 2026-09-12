from sklearn.inspection import permutation_importance

r = permutation_importance(rf, Xte, yte, n_repeats=30,
                           random_state=0, scoring="roc_auc")
perm = pd.Series(r.importances_mean,
                 index=X.columns).sort_values(ascending=False)

print("permutation importance, measured on held-out data")
for k in perm.index:
    sd = r.importances_std[list(X.columns).index(k)]
    print(f"  {k:<22} {perm[k]:>+.4f}  (sd {sd:.4f})")
