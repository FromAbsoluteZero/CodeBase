# A single neuron is a dot product plus a nonlinearity. Nothing more.
r = np.random.default_rng(30)
w = r.normal(size=64)
b = 0.0
x = X[0]                              # one digit, 64 pixel values

z = x @ w + b                         # the weighted sum from Chapter 9
a = max(0, z)                         # ReLU: pass positive, zero out negative

print(f"pixel vector shape: {x.shape}")
print(f"weighted sum z = {z:.3f}")
print(f"after ReLU,  a = {a:.3f}")
print(f"\nthat is the entire computation one neuron performs.")
print(f"a layer is many of these run in parallel; a network is")
print(f"layers of them run in sequence.")
