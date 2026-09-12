# Show a labeller two replies; they pick one. Bradley-Terry says the
# probability of picking A over B is the logistic of the utility gap.
N = 4000
a = rng.integers(0, 8, N)
b = rng.integers(0, 8, N)
keep = a != b
a, b = a[keep], b[keep]
gap = true_utility[a] - true_utility[b]
a_wins = rng.random(len(a)) < 1 / (1 + np.exp(-gap))

print(f"{len(a):,} preference pairs collected")
print(f"labeller picked A {a_wins.mean():.1%} of the time")

# A worked example of one pair
i = 0
print(f"\n  A = {replies[a[i]]!r}  vs  B = {replies[b[i]]!r}")
print(f"  true gap {gap[i]:+.1f}  ->  P(A preferred) "
      f"{1/(1+np.exp(-gap[i])):.3f}  ->  labeller chose "
      f"{'A' if a_wins[i] else 'B'}")
