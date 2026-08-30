# He initialization scales each layer's weights by the width it is
# fanning out from, so variance neither grows nor shrinks layer to layer.
Ws_he = he_init(sizes, seed=31)
a = X[:200]

print(f"{'layer':>7}{'mean |activation|':>20}{'fraction alive':>16}")
print(f"{'input':>7}{np.abs(a).mean():>20.4f}{'--':>16}")
for i, W in enumerate(Ws_he, 1):
    a = np.maximum(0, a @ W)
    alive = (a > 0).mean()
    print(f"{i:>7}{np.abs(a).mean():>20.4f}{alive:>16.4f}")

print(f"\nwhy sqrt(2/fan_in): each output is a sum of fan_in terms, each")
print(f"roughly variance 1 * weight_variance. Setting weight_variance to")
print(f"2/fan_in keeps the sum's variance near 1, and the factor of 2")
print(f"accounts for ReLU discarding half the signal on average.")
