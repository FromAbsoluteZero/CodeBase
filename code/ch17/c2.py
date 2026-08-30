# The two diagnostics that tell you which problem you have.
X = rng.uniform(-3, 3, size=(30, 1))
y = (np.sin(1.4 * X[:, 0]) + 0.3 * X[:, 0]
     + rng.normal(0, 0.45, 30))
cv = KFold(5, shuffle=True, random_state=0)

print(f"{'degree':>7}{'train MSE':>11}{'val MSE':>10}   diagnosis")
for deg in [1, 3, 5, 9, 14]:
    m = make_pipeline(PolynomialFeatures(deg), StandardScaler(),
                      LinearRegression())
    val = -cross_val_score(m, X, y, cv=cv,
                           scoring="neg_mean_squared_error").mean()
    m.fit(X, y)
    tr = ((y - m.predict(X)) ** 2).mean()
    d = ("underfit (high bias)" if tr > 0.35 else
         "overfit (high variance)" if val > 2 * tr + 0.1 else "balanced")
    print(f"{deg:>7}{tr:>11.3f}{val:>10.3f}   {d}")
