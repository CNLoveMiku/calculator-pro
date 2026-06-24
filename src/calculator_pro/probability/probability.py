"""Probability helpers for calculator-pro."""

from calculator_pro.probability.combinatorics import combinations


def conditional_probability(
    probability_a_and_b: float,
    probability_b: float,
) -> float:
    """Calculate conditional probability P(A|B).

    Formula:
        P(A|B) = P(A and B) / P(B)
        This means "the probability of A happening, given that B happened."

    Plain English:
        Restrict the sample space to cases where B happened, then find how often
        A also happened.
    """
    _validate_probability(probability_a_and_b, "probability_a_and_b")
    _validate_probability(probability_b, "probability_b")

    if probability_b == 0:
        raise ValueError("probability_b must be greater than 0.")

    if probability_a_and_b > probability_b:
        raise ValueError("P(A and B) cannot be greater than P(B).")

    return probability_a_and_b / probability_b


def binomial_probability(n: int, k: int, p: float) -> float:
    """Calculate the exact binomial probability P(X = k).

    Formula:
        P(X = k) = nCk x p^k x (1 - p)^(n - k)

    Plain English:
        Use this when there are n independent trials, each trial has the same
        success probability p, and you want exactly k successes.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if k < 0 or k > n:
        raise ValueError("k must be between 0 and n.")

    _validate_probability(p, "p")

    return combinations(n, k) * (p**k) * ((1 - p) ** (n - k))


def _validate_probability(value: float, name: str) -> None:
    """Validate that a value is a probability between 0 and 1."""
    if not isinstance(value, int | float):
        raise TypeError(f"{name} must be numeric.")

    if value < 0 or value > 1:
        raise ValueError(f"{name} must be between 0 and 1.")
