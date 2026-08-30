# PCA is fitted on data, so it leaks like any other transformation.
Xtr, Xte, ytr, yte = train_test_split(Xd, yd, test_size=0.3,
                                      random_state=0, stratify=yd)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

# WRONG: reduce everything first, then split and cross-validate
Xall = PCA(n_components=20, random_state=0).fit_transform(
           StandardScaler().fit_transform(Xd))
wrong = cross_val_score(LogisticRegression(max_iter=5000),
                        Xall, yd, cv=cv).mean()

# RIGHT: PCA inside the pipeline, refitted in every fold
right = cross_val_score(make_pipeline(StandardScaler(),
                        PCA(n_components=20, random_state=0),
                        LogisticRegression(max_iter=5000)),
                        Xd, yd, cv=cv).mean()
print(f"PCA fitted on all data first (WRONG): {wrong:.4f}")
print(f"PCA inside the pipeline     (right): {right:.4f}")
print(f"difference: {wrong - right:+.4f}")
print("\nthe gap is inside the noise, because PCA never sees y.")
print("compare: target encoding fitted the same way (Chapter 24)")
print("inflated training AUC, and SMOTE (Chapter 23) inflated 9x.")
print("how much a transformation leaks depends on whether it")
print("uses the target.")
