# Momentum accumulates a velocity, so consistent directions build speed
# and oscillating ones cancel. Adam also rescales each coordinate.
X, y, _ = make_problem(cond=10)      # condition number about 99

def run(kind, eta, steps=400, beta=0.9, b1=0.9, b2=0.999, eps=1e-8):
    w, v, m, s = np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2)
    hist = []
    for t in range(1, steps + 1):
        g = grad(X, y, w)
        if kind == "plain":
            w -= eta * g
        elif kind == "momentum":
            v = beta * v + g
            w -= eta * v
        else:                                   # adam
            m = b1 * m + (1 - b1) * g
            s = b2 * s + (1 - b2) * g * g
            mh, sh = m / (1 - b1**t), s / (1 - b2**t)
            w -= eta * mh / (np.sqrt(sh) + eps)
        hist.append(loss(X, y, w))
    return hist

for kind, eta in [("plain", 0.0094), ("momentum", 0.0035), ("adam", 0.10)]:
    h = run(kind, eta)
    first = next((i for i, l in enumerate(h, 1) if l < 0.11), None)
    print(f"{kind:<10} eta {eta:<7} loss<0.11 at step "
          f"{first if first else '>400':<6} final {h[-1]:.4f}")
print("\nmomentum's effective step is larger than its learning rate,")
print("so it usually wants a smaller eta than plain descent.")
