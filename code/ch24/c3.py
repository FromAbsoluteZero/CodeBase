# Target encoding replaces a category with the mean outcome for that
# category. Done naively it hands the model the answer.
Xtr, Xte, ytr, yte = train_test_split(df, y, test_size=0.3,
                                      random_state=0, stratify=y)

# WRONG: compute the means on all training rows, then use them as a feature
means = pd.Series(ytr, index=Xtr.index).groupby(Xtr["City"]).mean()
tr_naive = Xtr["City"].map(means).values
te_naive = Xte["City"].map(means).fillna(ytr.mean()).values

from sklearn.metrics import roc_auc_score
m = LogisticRegression(max_iter=2000).fit(tr_naive.reshape(-1, 1), ytr)
print("naive target encoding, City alone:")
print(f"  AUC on the training rows: "
      f"{roc_auc_score(ytr, m.predict_proba(tr_naive.reshape(-1,1))[:,1]):.4f}")
print(f"  AUC on held-out rows:     "
      f"{roc_auc_score(yte, m.predict_proba(te_naive.reshape(-1,1))[:,1]):.4f}")

# RIGHT: sklearn's TargetEncoder cross-fits internally
te = TargetEncoder(random_state=0)
tr_cf = te.fit_transform(Xtr[["City"]], ytr)
te_cf = te.transform(Xte[["City"]])
m2 = LogisticRegression(max_iter=2000).fit(tr_cf, ytr)
print("cross-fitted target encoding, City alone:")
print(f"  AUC on the training rows: "
      f"{roc_auc_score(ytr, m2.predict_proba(tr_cf)[:,1]):.4f}")
print(f"  AUC on held-out rows:     "
      f"{roc_auc_score(yte, m2.predict_proba(te_cf)[:,1]):.4f}")
print(f"\nreminder: City was generated independently of churn.")
