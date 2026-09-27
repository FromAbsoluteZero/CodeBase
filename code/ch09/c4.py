import numpy as np
from scipy.linalg import hilbert

a = np.array([3.0, 4.0])
cosine = lambda u, v: (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

for name, v in [("similar direction", np.array([4.0, 3.0])),
                ("perpendicular", np.array([-4.0, 3.0])),
                ("opposite", np.array([-3.0, -4.0]))]:
    print(f"a . {name:<18} = {a @ v:>6.1f}   cosine {cosine(a, v):>6.3f}")

# Solve, never invert. On a well-behaved matrix both are fine, so the
# demonstration needs one that is not: the Hilbert matrix is the standard
# ill-conditioned example, and correlated predictors produce the same effect.
print(f"\n{'n':>4}{'condition':>12}{'err solve':>13}{'err inverse':>14}")
for n in (6, 10, 14):
    A = hilbert(n)
    x_true = np.ones(n)
    y = A @ x_true
    e_solve = np.abs(np.linalg.solve(A, y) - x_true).max()
    e_inv = np.abs(np.linalg.inv(A) @ y - x_true).max()
    print(f"{n:>4}{np.linalg.cond(A):>12.1e}{e_solve:>13.2e}{e_inv:>14.2e}")
