"""Figure 10.1 - three learning rates on the same problem.

Runs Chapter 10's own run(eta, steps) on the same standardized order data the chapter uses,
so the three traces are the chapter's arithmetic.
"""
import numpy as np
from _style import *
from _data import orders

o = orders()
x = o["units"].values.astype(float)
y = o["rev"].values.astype(float)
xz = (x - x.mean()) / x.std()

def run(eta, steps):
    b0, b1, trace = 0.0, 0.0, []
    for _ in range(steps):
        err = (b0 + b1 * xz) - y
        trace.append((err ** 2).mean())
        b0 -= eta * 2 * err.mean()
        b1 -= eta * 2 * (err * xz).mean()
    return trace

STEPS = 60
traces = {eta: run(eta, STEPS) for eta in (0.001, 0.1, 1.2)}
best = run(0.1, 400)[-1]          # the loss the exact solution reaches

fig, ax = plt.subplots(figsize=(8.19, 3.70))
# Three of these colours land within about 8% of each other in tone once the page is
# printed in black ink, and the legend is the only place the reader can tell the lines
# apart. Each series therefore also carries its own dash pattern, which survives the
# conversion; the swatches in the legend carry the pattern too.
# The converging series stays SOLID. Dashing it made it coincide with the dashed reference
# rule it converges onto -- two broken lines of near-identical tone reading as one.
for eta, col, dash, verdict in ((0.001, RED, (0, (6, 2.4)), "crawling"),
                                (0.1, GREEN, "solid", "converging"),
                                (1.2, ORANGE, (0, (1.4, 1.8)), "diverging")):
    ax.plot(range(STEPS), traces[eta], color=col, lw=2.4, ls=dash,
            label=f"eta = {eta}  {verdict}")
ax.axhline(best, color="#9AA5B4", ls=(0, (1, 2.5)), lw=1.1)   # dotted, and lighter than any series
ax.set_yscale("log")
# The log axis has to span twelve orders of magnitude, so the band around the rule is only
# a few points tall and any label placed there is struck by the rule, the converging curve
# or the axis. Put it in the empty middle of the plot with a leader down to the rule.
ax.annotate(f"the best achievable loss ({best:,.0f})", xy=(34, best),
            xytext=(30, 6e8), color=SLATE, fontsize=9.5, ha="center", va="bottom",
            arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.0,
                            connectionstyle="arc3,rad=0.0"))
ax.set_xlabel("gradient descent step"); ax.set_ylabel("loss  (log scale)")
ax.set_title("One number, three outcomes: the learning rate decides whether training works",
             color=NAVY, fontsize=11.5, loc="left")
ax.legend(frameon=False, loc="center right")
fig.tight_layout()
save(fig, "fig10_1.png")
