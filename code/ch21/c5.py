# C and gamma both control complexity, and they interact. C sets how much
# margin violation is tolerated; gamma sets how far one point's influence
# reaches. Large values of either overfit.
Xm, ym = make_moons(n_samples=600, noise=0.28, random_state=0)
print(f"{'gamma':>8}" + "".join(f"{'C='+str(c):>10}" for c in
                                (0.1, 1, 10, 100)))
for g in (0.1, 1.0, 10.0, 100.0):
    row = ""
    for C in (0.1, 1, 10, 100):
        s = cross_val_score(make_pipeline(StandardScaler(),
                            SVC(C=C, gamma=g)), Xm, ym, cv=cv,
                            scoring="accuracy").mean()
        row += f"{s:>10.4f}"
    print(f"{g:>8.1f}{row}")
print("\nbest cell is the one to use; the corners show both failure modes.")
