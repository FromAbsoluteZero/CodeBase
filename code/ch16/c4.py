from sklearn.datasets import load_breast_cancer
Xc, yc = load_breast_cancer(return_X_y=True)
k = StratifiedKFold(5, shuffle=True, random_state=0)

# WRONG: the scaler sees every row, including each fold's validation rows
leaked = StandardScaler().fit_transform(Xc)
a = cross_val_score(LogisticRegression(max_iter=5000), leaked, yc,
                    cv=k, scoring="roc_auc").mean()

# RIGHT: the pipeline refits the scaler inside every fold
clean = cross_val_score(
    Pipeline([("s", StandardScaler()),
              ("m", LogisticRegression(max_iter=5000))]),
    Xc, yc, cv=k, scoring="roc_auc").mean()

print(f"leaked {a:.4f}   clean {clean:.4f}   difference {a - clean:+.4f}")
