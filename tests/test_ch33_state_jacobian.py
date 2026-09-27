"""Chapter 33, Step 2: the state-to-state Jacobian of the recurrence, checked numerically.

The chapter's `run_and_track_grad` multiplies one factor per step to get the gradient of the
last hidden state with respect to the first, and prints its norm. Step 3's finite-difference
checks cover the *parameter* gradients of `rnn_backward`; they say nothing about this product.
This test reads the function out of `code/ch33/c2.py` at run time, rewrites only its `return`
so the matrix comes back instead of its norm, and compares the matrix against central finite
differences of the same recurrence, in the same row-vector convention (row i is the response
of the last state to a move in element i of the first). It also asserts that the factors in
the opposite order would NOT pass, so the test can tell the two apart.
"""
import re, sys
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch33"


def _load_c2(swap=False):
    src = (CH / "c2.py").read_text(encoding="utf-8")
    m = re.search(r"^def run_and_track_grad\(.*?(?=^\S|\Z)", src, re.S | re.M)
    body = m.group(0).rstrip().replace("return np.linalg.norm(grad)", "return grad")
    if swap:  # the other order of the two factors, which must fail
        body = body.replace("Wh_ @ np.diag(tanh_grad(hs[t]))", "np.diag(tanh_grad(hs[t])) @ Wh_")
        assert body != m.group(0), "swap did not apply"
    g = {"np": np}
    exec("def tanh_grad(h):\n    return 1 - h**2\n", g)
    g["D_hid"] = 16
    g["r2"] = np.random.default_rng(33)
    g["Wh_decay"] = g["r2"].normal(0, 0.3, (16, 16))          # the chapter's own draw order
    exec(body, g)
    return g


def _finite_difference(xs, W, eps=1e-6):
    def forward(h0):
        h = h0.copy()
        for x in xs:
            h = np.tanh(x + h @ W)
        return h
    J = np.empty((16, 16))
    for i in range(16):
        d = np.zeros(16); d[i] = eps
        J[i] = (forward(d) - forward(-d)) / (2 * eps)
    return J


def _run(swap):
    g = _load_c2(swap)
    out = []
    for n in (5, 10):
        # replay the chapter's RNG so the inputs are the ones the function drew
        r_probe = np.random.default_rng(33); r_probe.normal(0, 0.3, (16, 16))
        for k in (5, 10):
            xs = r_probe.normal(size=(k, 16))
            if k == n: break
        J = g["run_and_track_grad"](n, g["Wh_decay"])
        J_fd = _finite_difference(xs, g["Wh_decay"])
        out.append((n, np.linalg.norm(J), np.linalg.norm(J - J_fd) / np.linalg.norm(J_fd)))
    return out


def test_state_jacobian_matches_finite_differences():
    for n, norm, rel in _run(swap=False):
        assert rel < 1e-6, f"{n} steps: Jacobian differs from finite differences, relative {rel:.2e}"
    norms = {n: norm for n, norm, _ in _run(swap=False)}
    assert abs(norms[5] - 0.5151874816) < 1e-9
    assert abs(norms[10] - 0.1483736332) < 1e-9


def test_opposite_factor_order_is_detected():
    for n, _, rel in _run(swap=True):
        assert rel > 0.5, f"{n} steps: the swapped order was not detected (relative {rel:.2e})"


if __name__ == "__main__":
    test_state_jacobian_matches_finite_differences()
    test_opposite_factor_order_is_detected()
    print("ok")
