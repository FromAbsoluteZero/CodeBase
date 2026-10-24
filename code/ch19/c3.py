# The criterion must match what you computed. sklearn defaults to gini.
for crit in ("entropy", "gini"):
    t = DecisionTreeClassifier(max_depth=1, criterion=crit,
                               random_state=0).fit(Xtr, ytr)
    f = Xtr.columns[t.tree_.feature[0]]
    print(f"criterion={crit:<8} root: {f} <= {t.tree_.threshold[0]:.2f}")

print()
# Gini and entropy rank splits almost identically, which is why the default
# rarely matters -- but comparing one against the other does.
def gini(p):
    return 1 - (p**2 + (1-p)**2)
def entropy(p):
    return 0.0 if p in (0.0, 1.0) else -(p*np.log2(p) + (1-p)*np.log2(1-p))
print(f"{'p':>6}{'entropy':>10}{'gini':>8}")
for p in (0.0, 0.1215, 0.25, 0.5, 0.75):
    print(f"{p:>6.4f}{entropy(p):>10.4f}{gini(p):>8.4f}")
