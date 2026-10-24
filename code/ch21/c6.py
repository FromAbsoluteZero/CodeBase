# What all this costs. kNN has no training time and expensive prediction;
# a kernel SVM has expensive training and scales badly with rows.
rng = np.random.default_rng(0)
print(f"{'rows':>8}{'kNN fit':>10}{'kNN predict':>13}"
      f"{'SVM fit':>10}{'SVM predict':>13}")
for n in (1000, 4000, 16000):
    X = rng.normal(size=(n, 12))
    yy = (X[:, 0] + X[:, 1] ** 2 > 1).astype(int)
    Xq = rng.normal(size=(500, 12))
    row = []
    for clf in (KNeighborsClassifier(25), SVC(kernel="rbf")):
        t0 = time.perf_counter(); clf.fit(X, yy)
        t_fit = time.perf_counter() - t0
        t0 = time.perf_counter(); clf.predict(Xq)
        t_pred = time.perf_counter() - t0
        row += [t_fit, t_pred]
    print(f"{n:>8}{row[0]*1000:>9.1f}ms{row[1]*1000:>12.1f}ms"
          f"{row[2]*1000:>9.1f}ms{row[3]*1000:>12.1f}ms")
