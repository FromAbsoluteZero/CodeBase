"""Figure 2.2 - a traceback, annotated at 400 DPI.

The traceback text, the three annotations and the closing sentence are the diagram's.
"""
from _style import *

fig, ax = blank((7.60, 3.033), 100, 40)

rbox(ax, 4.0, 8.5, 65.0, 28.0, edge=NAVY, face="#F5F7FA", lw=2.0, r=1.2)
TB = [(7.5, 33.5, "Traceback (most recent call last):", "#5A6673", False),
      (9.5, 29.5, 'File "<stdin>", line 3, in <module>', "#5A6673", False),
      (11.5, 25.5, 'total = revenue + "12"', "#3B4A5A", False),
      (18.0, 21.7, "~~~~~~~~^~~~~~", "#3B4A5A", False),
      (7.5, 17.5, "TypeError: unsupported operand type(s) for +:", RED, True),
      (7.5, 13.3, "'int' and 'str'", RED, True)]
for x, y, t, c, b in TB:
    label(ax, x, y, t, fs=9.5, color=c, bold=b, mono=True, ha="left")

NOTES = [(33.5, "IGNORE FOR NOW", "how Python\ngot there", "#C8CED8", "#9AA5B4"),
         (25.0, "THEN THIS", "which line\nof your code", "#5A6673", SLATE),
         (14.5, "READ THIS FIRST", "the error type\nand what went wrong", "#B0521F", SLATE)]
for y, head, body, acol, tcol in NOTES:
    arrow(ax, 70.5, y, 75.5, y, color=acol, lw=1.8, scale=14)
    label(ax, 77.0, y + 2.2, head, fs=9.5, bold=True,
          color=acol if acol != "#C8CED8" else "#B6BEC9", ha="left")
    label(ax, 77.0, y - 2.0, body, fs=9.5, color=tcol, ha="left", va="center")

label(ax, 4.0, 3.0, "Change one thing. Run again. Read the last line again. "
                    "That loop is what programming is.",
      fs=10.5, italic=True, color=NAVY, ha="left")
save(fig, "fig02_2.png")
