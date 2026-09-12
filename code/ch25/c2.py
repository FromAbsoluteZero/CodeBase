# Random search covers a wider space for the same budget, and samples
# continuous parameters on the scale they actually vary on.
space = {"clf__learning_rate": loguniform(1e-3, 3e-1),
         "clf__max_depth": randint(2, 9),
         "clf__max_iter": randint(60, 400),
         "clf__l2_regularization": loguniform(1e-3, 1e1)}
rs = RandomizedSearchCV(base_pipe(HistGradientBoostingClassifier(
                            random_state=0)),
                        space, n_iter=30, cv=cv, scoring="roc_auc",
                        random_state=0, n_jobs=-1)
rs.fit(df, y)
print(f"30 samples x 5 folds = 150 fits")
for k, v in rs.best_params_.items():
    print(f"  {k.replace('clf__',''):<20} "
          f"{v if isinstance(v, int) else round(v, 5)}")
print(f"best CV AUC: {rs.best_score_:.4f}")

r = pd.DataFrame(rs.cv_results_).nlargest(5, "mean_test_score")
print(f"\ntop five of thirty, mean +/- sd")
for _, row in r.iterrows():
    print(f"  {row['mean_test_score']:.4f} +/- {row['std_test_score']:.4f}")
