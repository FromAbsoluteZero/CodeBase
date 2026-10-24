"""Chapters 22 and 36: ranking ties must break the same way on every platform.

`np.argsort` defaults to an introsort whose tie order differs between platforms and NumPy
builds. Chapter 36's top-k and top-p sampling (`code/ch36/c4.py`) and Chapter 22's decile
calibration table (`code/ch22/c4.py`, and Figure 22.2 in `figs.py`) both rank arrays with
many exact ties, so the printed output depended on the machine. The fix is
`kind="stable"`, which orders ties by index. These tests pin that.
"""
import re
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent / "code"


def _argsort_calls(path):
    return re.findall(r"np\.argsort\(([^)]*)\)", (ROOT / path).read_text(encoding="utf-8"))


def test_sources_use_stable_sort():
    for path in ["ch36/c4.py", "ch22/c4.py", "ch22/figs.py"]:
        calls = _argsort_calls(path)
        assert calls, f"{path}: no argsort found"
        for c in calls:
            assert 'kind="stable"' in c, f"{path}: np.argsort({c}) is not stable"


def test_top_k_with_ties_is_index_ordered():
    p = np.array([0.2, 0.3, 0.2, 0.3, 0.0])
    idx = np.argsort(-p, kind="stable")[:3]
    assert idx.tolist() == [1, 3, 0]


def test_decile_bins_with_ties_are_deterministic():
    rng = np.random.default_rng(0)
    p = rng.choice([0.001, 0.002, 0.003], size=200)     # heavy ties, like HGB probabilities
    order = np.argsort(p, kind="stable")
    bins = [order[b * len(p) // 10:(b + 1) * len(p) // 10].tolist() for b in range(10)]
    again = [np.argsort(p, kind="stable")[b * len(p) // 10:(b + 1) * len(p) // 10].tolist()
             for b in range(10)]
    assert bins == again
    # within a run of equal values, stable order is index order
    for b in bins:
        vals = p[b]
        for v in np.unique(vals):
            same = [i for i in b if p[i] == v]
            assert same == sorted(same)


if __name__ == "__main__":
    test_sources_use_stable_sort(); test_top_k_with_ties_is_index_ordered()
    test_decile_bins_with_ties_are_deterministic(); print("ok")
