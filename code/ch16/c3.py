for d in [2, 3, 4, 5, 6, 8, 12]:
    s = cross_val_score(DecisionTreeClassifier(max_depth=d, random_state=0),
                        Xtr, ytr, cv=cv, scoring="roc_auc")
    print(f"depth {d:>2}: AUC {s.mean():.4f} +/- {s.std():.4f}"
          f"   folds {np.round(s, 3)}")
