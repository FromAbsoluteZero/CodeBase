# Fit a reward model: one number per reply, learned only from the choices.
r = np.zeros(8)
for step in range(4000):
    p_a = 1 / (1 + np.exp(-(r[a] - r[b])))       # model's P(A preferred)
    err = a_wins - p_a                            # gradient of log-likelihood
    g = np.zeros(8)
    np.add.at(g, a, -err)
    np.add.at(g, b,  err)
    r -= 0.05 * g / len(a)

r = r - r.mean()                                  # only gaps are identified
truth = true_utility - true_utility.mean()

print(f"{'reply':<24}{'learned r':>11}{'true':>9}")
for name, rr, tt in zip(replies, r, truth):
    print(f"  {name:<22}{rr:>+11.2f}{tt:>+9.2f}")
print(f"\ncorrelation with truth: {np.corrcoef(r, truth)[0,1]:.3f}")
