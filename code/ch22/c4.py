# A score that ranks well need not be a probability you can trust.
lr = make_pipeline(StandardScaler(),
                   LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
gb = HistGradientBoostingClassifier(random_state=0).fit(Xtr, ytr)

for name, mdl in [("logistic", lr), ("gradient boosting", gb)]:
    p = mdl.predict_proba(Xte)[:, 1]
    print(f"{name:<20} AUC {roc_auc_score(yte, p):.4f}   "
          f"Brier {brier_score_loss(yte, p):.6f}   "
          f"mean predicted {p.mean():.5f}  actual {yte.mean():.5f}")

print(f"\ncalibration of the boosted model, by decile of predicted risk")
p = gb.predict_proba(Xte)[:, 1]
order = np.argsort(p)
print(f"{'bucket':>7}{'predicted':>12}{'actual':>10}{'n':>8}")
for b in range(10):
    idx = order[b*len(p)//10:(b+1)*len(p)//10]
    print(f"{b+1:>7}{p[idx].mean():>12.5f}{yte[idx].mean():>10.5f}{len(idx):>8}")
