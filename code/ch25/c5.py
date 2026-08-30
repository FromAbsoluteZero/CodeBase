# The honest final report: tune on training, estimate honestly, then
# open the test set exactly once.
from sklearn.metrics import roc_auc_score
Xtr, Xte, ytr, yte = train_test_split(df, y, test_size=0.3,
                                      random_state=0, stratify=y)

space = {"clf__learning_rate": loguniform(1e-3, 3e-1),
         "clf__max_depth": randint(2, 9),
         "clf__max_iter": randint(60, 400),
         "clf__l2_regularization": loguniform(1e-3, 1e1)}
search = RandomizedSearchCV(base_pipe(HistGradientBoostingClassifier(
                                random_state=0)),
                            space, n_iter=40, cv=cv, scoring="roc_auc",
                            random_state=0, n_jobs=-1)
search.fit(Xtr, ytr)

nested = cross_val_score(search, Xtr, ytr,
                         cv=StratifiedKFold(4, shuffle=True, random_state=1),
                         scoring="roc_auc", n_jobs=-1).mean()
test = roc_auc_score(yte, search.predict_proba(Xte)[:, 1])
baseline = cross_val_score(base_pipe(LogisticRegression(max_iter=4000)),
                           Xtr, ytr, cv=cv, scoring="roc_auc").mean()

print(f"untuned logistic baseline (CV)  {baseline:.4f}")
print(f"tuned inner CV score            {search.best_score_:.4f}")
print(f"nested CV estimate              {nested:.4f}")
print(f"test set, opened once           {test:.4f}")
print(f"\ntuning bought {search.best_score_ - baseline:+.4f} on the inner score")
print(f"and {nested - baseline:+.4f} once measured honestly")
