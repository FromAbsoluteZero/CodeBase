"""Chapter 2, worked example Step 5: the break-even quantity rounds UP.

Chapter 2 prints no companion directory, so the line under test is quoted from the book:

    breakeven = monthly_fixed / margin_dollars
    breakeven_cups = math.ceil(breakeven)

The first edition's pre-publication draft used `int(monthly_fixed // margin_dollars) + 1`,
which is right only when the division is inexact: 900 / 3 gave 301 cups instead of 300.
This test pins the corrected idiom on an exact division, on the chapter's own numbers, and
on a value just above an integer, and shows that the old idiom fails the exact case.
"""
import math


def book_breakeven(monthly_fixed, margin_dollars):
    breakeven = monthly_fixed / margin_dollars
    breakeven_cups = math.ceil(breakeven)
    return breakeven, breakeven_cups


def old_idiom(monthly_fixed, margin_dollars):
    return int(monthly_fixed // margin_dollars) + 1


def test_exact_division_is_not_rounded_up_again():
    assert book_breakeven(900, 3.0) == (300.0, 300)
    assert old_idiom(900, 3.0) == 301          # the defect the fix removes


def test_chapter_numbers_unchanged():
    breakeven, cups = book_breakeven(900, 3.45)
    assert round(breakeven, 2) == 260.87 and cups == 261


def test_just_above_an_integer_rounds_up():
    assert book_breakeven(900.01, 3.0)[1] == 301


if __name__ == "__main__":
    test_exact_division_is_not_rounded_up_again(); test_chapter_numbers_unchanged()
    test_just_above_an_integer_rounds_up(); print("ok")
