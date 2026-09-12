b0, b1 = 0.0, 0.0
for step in range(200):
    err = (b0 + b1 * xz) - y
    if step in (0, 1, 3, 10, 50, 199):
        print(f"  step {step:>3}: b0={b0:>7.2f} b1={b1:>7.2f} "
              f"loss={(err**2).mean():>10,.0f}")
    b0 -= eta * 2 * err.mean()
    b1 -= eta * 2 * (err * xz).mean()
