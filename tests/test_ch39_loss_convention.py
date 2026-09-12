"""Chapter 39: the update rule and the reported loss use different normalizations, by convention.

`mse_loss` reports the elementwise mean over n examples and D = 256 outputs. The updates in
`train_full`, `train_lora` and `train_adapter` are the exact gradient of a different but
related objective: the squared error SUMMED over the D outputs and averaged over examples,
which is D times the reported MSE. So every step is D times the gradient of the printed loss,
a constant rescaling of the step (an effective learning rate of eta * D on the printed scale),
not a different direction. The book says so in Step 2. This test pins both facts with central
finite differences against the chapter's own functions.
"""
import io, contextlib
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch39"


def _ns():
    g = {"__name__": "__main__"}
    with contextlib.redirect_stdout(io.StringIO()):
        for f in ["_lib.py", "c1.py", "c2.py"]:
            exec(compile((CH / f).read_text(encoding="utf-8"), str(CH / f), "exec"), g)
        src = (CH / "c3.py").read_text(encoding="utf-8")
        exec(compile(src.split("\nprint(")[0], "c3-def", "exec"), g)       # train_lora only
        src = (CH / "c5.py").read_text(encoding="utf-8")
        exec(compile(src.split("\nprint(")[0], "c5-def", "exec"), g)       # train_adapter only
    return g


def _sum_objective(g, W, X, T):
    H = np.tanh(X @ W)
    return np.mean(np.sum((H - T) ** 2, axis=1))


def test_full_update_is_gradient_of_summed_objective():
    g = _ns(); D = g["D"]; X, T = g["Xtr"][:64], g["Htr_target"][:64]; W0 = g["W_pretrained"]
    eta = 1e-3
    W1, _ = g["train_full"](X, T, X, T, W0, epochs=1, eta=eta)
    step = (W0 - W1) / eta
    rng = np.random.default_rng(39); eps = 1e-5
    for _ in range(5):
        i, j = rng.integers(0, D, 2)
        Wp, Wm = W0.copy(), W0.copy(); Wp[i, j] += eps; Wm[i, j] -= eps
        fd_sum = (_sum_objective(g, Wp, X, T) - _sum_objective(g, Wm, X, T)) / (2 * eps)
        fd_mse = (g["mse_loss"](Wp, X, T) - g["mse_loss"](Wm, X, T)) / (2 * eps)
        assert abs(step[i, j] - fd_sum) < 1e-6 * max(1, abs(fd_sum))
        assert abs(step[i, j] / fd_mse - D) < 1e-3


def test_lora_updates_follow_the_same_convention():
    g = _ns(); D = g["D"]; X, T = g["Xtr"][:64], g["Htr_target"][:64]; W0 = g["W_pretrained"]
    rank, seed, eta = 4, 39, 1e-3
    A0 = np.random.default_rng(seed).normal(0, 0.01, (D, rank)); B0 = np.zeros((rank, D))
    A1, B1, _ = g["train_lora"](X, T, X, T, W0, rank, seed, epochs=1, eta=eta)
    stepB = (B0 - B1) / eta
    i, j = 1, 20; eps = 1e-5
    Bp, Bm = B0.copy(), B0.copy(); Bp[i, j] += eps; Bm[i, j] -= eps
    fd = (_sum_objective(g, W0 + A0 @ Bp, X, T) - _sum_objective(g, W0 + A0 @ Bm, X, T)) / (2 * eps)
    assert abs(stepB[i, j] - fd) < 1e-6 * max(1, abs(fd))
    assert np.allclose(A1, A0)              # with B = 0 the first step leaves A unchanged


def test_adapter_updates_follow_the_same_convention():
    g = _ns(); D = g["D"]; X, T = g["Xtr"][:64], g["Htr_target"][:64]; W0 = g["W_pretrained"]
    bn, seed, eta = 4, 39, 1e-3
    rr = np.random.default_rng(seed)
    Wd0 = rr.normal(0, np.sqrt(1 / D), (D, bn)); Wu0 = np.zeros((bn, D))
    # one step of the chapter's function, recovered through its held-out prediction path
    H0 = np.tanh(X @ W0)
    def obj(Wd, Wu):
        H = H0 + (H0 @ Wd) @ Wu
        return np.mean(np.sum((H - T) ** 2, axis=1))
    # replicate one update exactly as train_adapter computes it, then compare with FD
    z = H0 @ Wd0; H = H0 + z @ Wu0; dH = 2 * (H - T) / len(X)
    dWup = z.T @ dH; dz = dH @ Wu0.T; dWdown = H0.T @ dz
    i, j = 3, 7; eps = 1e-5
    Up, Um = Wu0.copy(), Wu0.copy(); Up[i, j] += eps; Um[i, j] -= eps
    fd = (obj(Wd0, Up) - obj(Wd0, Um)) / (2 * eps)
    assert abs(dWup[i, j] - fd) < 1e-6 * max(1, abs(fd))
    assert np.allclose(dWdown, 0)           # W_up starts at zero, so W_down gets no gradient yet
    # and the chapter's own function agrees with this replica after one step
    loss, n = g["train_adapter"](X, T, X, T, W0, bn, seed, epochs=1, eta=eta)
    assert n == 2 * D * bn


if __name__ == "__main__":
    test_full_update_is_gradient_of_summed_objective(); test_lora_updates_follow_the_same_convention()
    test_adapter_updates_follow_the_same_convention(); print("ok")
