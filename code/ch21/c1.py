# kNN has no training step. It memorizes, then measures distance at
# prediction time -- which makes scaling decisive, not merely advisable.
for label, scale in [("unscaled", False), ("standardized", True)]:
    s = cross_val_score(pipe(KNeighborsClassifier(25), scale=scale),
                        df, y, cv=cv, scoring="roc_auc")
    print(f"kNN, {label:<13} CV AUC {s.mean():.4f} +/- {s.std():.4f}")

print(f"\nwhy: the numeric columns before scaling")
for c in NUM:
    col = df[c].dropna()
    print(f"  {c:<16} sd {col.std():>10,.1f}")
