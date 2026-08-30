# Grid search: every combination, exhaustively.
grid = {"clf__C": [0.01, 0.1, 1, 10, 100],
        "clf__penalty": ["l1", "l2"]}
gs = GridSearchCV(base_pipe(LogisticRegression(max_iter=4000,
                            solver="liblinear")),
                  grid, cv=cv, scoring="roc_auc", n_jobs=-1)
gs.fit(df, y)
print(f"fits: 10 combinations x 5 folds = 50")
print(f"best params: {gs.best_params_}")
print(f"best CV AUC: {gs.best_score_:.4f}")

r = pd.DataFrame(gs.cv_results_).nlargest(4, "mean_test_score")
print(f"\n{'C':>8}{'penalty':>9}{'mean':>9}{'sd':>8}")
for _, row in r.iterrows():
    print(f"{row['param_clf__C']:>8}{row['param_clf__penalty']:>9}"
          f"{row['mean_test_score']:>9.4f}{row['std_test_score']:>8.4f}")
