"""Chapter 28, Step 7: the random forest scored under the baselines' own protocol.

As printed, the forest's lag_7 feature takes actual values from inside the 28-day test window
for its last three weeks, which the chapter discloses. This test evaluates the same trained
forest from the same single origin as seasonal naive, feeding its own predictions in as the
lags it has not yet observed, and pins the numbers the book quotes: 795 as printed, about
909 under the matched protocol, against seasonal naive's 758. The direction of the chapter's
conclusion (the forest loses) is unchanged either way.
"""
import io, contextlib, os, shutil, tempfile
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "code" / "ch28"


def _run_chapter():
    tmp = tempfile.mkdtemp()
    for f in CH.glob("*.py"):
        shutil.copy(f, tmp)
    shutil.copy(ROOT / "data" / "generated" / "daily_revenue.csv", tmp)
    cwd = os.getcwd(); os.chdir(tmp)
    g = {"__name__": "__main__"}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for f in ["_lib.py", "c1.py", "c2.py", "c3.py", "c4.py", "c5.py", "c6.py"]:
                exec(compile((Path(tmp) / f).read_text(encoding="utf-8"), f, "exec"), g)
    finally:
        os.chdir(cwd)
    return g


def test_matched_origin_recursive_forest():
    g = _run_chapter()
    s, H, m, X, te = g["s"], g["H"], g["m"], g["X"], g["te"]
    printed = np.mean(np.abs(te["y"] - m.predict(te[X])))
    hist = s.iloc[:-H].tolist(); rec = []
    for d in s.index[-H:]:
        row = pd.DataFrame([[d.dayofweek, d.month, hist[-7], hist[-14], np.mean(hist[-34:-6])]],
                           columns=X)
        p = float(m.predict(row)[0]); rec.append(p); hist.append(p)
    matched = np.mean(np.abs(s.iloc[-H:].values - np.array(rec)))
    naive = np.mean(np.abs(s.iloc[-H:].values - np.tile(s.iloc[-H - 7:-H].values, 4)))
    assert np.allclose(rec[:7], m.predict(te[X])[:7])      # first week uses only real history
    assert abs(printed - 795) < 1 and abs(naive - 758) < 1
    assert abs(matched - 909) < 1.5, matched
    assert matched > printed > naive


if __name__ == "__main__":
    test_matched_origin_recursive_forest(); print("ok")
