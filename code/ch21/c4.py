# An SVM maximizes the margin: the gap between the boundary and the
# closest points on either side. Only those points matter.
Xm, ym = make_moons(n_samples=800, noise=0.18, random_state=0)
Xc, yc = make_circles(n_samples=800, noise=0.10, factor=0.45, random_state=0)

for name, X_, y_ in [("moons", Xm, ym), ("circles", Xc, yc)]:
    print(f"{name}")
    for label, clf in [("logistic", LogisticRegression(max_iter=2000)),
                       ("linear SVM", LinearSVC(C=1.0, max_iter=20000)),
                       ("SVM, RBF kernel", SVC(C=1.0, kernel="rbf"))]:
        m = make_pipeline(StandardScaler(), clf)
        s = cross_val_score(m, X_, y_, cv=cv, scoring="accuracy")
        extra = ""
        if isinstance(clf, SVC):
            m.fit(X_, y_)
            extra = f"   support vectors {m[-1].n_support_.sum()} of {len(y_)}"
        print(f"  {label:<18}accuracy {s.mean():.4f}{extra}")
