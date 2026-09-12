"""Chapter 39, Step 4: the source CNN's filters must actually be trained.

`train_cnn_source` in `code/ch39/c4.py` is described as "identical recipe to Chapter 35".
The pre-publication draft updated only the classification head and returned the filters at
their random initial values, so every downstream accuracy in Step 4 was measured on random
features. This runs Steps 1-3 and the Step 4 preamble from the chapter files and asserts that
training moves the filters, in the spirit of `not np.allclose(filters_before, filters_after)`.
"""
import io, contextlib, sys
from pathlib import Path
import numpy as np

CH = Path(__file__).resolve().parent.parent / "code" / "ch39"


def _run_to_source_filters():
    g = {"__name__": "__main__"}
    with contextlib.redirect_stdout(io.StringIO()):
        for f in ["_lib.py", "c1.py", "c2.py", "c3.py"]:
            exec(compile((CH / f).read_text(encoding="utf-8"), str(CH / f), "exec"), g)
        src = (CH / "c4.py").read_text(encoding="utf-8")
        head = src.split("src_filters = train_cnn_source")[0]
        exec(compile(head, "c4-head", "exec"), g)
    return g


def test_filters_change_during_source_training():
    g = _run_to_source_filters()
    rr = np.random.default_rng(39)
    filters_before = rr.normal(0, np.sqrt(2 / 9), (4, 3, 3))      # the function's own draw
    filters_after = g["train_cnn_source"](g["Xsrc_tr"], g["ysrc_tr"], seed=39)
    assert filters_after.shape == filters_before.shape
    assert not np.allclose(filters_before, filters_after), "source filters were never updated"
    assert np.abs(filters_after - filters_before).max() > 0.1


def test_recipe_updates_filters_in_source():
    src = (CH / "c4.py").read_text(encoding="utf-8")
    assert "filters -= " in src, "no filter update in train_cnn_source"


if __name__ == "__main__":
    test_filters_change_during_source_training(); test_recipe_updates_filters_in_source(); print("ok")
