"""Make the figures readable when the book is printed in black and white. OFF BY DEFAULT.

KDP converts a black-ink interior to greyscale. Under Rec. 601 the palette collapses:

    navy   #1F3A5F -> 54      maroon #8C2F39 -> 76
    green  #2F6B54 -> 86      slate  #5A6673 -> 100

so navy and maroon land 22 levels apart and maroon and green only 10. Two solid curves of
the same weight separated by that little are hard to tell apart on paper.

This module gives every colour its own dash pattern and its own hatch, keyed to the colour
itself, so a reader in greyscale separates the series by pattern while a reader in colour sees
the same palette. Anything that already sets a linestyle, a format string or a hatch is left
alone.

**It does nothing unless you set FAZ_GREYSCALE=1.** The figures printed in the book and shipped
in `figures/` are drawn WITHOUT it, so leaving it off is what reproduces the book. Turning it on
changes 44 of the 53 generated figures — a real improvement for a black-ink printing, and a real
difference from the printed page. Choose deliberately:

    FAZ_GREYSCALE=1 python figs.py

Two figures needed the separation badly enough to carry it unconditionally, and they carry it in
their own source rather than here: 10.1 and 15.1, in `figures/sources/`.

Imported by each code/chNN/figs.py before it draws.
"""
import os as _os

from matplotlib.axes import Axes

_ENABLED = _os.environ.get("FAZ_GREYSCALE") == "1"

DASH = {
    "#8C2F39": (0, (6.0, 2.2)),            # maroon: long dash
    "#2F6B54": (0, (1.4, 1.8)),            # green:  dotted
    "#C1662F": (0, (7.0, 2.0, 1.4, 2.0)),  # orange: dash-dot
}
HATCH = {"#8C2F39": "///", "#2F6B54": "...", "#C1662F": "\\\\\\"}
# Matplotlib draws hatching in the EDGE colour, so setting the edge to the face colour would
# make the hatch invisible in colour and in greyscale alike. It is drawn in the body-text ink
# instead, which reads on every stock.
HATCH_INK = "#222222"

_plot, _bar, _barh = Axes.plot, Axes.bar, Axes.barh

def _has_style(args, kw):
    if any(k in kw for k in ("ls", "linestyle", "dashes")):
        return True
    for a in args:
        # A format string. Anything that sets a line style OR a marker is left alone:
        # injecting a dash into ax.plot(x, y, "o", ...) would draw a line the author
        # deliberately did not ask for.
        if isinstance(a, str) and a and not a[0].isdigit():
            if any(c in a for c in "-:") or any(c in a for c in "os^v<>dDp*+x.,hH1234|_"):
                return True
    if "marker" in kw and kw.get("linestyle") in (None, "", "none", "None"):
        return True
    return False

def plot(self, *args, **kw):
    c = kw.get("color") or kw.get("c")
    if isinstance(c, str) and c in DASH and not _has_style(args, kw):
        kw["linestyle"] = DASH[c]
    return _plot(self, *args, **kw)

def _hatched(fn):
    def wrapper(self, *args, **kw):
        c = kw.get("color") or kw.get("facecolor")
        if isinstance(c, str) and c in HATCH and "hatch" not in kw:
            kw["hatch"] = HATCH[c]
            kw.setdefault("edgecolor", HATCH_INK)
            kw.setdefault("linewidth", 0.6)
        return fn(self, *args, **kw)
    return wrapper

if _ENABLED:
    Axes.plot = plot
    Axes.bar = _hatched(_bar)
    Axes.barh = _hatched(_barh)
