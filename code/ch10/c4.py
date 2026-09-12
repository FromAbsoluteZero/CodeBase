b0, b1 = 0.0, 0.0
pred = b0 + b1 * xz
err = pred - y
print(f"starting weights: b0={b0}, b1={b1}")
print(f"predicting {pred[0]:.1f} for an order actually worth {y[0]:.2f}")
print(f"mean squared error: {(err**2).mean():,.1f}")
print(f"typical miss: ${np.sqrt((err**2).mean()):,.2f}")
