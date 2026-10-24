"""Shared style for the diagrams.

Matches the style the chapter figure generators in code/ch16..ch44 use, so a
figure sits beside a generated one without looking different.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY, RED, GREEN, ORANGE, SLATE = "#1F3A5F", "#8C2F39", "#2F6B54", "#C1662F", "#5A6673"
TINT, RULE = "#EEF2F6", "#C8CED8"
DPI = 400

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10.5,
    "axes.edgecolor": SLATE, "text.color": "#222",
    "xtick.color": SLATE, "ytick.color": SLATE,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.dpi": DPI,
})

def save(fig, name):
    fig.savefig(name, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------------------------------
# Primitives shared by the diagram scripts. The generated figures in code/chNN/figs.py
# use plain matplotlib patches, so these are deliberately thin wrappers rather than a layer.
import matplotlib.patches as mp

def blank(figsize, xlim=100, ylim=50):
    """A full-bleed axes with no frame, in arbitrary layout units, for a drawn diagram.

    add_axes rather than subplots: the diagram supplies its own margins, and a default
    subplot inset would shrink one layout unit by a fifth and make the text overrun the
    boxes it was measured against."""
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, xlim); ax.set_ylim(0, ylim); ax.axis("off")
    return fig, ax

def rbox(ax, x, y, w, h, edge=None, face="white", lw=1.6, r=1.2, z=1):
    ax.add_patch(mp.FancyBboxPatch((x, y), w, h,
                                   boxstyle=f"round,pad=0,rounding_size={r}",
                                   linewidth=lw, edgecolor=edge or SLATE,
                                   facecolor=face, zorder=z))

def label(ax, x, y, txt, fs=10.5, color="#222", bold=False, italic=False,
          ha="center", va="center", mono=False, ls=1.25, z=3):
    ax.text(x, y, txt, ha=ha, va=va, fontsize=fs, color=color,
            fontweight="bold" if bold else "normal",
            style="italic" if italic else "normal",
            family="DejaVu Sans Mono" if mono else "DejaVu Sans",
            linespacing=ls, zorder=z)

def arrow(ax, x0, y0, x1, y1, color=None, lw=2.0, scale=16, style="-|>", conn=None):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=style, color=color or ORANGE, lw=lw,
                                mutation_scale=scale, shrinkA=0, shrinkB=0,
                                connectionstyle=conn or "arc3,rad=0"))

def rule(ax, x0, x1, y, color=None, lw=1.0):
    ax.plot([x0, x1], [y, y], color=color or RULE, lw=lw, zorder=0)
