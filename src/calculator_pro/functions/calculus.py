"""Calculus helpers for calculator-pro."""

from collections.abc import Callable


def approximate_derivative(
    function: Callable[[float], float],
    x: float,
    step: float = 1e-5,
) -> float:
    """Approximate a derivative at a point using central difference.

    Formula:
        f'(x) is approximately (f(x + h) - f(x - h)) / (2h),
        where h is a small positive step.

    Plain English:
        Estimate the slope by comparing function values just to the right and
        just to the left of x.
    """
    if not callable(function):
        raise TypeError("function must be callable.")

    if not isinstance(x, int | float):
        raise TypeError("x must be numeric.")

    if not isinstance(step, int | float):
        raise TypeError("step must be numeric.")

    if step <= 0:
        raise ValueError("step must be greater than 0.")

    return (function(x + step) - function(x - step)) / (2 * step)
