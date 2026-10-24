slope = b1 / x.std()
intercept = b0 - b1 * x.mean() / x.std()
print(f"each additional unit is worth ${slope:.2f} of revenue")
print(f"an order with no units would be ${intercept:.2f}")

final_err = (intercept + slope * x) - y
print(f"\ntypical miss now: ${np.sqrt((final_err**2).mean()):,.2f}")
start_err = np.sqrt(((0.0 + 0.0*xz - y)**2).mean())
print(f"started at:       ${start_err:,.2f}")
