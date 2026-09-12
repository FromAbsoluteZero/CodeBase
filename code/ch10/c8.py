X = np.column_stack([np.ones(len(x)), x])
exact = np.linalg.lstsq(X, y, rcond=None)[0]

print(f"gradient descent: intercept {intercept:9.4f}  "
      f"slope {slope:8.4f}")
print(f"exact algebra:    intercept {exact[0]:9.4f}  "
      f"slope {exact[1]:8.4f}")
print(f"difference:       {abs(intercept-exact[0]):9.6f}  "
      f"      {abs(slope-exact[1]):8.6f}")
