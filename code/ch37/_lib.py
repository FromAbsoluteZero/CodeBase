import numpy as np
rng = np.random.default_rng(3)
replies = ["refuses politely", "answers briefly", "answers with detail",
           "answers with sources", "hedges vaguely", "rambles at length",
           "flatters the user", "answers, then flatters"]
true_utility = np.array([0.1, 1.4, 2.1, 2.6, -0.4, -0.9, -1.2, 1.0])
logits_ref = np.array([0.4, 0.3, 0.2, -0.6, 0.9, 1.1, 0.7, 0.1])
softmax = lambda z: np.exp(z - z.max()) / np.exp(z - z.max()).sum()
pi_ref = softmax(logits_ref)

N = 4000
a = rng.integers(0, 8, N); b = rng.integers(0, 8, N)
keep = a != b; a, b = a[keep], b[keep]
gap = true_utility[a] - true_utility[b]
a_wins = rng.random(len(a)) < 1 / (1 + np.exp(-gap))

r = np.zeros(8)
for _ in range(4000):
    p_a = 1 / (1 + np.exp(-(r[a] - r[b])))
    err = a_wins - p_a
    g = np.zeros(8); np.add.at(g, a, -err); np.add.at(g, b, err)
    r -= 0.05 * g / len(a)
r = r - r.mean()
truth = true_utility - true_utility.mean()
