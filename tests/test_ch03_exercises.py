"""Chapter 3, practice and solutions: the printed exercise code must be valid Python.

The first-edition draft compressed compound statements onto one line with semicolons
(`def total(prices): s = 0; for p in prices: ...`), which Python rejects. Exercise 2 and
Solutions 3 and 4 are now printed as indented code blocks. Chapter 3 has no companion
directory, so the printed text is quoted here: each block must compile, the flawed function
must fail the way the solution says (None, then TypeError), and the repair must return 6.
"""
EXERCISE_2 = """def total(prices):
    s = 0
    for p in prices:
        s = s + p
    print(s)

result = total([1, 2, 3])
print(result * 2)
"""
SOLUTION_3 = '''if amount >= 500:
    label = "large"
elif amount >= 100:
    label = "medium"
elif amount > 0:
    label = "small"
else:
    label = "empty"
'''
SOLUTION_4 = """counts = {}
for r in regions:
    counts[r] = counts.get(r, 0) + 1
"""
OLD_ONE_LINERS = [
    "def total(prices): s = 0; for p in prices: s = s + p; print(s)",
    'if amount >= 500: label = "large"; elif amount >= 100: label = "medium"; elif amount > 0: label = "small"; else: label = "empty"',
    "counts = {}; for r in regions: counts[r] = counts.get(r, 0) + 1",
]


def test_printed_blocks_compile():
    for src in (EXERCISE_2, SOLUTION_3, SOLUTION_4):
        compile(src, "<chapter 3>", "exec")


def test_old_one_liners_do_not():
    import pytest
    for src in OLD_ONE_LINERS:
        with pytest.raises(SyntaxError):
            compile(src, "<old>", "exec")


def test_exercise_2_fails_as_the_solution_says_and_repairs():
    import io, contextlib, pytest
    g = {}
    with contextlib.redirect_stdout(io.StringIO()) as out, pytest.raises(TypeError):
        exec(EXERCISE_2, g)
    assert out.getvalue().strip() == "6" and g["result"] is None
    repaired = EXERCISE_2.replace("    print(s)", "    return s")
    g = {}
    with contextlib.redirect_stdout(io.StringIO()) as out:
        exec(repaired, g)
    assert g["result"] == 6 and out.getvalue().strip() == "12"


def test_solutions_3_and_4_behave():
    labels = {}
    for amount in (800, 500, 100, 5, 0):
        g = {"amount": amount}; exec(SOLUTION_3, g); labels[amount] = g["label"]
    assert labels == {800: "large", 500: "large", 100: "medium", 5: "small", 0: "empty"}
    g = {"regions": ["East", "West", "East", "North", "West", "East"]}; exec(SOLUTION_4, g)
    assert g["counts"] == {"East": 3, "West": 2, "North": 1}


if __name__ == "__main__":
    test_printed_blocks_compile(); test_exercise_2_fails_as_the_solution_says_and_repairs()
    test_solutions_3_and_4_behave(); print("ok")
