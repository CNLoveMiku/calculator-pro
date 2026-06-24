"""Combinatorics helpers for calculator-pro."""


def factorial(n: int) -> int:
    """Calculate n factorial.

    Formula:
        n! = n x (n - 1) x ... x 2 x 1, and 0! = 1.

    Plain English:
        Multiply all whole numbers from n down to 1.
    """
    _validate_non_negative_integer(n, "n")

    result = 1
    for value in range(2, n + 1):
        result *= value

    return result


def permutations(n: int, r: int) -> int:
    """Calculate the number of ordered selections, nPr.

    Formula:
        nPr = n! / (n - r)!
        Use this when order matters.

    Plain English:
        Count the number of ways to choose r items from n items when different
        orders count as different outcomes.
    """
    _validate_n_and_r(n, r)
    return factorial(n) // factorial(n - r)


def combinations(n: int, r: int) -> int:
    """Calculate the number of unordered selections, nCr.

    Formula:
        nCr = n! / (r! x (n - r)!)
        Use this when order does not matter.

    Plain English:
        Count the number of ways to choose r items from n items when order is
        ignored.
    """
    _validate_n_and_r(n, r)
    return factorial(n) // (factorial(r) * factorial(n - r))


def _validate_n_and_r(n: int, r: int) -> None:
    """Validate values used in nPr and nCr."""
    _validate_non_negative_integer(n, "n")
    _validate_non_negative_integer(r, "r")

    if r > n:
        raise ValueError("r must be less than or equal to n.")


def _validate_non_negative_integer(value: int, name: str) -> None:
    """Validate that a value is a non-negative integer."""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer.")

    if value < 0:
        raise ValueError(f"{name} must be non-negative.")
