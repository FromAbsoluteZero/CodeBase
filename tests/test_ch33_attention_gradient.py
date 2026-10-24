"""Chapter 33, Step 6: the attention backward pass, checked against finite differences.

Step 3 checks `rnn_backward` numerically; the attention block in `code/ch33/c6.py` (query
scores, softmax weights, weighted-sum context, and the walk back through the recurrence)
had no such check in the text. This reads `train_recall_attention` out of the chapter file,
stops it after the first gradient computation, and compares every parameter gradient with
central finite differences of the same loss, mean cross-entropy over the training set.
"""
import io, contextlib, re
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch33"


def _namespace():
    g = {"__name__": "__main__"}
    with contextlib.redirect_stdout(io.StringIO()):
        for f in ["_lib.py", "c3.py", "c5.py"]:        # softmax/data; rnn_forward; make_recall_task
            src = (CH / f).read_text(encoding="utf-8")
            if f == "c5.py":                            # only the task generator, not the training runs
                src = src.split("\nplain_recall")[0]
                src = src[:src.rfind("\ndef train_recall")] if "\ndef train_recall" in src else src
            exec(compile(src, f, "exec"), g)
    src = (CH / "c6.py").read_text(encoding="utf-8")
    m = re.search(r"^def train_recall_attention\(.*?(?=^\S)", src, re.S | re.M)
    body = m.group(0)
    stop = "        Wo -= eta*dWo; bo -= eta*dbo; q -= eta*dq"
    assert stop in body
    body = body.replace(stop, "        return dict(Xs=Xs, Y=Y, Wx=Wx, Wh=Wh, bh=bh, q=q, Wo=Wo, bo=bo,\n"
                              "                    dWx=dWx, dWh=dWh, dbh=dbh, dq=dq, dWo=dWo, dbo=dbo)")
    exec(compile(body, "c6-grad", "exec"), g)
    return g


def _loss(g, Xs, Y, Wx, Wh, bh, q, Wo, bo):
    hs = g["rnn_forward"](Xs, Wx, Wh, bh)[:, 1:]
    weights = g["softmax"](hs @ q)
    context = np.einsum("nt,nth->nh", weights, hs)
    p = g["softmax"](context @ Wo + bo)
    return -np.mean(np.log(np.sum(p * Y, axis=1)))


def test_attention_gradients_match_finite_differences():
    g = _namespace()
    r = g["train_recall_attention"](10, seed=33)
    Xs, Y = r["Xs"], r["Y"]
    params = {k: r[k].astype(float).copy() for k in ("Wx", "Wh", "bh", "q", "Wo", "bo")}
    eps = 1e-6
    for name, grad in (("Wx", r["dWx"]), ("Wh", r["dWh"]), ("bh", r["dbh"]),
                       ("q", r["dq"]), ("Wo", r["dWo"]), ("bo", r["dbo"])):
        arr = params[name]
        rng = np.random.default_rng(len(name))
        for _ in range(4):
            idx = tuple(rng.integers(0, s) for s in arr.shape)
            orig = arr[idx]
            arr[idx] = orig + eps; lp = _loss(g, Xs, Y, **params)
            arr[idx] = orig - eps; lm = _loss(g, Xs, Y, **params)
            arr[idx] = orig
            numeric = (lp - lm) / (2 * eps)
            assert abs(numeric - grad[idx]) < 1e-6, f"{name}{idx}: analytic {grad[idx]:.8f} numeric {numeric:.8f}"


if __name__ == "__main__":
    test_attention_gradients_match_finite_differences(); print("ok")
