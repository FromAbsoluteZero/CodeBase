"""Chapters 22 and 23: two accountings of the six-dollar review, stated and reconciled.

Chapter 22 Step 7 charges the review cost on every flagged transaction (break-even precision
6/204 = 2.94%). Chapter 23's p* = C_FP / (C_FP + C_FN) charges it only on wasted reviews
(6/210 = 2.86%), as does `total_cost()` in Steps 2 and 4; Step 5's capacity net charges it on
every review again. The book now says so in both places. This test runs Chapter 23 as
printed and checks the two accountings differ by exactly C_FP per caught fraud.
"""
import io, contextlib
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch23"
DATA = Path(__file__).resolve().parent.parent / "data" / "generated"


def _run_chapter(tmp_path):
    import shutil
    for f in CH.glob("*.py"):
        shutil.copy(f, tmp_path)
    shutil.copy(DATA / "transactions.csv", tmp_path)
    import os
    cwd = os.getcwd(); os.chdir(tmp_path)
    g = {"__name__": "__main__"}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for f in ["_lib.py", "c1.py", "c2.py", "c3.py", "c4.py", "c5.py"]:
                exec(compile((tmp_path / f).read_text(encoding="utf-8"), f, "exec"), g)
    finally:
        os.chdir(cwd)
    return g


def test_break_even_conventions():
    assert abs(6 / 204 - 0.0294) < 5e-5            # Chapter 22: every review charged
    assert abs(6 / (6 + 204) - 0.0286) < 5e-5      # Chapter 23: wasted reviews only


def test_step5_net_reconciles_with_total_cost(tmp_path=None):
    if tmp_path is None:
        import tempfile; tmp_path = Path(tempfile.mkdtemp())
    g = _run_chapter(tmp_path)
    yte, top, C_FP, C_FN, CAP = g["yte"], g["top"], g["C_FP"], g["C_FN"], g["CAPACITY"]
    tp = int(yte[top].sum())
    net_every_review = tp * C_FN - CAP * C_FP                     # Step 5 as printed
    pred = np.zeros_like(yte); pred[top] = 1
    cost, fp, fn = g["total_cost"](pred)
    net_wasted_only = C_FN * int(yte.sum()) - cost                # Steps 2 and 4's accounting
    assert net_every_review == g["net"]
    assert net_wasted_only - net_every_review == tp * C_FP        # exactly one review per caught fraud
    assert (net_every_review, net_wasted_only) == (3492, 3630)    # the two figures the book states


if __name__ == "__main__":
    test_break_even_conventions(); test_step5_net_reconciles_with_total_cost(); print("ok")
