Z = (X - X.mean(axis=0)) / X.std(axis=0)
w2 = np.array([0.5, 0.3, 0.2])      # now these mean what they say
cust["score_z"] = Z @ w2

contrib2 = np.abs(Z * w2)
share2 = contrib2.sum(axis=0) / contrib2.sum()
for name, s in zip(cust.columns[:3], share2):
    print(f"  {name:<8} contributes {s:.1%}")
