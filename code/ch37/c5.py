# Labellers are human. Suppose they mildly enjoy being flattered,
# so what they REWARD is not quite what serves them.
flattery = np.array([0, 0, 0, 0, 0, 0, 1, 1])
proxy_utility = true_utility + 2.2 * flattery      # what the labels reflect

gap_p = proxy_utility[a] - proxy_utility[b]
a_wins_p = rng.random(len(a)) < 1 / (1 + np.exp(-gap_p))

r_bias = np.zeros(8)
for _ in range(4000):
    p_a = 1 / (1 + np.exp(-(r_bias[a] - r_bias[b])))
    err = a_wins_p - p_a
    g = np.zeros(8); np.add.at(g, a, -err); np.add.at(g, b, err)
    r_bias -= 0.05 * g / len(a)
r_bias -= r_bias.mean()

def rlhf(reward, beta, steps=3000, eta=0.1):
    z = logits_ref.copy()
    for _ in range(steps):
        p = softmax(z)
        adv = reward - beta * (np.log(p / pi_ref) + 1)
        z += eta * p * (adv - p @ adv)
    return softmax(z)

print(f"{'beta':>6}{'reward model score':>20}"
      f"{'TRUE utility':>14}   top reply")
for beta in [2.0, 0.5, 0.1, 0.02]:
    p = rlhf(r_bias, beta)
    print(f"{beta:>6.2f}{p @ r_bias:>20.2f}{p @ true_utility:>14.2f}"
          f"   {replies[p.argmax()]}")
