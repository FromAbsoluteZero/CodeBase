# The forward pass through a real two-layer network, on one digit.
D_in, H, D_out = 64, 32, 10
r3 = np.random.default_rng(30)
W1 = r3.normal(0, np.sqrt(2/D_in), (D_in, H))    # He initialization
b1 = np.zeros(H)
W2 = r3.normal(0, np.sqrt(2/H), (H, D_out))
b2 = np.zeros(D_out)

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)          # overflow guard
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

def forward(Xb):
    z1 = Xb @ W1 + b1
    a1 = np.maximum(0, z1)                         # ReLU
    z2 = a1 @ W2 + b2
    p = softmax(z2)
    return z1, a1, z2, p

x = X[:1]
z1, a1, z2, p = forward(x)
print(f"input           {x.shape}")
print(f"after layer 1   {a1.shape}   ({(a1 > 0).sum()} of {H} neurons fired)")
print(f"after layer 2   {z2.shape}")
print(f"after softmax   {p.shape}   sums to {p.sum():.6f}")
print(f"\npredicted digit: {p.argmax()}   true label: {y[:1][0]}")
print(f"confidence in that digit: {p.max():.3f}")
