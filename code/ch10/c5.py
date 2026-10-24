g0 = 2 * err.mean()
g1 = 2 * (err * xz).mean()
print(f"gradient for b0: {g0:,.2f}")
print(f"gradient for b1: {g1:,.2f}")

eta = 0.1
b0 -= eta * g0
b1 -= eta * g1
print(f"\nafter one step: b0={b0:.3f}, b1={b1:.3f}")
new_err = (b0 + b1 * xz) - y
print(f"loss: {(err**2).mean():,.1f} -> {(new_err**2).mean():,.1f}")
