"""Chapter 10, Solution 1: a derivative fixes the step's direction, not the loss after the step.

Weight 5, derivative -40, learning rate 0.1 gives weight 9. Two convex losses share that
derivative at 5; the same step lowers one and raises the other, which is why the solution
now says the change in loss cannot be read from the derivative alone.
"""


def test_two_losses_same_derivative_opposite_outcomes():
    f1 = lambda w: (w - 25) ** 2          # derivative at 5: -40
    f2 = lambda w: 20 * (w - 6) ** 2      # derivative at 5: -40
    w_new = 5 - 0.1 * (-40)
    assert w_new == 9
    assert 2 * (5 - 25) == -40 and 40 * (5 - 6) == -40
    assert (f1(5), f1(9)) == (400, 256)   # falls
    assert (f2(5), f2(9)) == (20, 180)    # rises


if __name__ == "__main__":
    test_two_losses_same_derivative_opposite_outcomes(); print("ok")
