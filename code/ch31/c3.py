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

print(f"{'layer':>7}{'max sigmoid grad':>18}{'backward signal':>18}")
signal = 1.0
for i, z in enumerate(reversed(zs), 1):
    g = sigmoid_grad(z).max()
    signal *= g
    print(f"{i:>7}{g:>18.4f}{signal:>18.2e}")
print(f"\nafter {len(zs)} layers, a gradient of 1.0 at the output has")
print(f"shrunk by this factor before it reaches the first layer.")
