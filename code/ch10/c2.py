def run(eta, steps):
    b0, b1 = 0.0, 0.0
    trace = []
    for i in range(steps):
        err = (b0 + b1 * xz) - y
        trace.append((err**2).mean())
        b0 -= eta * 2 * err.mean()
        b1 -= eta * 2 * (err * xz).mean()
    return trace

for eta in [0.001, 0.1, 1.2]:
    t = run(eta, 12)
    verdict = ("diverging" if t[-1] > t[0] else
               "converging" if t[-1] < t[0] * 0.5 else "crawling")
    print(f"eta={eta:<6} loss {t[0]:>12,.0f} -> {t[-1]:>14,.0f}"
          f"  {verdict}")
