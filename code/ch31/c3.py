# Sigmoid saturates: its gradient is near zero almost everywhere except
# a narrow band around zero. Stack layers of it and the gradient reaching
# the earliest layers vanishes, however good the initialization is.
def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

def sigmoid_grad(z):
    s = sigmoid(z)
    return s * (1 - s)

Ws_s = he_init(sizes, seed=31)
a = X[:200]
zs = []
for W in Ws_s:
    z = a @ W
    zs.append(z)
    a = sigmoid(z)

print(f"{'layer':>7}{'max sigmoid grad':>18}{'slopes only':>13}"
      f"{'through weights':>17}")
signal = 1.0
g = np.ones_like(zs[-1])            # a gradient of 1.0 at every output unit
for i, (z, W) in enumerate(zip(reversed(zs), reversed(Ws_s)), 1):
    gmax = sigmoid_grad(z).max()
    signal *= gmax
    g = (g * sigmoid_grad(z)) @ W.T     # the real backward pass, weights too
    print(f"{i:>7}{gmax:>18.4f}{signal:>13.2e}{np.abs(g).mean():>17.2e}")
print(f"\nafter {len(zs)} layers, the slopes alone shrink a gradient by")
print(f"{signal:.2e}; through this network's weights it arrives at")
print(f"{np.abs(g).mean():.2e} of its size at the output.")
