# Precision at fixed capacity: the metric an operations team actually has.
m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]
order = np.argsort(-p)

print(f"{'reviewed':>9}{'caught':>8}{'precision':>11}{'recall':>9}{'lift':>8}")
for k in (50, 100, 250, 500, 1000, 2000):
    top = order[:k]
    prec = yte[top].mean()
    print(f"{k:>9}{yte[top].sum():>8}{prec:>11.1%}"
          f"{yte[top].sum()/yte.sum():>9.1%}{prec/yte.mean():>7.0f}x")
