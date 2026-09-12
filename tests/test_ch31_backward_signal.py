"""Chapter 31, Step 3: the backward signal through the sigmoid stack, weights included.

The printed block used to multiply only the maximum sigmoid slope per layer and call the
product "backward signal". That product is the activations' share of the gradient; each
weight matrix multiplies the gradient too, and a differently scaled matrix can shrink it less
or even grow it. The block now also propagates a gradient of 1.0 at every output unit back
through the network's actual weights. This test runs the chapter's own Steps 1-3, checks the
propagated gradient against central finite differences of the same forward pass, and pins the
two printed factors.
"""
import io, contextlib
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch31"


def _run():
    g = {"__name__": "__main__"}
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        for f in ["_lib.py", "c1.py", "c2.py", "c3.py"]:
            exec(compile((CH / f).read_text(encoding="utf-8"), str(CH / f), "exec"), g)
    return g, out.getvalue()


def test_propagated_gradient_matches_finite_differences():
    g, _ = _run()
    sigmoid, Ws, X = g["sigmoid"], g["Ws_s"], g["X"][:200]

    def forward_sum(x):                      # one input row -> sum of its 64 outputs
        a = x[None, :]
        for W in Ws:
            a = sigmoid(a @ W)
        return a.sum()                       # upstream gradient 1.0 at every output unit

    grad = g["g"]                            # what the block propagated back to the input
    assert grad.shape == X.shape
    eps = 1e-5
    rng = np.random.default_rng(31)
    for _ in range(6):
        i, j = rng.integers(0, 200), rng.integers(0, 64)
        xp, xm = X[i].copy(), X[i].copy(); xp[j] += eps; xm[j] -= eps
        fd = (forward_sum(xp) - forward_sum(xm)) / (2 * eps)
        assert abs(fd - grad[i, j]) < 1e-9 + 1e-4 * abs(grad[i, j]), (i, j, fd, grad[i, j])


def test_printed_factors():
    g, text = _run()
    assert abs(g["signal"] - 0.25 ** 8) < 1e-8                # slopes only (max slope is 0.25 to 4 places)
    assert abs(np.abs(g["g"]).mean() - 5.28e-05) < 5e-07      # through this network's weights
    assert "slopes only" in text and "through weights" in text


def test_weights_can_reverse_the_activation_only_story():
    # A scalar counterexample: sigmoid(8h - 4) has slope 0.25 at h = 0.5, but the full layer
    # derivative is 8 * 0.25 = 2, so eight layers multiply a gradient by 256, not by 0.25**8.
    h, d = 0.5, 1.0
    for _ in range(8):
        s = 1 / (1 + np.exp(-(8 * h - 4)))
        d *= 8 * s * (1 - s)
        h = s
    assert abs(d - 256) < 1e-9


if __name__ == "__main__":
    test_propagated_gradient_matches_finite_differences(); test_printed_factors()
    test_weights_can_reverse_the_activation_only_story(); print("ok")
