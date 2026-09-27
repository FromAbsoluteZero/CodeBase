# Does compressing cost accuracy? Fit inside a pipeline so PCA is
# refitted in every fold, exactly as Chapter 16 requires.
cv = StratifiedKFold(5, shuffle=True, random_state=0)
full = cross_val_score(make_pipeline(StandardScaler(),
                       LogisticRegression(max_iter=5000)),
                       Xd, yd, cv=cv).mean()
print(f"{'components':>11}{'accuracy':>10}{'vs all 64':>11}")
for k in (5, 10, 20, 30, 40, 64):
    m = make_pipeline(StandardScaler(), PCA(n_components=k, random_state=0),
                      LogisticRegression(max_iter=5000))
    s = cross_val_score(m, Xd, yd, cv=cv).mean()
    print(f"{k:>11}{s:>10.4f}{s - full:>+11.4f}")
print(f"\nall 64 raw pixels, no PCA: {full:.4f}")
