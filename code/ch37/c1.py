import numpy as np
rng = np.random.default_rng(3)

# Eight candidate replies a small model might give to one prompt.
replies = ["refuses politely", "answers briefly", "answers with detail",
           "answers with sources", "hedges vaguely", "rambles at length",
           "flatters the user", "answers, then flatters"]

# What people actually want. The model never sees this.
true_utility = np.array([0.1, 1.4, 2.1, 2.6, -0.4, -0.9, -1.2, 1.0])

# The pretrained model, before any alignment: fluent, not helpful.
logits_ref = np.array([0.4, 0.3, 0.2, -0.6, 0.9, 1.1, 0.7, 0.1])
softmax = lambda z: np.exp(z - z.max()) / np.exp(z - z.max()).sum()
pi_ref = softmax(logits_ref)

print(f"{'reply':<24}{'true utility':>13}{'pretrained p':>14}")
for r, u, p in zip(replies, true_utility, pi_ref):
    print(f"  {r:<22}{u:>+13.1f}{p:>14.3f}")
print(f"\nexpected utility of the pretrained model: "
      f"{pi_ref @ true_utility:+.3f}")
