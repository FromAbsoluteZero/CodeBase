# Preprocessing choices are hyperparameters too. Tune them in the same
# search, so each option is evaluated with the folds refitted around it.
space = {
    "pre__n__imp__strategy": ["median", "mean"],
    "clf__learning_rate": loguniform(1e-3, 3e-1),
    "clf__max_depth": randint(2, 9),
    "clf__max_iter": randint(60, 400),
    "clf__l2_regularization": loguniform(1e-3, 1e1),
}
rs = RandomizedSearchCV(base_pipe(HistGradientBoostingClassifier(
                            random_state=0)),
                        space, n_iter=40, cv=cv, scoring="roc_auc",
                        random_state=0, n_jobs=-1)
rs.fit(df, y)
print(f"best CV AUC {rs.best_score_:.4f}")
print(f"imputation chosen: {rs.best_params_['pre__n__imp__strategy']}")

r = pd.DataFrame(rs.cv_results_)
print(f"\n{'imputation':>12}{'best of that option':>22}{'tried':>8}")
for s in ("median", "mean"):
    sub = r[r["param_pre__n__imp__strategy"] == s]
    print(f"{s:>12}{sub['mean_test_score'].max():>22.4f}{len(sub):>8}")
