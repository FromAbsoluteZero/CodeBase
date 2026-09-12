# The tuned score is the maximum of many noisy estimates, so it is biased
# upward -- and the bias grows with how many candidates you try.
X, yy = make_classification(n_samples=600, n_features=20, n_informative=6,
                            flip_y=0.15, random_state=0)
space = {"learning_rate": loguniform(1e-3, 3e-1),
         "max_depth": randint(2, 8), "max_iter": randint(60, 300),
         "l2_regularization": loguniform(1e-3, 1e1)}
outer = StratifiedKFold(4, shuffle=True, random_state=0)

print(f"{'candidates':>11}{'inner (tuned)':>15}{'nested (honest)':>17}"
      f"{'optimism':>10}")
for n_iter in (5, 20, 60):
    s = RandomizedSearchCV(HistGradientBoostingClassifier(random_state=0),
                           space, n_iter=n_iter, cv=3, random_state=0,
                           n_jobs=-1)
    s.fit(X, yy)
    nested = cross_val_score(s, X, yy, cv=outer, n_jobs=-1).mean()
    print(f"{n_iter:>11}{s.best_score_:>15.4f}{nested:>17.4f}"
          f"{s.best_score_ - nested:>+10.4f}")
