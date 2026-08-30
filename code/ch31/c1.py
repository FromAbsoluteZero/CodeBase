# Stack many layers with the naive initialization every tutorial starts
# with: weights drawn from a standard normal. Watch what happens to the
# signal as it passes through, before any training at all.
sizes = [64] + [64] * 8                  # nine layers, same width throughout
Ws = naive_init(sizes, seed=31)
a = X[:200]                              # 200 digits, forward pass only

print(f"{'layer':>7}{'mean |activation|':>20}{'fraction alive':>16}")
print(f"{'input':>7}{np.abs(a).mean():>20.4f}{'--':>16}")
for i, W in enumerate(Ws, 1):
    a = np.maximum(0, a @ W)             # ReLU at every layer
    alive = (a > 0).mean()
    print(f"{i:>7}{np.abs(a).mean():>20,.1f}{alive:>16.4f}")
