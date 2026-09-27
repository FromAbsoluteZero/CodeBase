t = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
leaf = t.apply(Xtr)                       # which leaf each employee lands in

rows = []
for lf in np.unique(leaf):
    m = leaf == lf
    rows.append((m.sum(), ytr[m].mean(), lf))
rows.sort(key=lambda r: -r[1])

print(f"{'leaf':>6}{'employees':>11}{'attrition':>11}{'vs base':>9}")
base = ytr.mean()
for n, p, lf in rows:
    print(f"{lf:>6}{n:>11}{p:>11.1%}{p/base:>8.1f}x")

top = rows[0]
print(f"\nhighest-risk leaf holds {top[0]} of {len(ytr)} employees "
      f"({top[0]/len(ytr):.1%})")
print(f"and {top[1]:.0%} of them left, against a {base:.1%} base rate")
