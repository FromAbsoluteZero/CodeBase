# RLHF: raise expected reward, but stay near the pretrained model.
# The KL penalty is what stops it collapsing onto one reply.
def rlhf(beta, steps=3000, eta=0.1):
    z = logits_ref.copy()
    for _ in range(steps):
        p = softmax(z)
        # gradient of  E[r] - beta * KL(pi || pi_ref)
        adv = r - beta * (np.log(p / pi_ref) + 1)
        z += eta * p * (adv - p @ adv)
    return softmax(z)

print(f"{'beta':>6}{'KL':>8}{'model reward':>14}"
      f"{'TRUE utility':>14}   top reply")
for beta in [10.0, 2.0, 0.5, 0.1, 0.02]:
    p = rlhf(beta)
    kl = (p * np.log(p / pi_ref)).sum()
    print(f"{beta:>6.2f}{kl:>8.2f}{p @ r:>14.2f}{p @ true_utility:>14.2f}"
          f"   {replies[p.argmax()]}")
print(f"\npretrained baseline: true utility {pi_ref @ true_utility:+.2f}")
