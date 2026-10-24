# k trades bias against variance, exactly as Chapter 17 described.
print(f"{'k':>5}{'train AUC':>12}{'CV AUC':>10}{'sd':>8}")
Xtr, Xte, ytr, yte = train_test_split(df, y, test_size=0.3,
                                      random_state=0, stratify=y)
for k in (1, 5, 15, 35, 75, 200):
    m = pipe(KNeighborsClassifier(k)).fit(Xtr, ytr)
    tr = roc_auc_score(ytr, m.predict_proba(Xtr)[:, 1])
    s = cross_val_score(pipe(KNeighborsClassifier(k)), Xtr, ytr,
                        cv=cv, scoring="roc_auc")
    print(f"{k:>5}{tr:>12.4f}{s.mean():>10.4f}{s.std():>8.4f}")
