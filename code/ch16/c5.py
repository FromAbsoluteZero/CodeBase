pipe = Pipeline([("scale", StandardScaler()),
                 ("model", LogisticRegression(max_iter=1000))])
final = pipe.fit(Xtr, ytr)
p_test = final.predict_proba(Xte)[:, 1]

cv_est = cross_val_score(pipe, Xtr, ytr, cv=cv, scoring="roc_auc").mean()
tree = DecisionTreeClassifier(max_depth=4, random_state=0).fit(Xtr, ytr)
print(f"cross-validated estimate: {cv_est:.4f}")
print(f"test set result:          {roc_auc_score(yte, p_test):.4f}")
print(f"(the tree, for reference: "
      f"{roc_auc_score(yte, tree.predict_proba(Xte)[:, 1]):.4f})")
