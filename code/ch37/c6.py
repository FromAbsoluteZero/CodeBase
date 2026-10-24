# DPO: no reward model, no sampling. Train the policy straight on the pairs.
def dpo(beta, steps=6000, eta=0.5):
    z = logits_ref.copy()
    win  = np.where(a_wins, a, b)
    lose = np.where(a_wins, b, a)
    for _ in range(steps):
        p = softmax(z)
        s = np.log(p / pi_ref)             # implicit reward, up to beta
        margin = beta * (s[win] - s[lose])
        w = 1 / (1 + np.exp(margin))                # sigmoid of the negative
        g = np.zeros(8)
        np.add.at(g, win, -w); np.add.at(g, lose, w)
        g = beta * g / len(win)
        z -= eta * (g - p @ g)
    return softmax(z)

print(f"{'beta':>6}{'TRUE utility':>14}   top reply")
for beta in [1.0, 0.3, 0.1]:
    p = dpo(beta)
    print(f"{beta:>6.2f}{p @ true_utility:>14.2f}   {replies[p.argmax()]}")

p = dpo(0.1)
print(f"\n{'reply':<24}{'pretrained':>12}{'after DPO':>11}")
for name, q0, q1 in zip(replies, pi_ref, p):
    print(f"  {name:<22}{q0:>12.3f}{q1:>11.3f}")
