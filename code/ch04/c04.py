import numpy as np, time

X = np.random.default_rng(0).normal(size=(1000, 5))   # 1000 rows, 5 features
w = np.array([2.0, -1.5, 0.5, 0.0, 3.0])              # one weight per feature

y_hat = X @ w                       # (1000,5) @ (5,) -> (1000,)
print(f"X {X.shape}   w {w.shape}   X @ w {y_hat.shape}")

# @ is matrix multiplication. * is elementwise, and broadcasting will often
# make it succeed silently with the wrong shape rather than raise.
print(f"(X * w).shape = {(X * w).shape}   <- not a prediction")

# Broadcasting: shapes are compared from the trailing axis backward.
col_means = X.mean(axis=0)          # axis=0 collapses rows -> one per column
centered = X - col_means            # (1000,5) - (5,) stretches the (5,)
print(f"column means {col_means.round(3)}")
print(f"centered column means {centered.mean(axis=0).round(12)}")

# Vectorization is not a style preference.
t0 = time.perf_counter()
loop = np.array([sum(X[i, j] * w[j] for j in range(5)) for i in range(1000)])
t_loop = time.perf_counter() - t0
t0 = time.perf_counter()
for _ in range(100):
    fast = X @ w
t_vec = (time.perf_counter() - t0) / 100
print(f"loop {t_loop*1000:.2f} ms   vectorized {t_vec*1000:.4f} ms"
      f"   ratio {t_loop/t_vec:,.0f}x")
print("same answer:", np.allclose(loop, fast))
