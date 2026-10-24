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

outer = StratifiedKFold(4, shuffle=True, random_state=1)
nested = cross_val_score(search, Xtr, ytr, cv=outer,
                         scoring="roc_auc", n_jobs=-1).mean()
test = roc_auc_score(yte, search.predict_proba(Xte)[:, 1])

# The same boosted pipeline at its default settings, scored on the same
# folds as each tuned number, so each difference is what tuning changed.
untuned = base_pipe(HistGradientBoostingClassifier(random_state=0))
base_inner = cross_val_score(untuned, Xtr, ytr, cv=cv,
                             scoring="roc_auc").mean()
base_outer = cross_val_score(untuned, Xtr, ytr, cv=outer,
                             scoring="roc_auc").mean()

print(f"untuned boosting, 5 inner folds  {base_inner:.4f}")
print(f"tuned, best inner CV score       {search.best_score_:.4f}")
print(f"untuned boosting, 4 outer folds  {base_outer:.4f}")
print(f"tuned, nested CV estimate        {nested:.4f}")
print(f"test set, opened once            {test:.4f}")
print(f"\ntuning bought {search.best_score_ - base_inner:+.4f} on "
      f"the inner score")
print(f"and {nested - base_outer:+.4f} once measured honestly")
