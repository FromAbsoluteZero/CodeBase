Xo, yo = o[feats].values, o["rev"].values
cv = KFold(5, shuffle=True, random_state=0)

def run(model):
    m = make_pipeline(StandardScaler(), model)
    mse = -cross_val_score(m, Xo, yo, cv=cv,
                           scoring="neg_mean_squared_error").mean()
    m.fit(Xo, yo)
    return mse, m[-1].coef_

print(f"{'model':<18}{'CV MSE':>10}{'non-zero':>10}")
for name, mdl in [("plain", LinearRegression()),
                  ("ridge  (a=10)", Ridge(alpha=10)),
                  ("lasso  (a=1)", Lasso(alpha=1.0, max_iter=50000)),
                  ("lasso  (a=5)", Lasso(alpha=5.0, max_iter=50000))]:
    mse, w = run(mdl)
    print(f"{name:<18}{mse:>10.1f}{int((np.abs(w) > 1e-6).sum()):>10}")

print()
_, w_ridge = run(Ridge(alpha=10))
_, w_lasso = run(Lasso(alpha=5.0, max_iter=50000))
print(f"{'feature':<12}{'ridge':>9}{'lasso':>9}")
for f, a, b in zip(feats, w_ridge, w_lasso):
    print(f"{f:<12}{a:>9.1f}{b:>9.1f}")
