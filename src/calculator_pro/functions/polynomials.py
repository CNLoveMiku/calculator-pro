"""Polynomial helpers for calculator-pro."""

from collections.abc import Sequence


def evaluate_polynomial(coefficients: Sequence[float], x: float) -> float:
    """Evaluate a polynomial using Horner's method.

    Formula:
        For coefficients [a, b, c], the polynomial is ax^2 + bx + c.
        Horner's method rewrites it as (a * x + b) * x + c,
        which uses fewer multiplications.

    Plain English:
        Start with the first coefficient, repeatedly multiply by x, then add
        the next coefficient.
    """
    if not coefficients:
        raise ValueError("At least one coefficient is required.")

    if not isinstance(x, int | float):
        raise TypeError("x must be numeric.")

    result = 0.0
    for coefficient in coefficients:
        if not isinstance(coefficient, int | float):
            raise TypeError("All coefficients must be numeric.")
        result = result * x + coefficient

    return result
