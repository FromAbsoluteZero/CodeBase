# The same overfit model, rescued by a penalty instead of less capacity.
X = rng.uniform(-3, 3, size=(30, 1))
y = np.sin(1.4 * X[:, 0]) + 0.3 * X[:, 0] + rng.normal(0, 0.45, 30)
cv = KFold(5, shuffle=True, random_state=0)

print(f"{'alpha':>9}{'train MSE':>11}{'val MSE':>10}{'largest |w|':>13}")
for a in [0.0, 1e-4, 1e-2, 1e-1, 1.0, 10.0, 100.0]:
    m = make_pipeline(PolynomialFeatures(14), StandardScaler(),
                      Ridge(alpha=a) if a else LinearRegression())
    val = -cross_val_score(m, X, y, cv=cv,
                           scoring="neg_mean_squared_error").mean()
    m.fit(X, y)
    tr = ((y - m.predict(X)) ** 2).mean()
    w = np.abs(m[-1].coef_).max()
    print(f"{a:>9.4f}{tr:>11.3f}{val:>10.3f}{w:>13.1f}")
