contrib = X * w                # each feature's contribution
share = contrib.sum(axis=0) / contrib.sum()
for name, s in zip(cust.columns[:3], share):
    print(f"  {name:<8} contributes {s:.1%} of total score")
