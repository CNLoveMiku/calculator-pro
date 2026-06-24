"""Vector operations for calculator-pro."""

from collections.abc import Sequence


Vector = Sequence[float]


def dot_product(left: Vector, right: Vector) -> float:
    """Calculate the dot product of two vectors.

    Formula:
        a . b = a1b1 + a2b2 + ... + anbn

    Plain English:
        Multiply matching components, then add those products together.
    """
    left_values = _validate_vector(left, "left")
    right_values = _validate_vector(right, "right")

    if len(left_values) != len(right_values):
        raise ValueError("Vectors must have the same number of components.")

    return sum(
        left_value * right_value
        for left_value, right_value in zip(left_values, right_values)
    )


def cross_product(left: Vector, right: Vector) -> list[float]:
    """Calculate the cross product of two 3D vectors.

    Formula:
        For a = [a1, a2, a3] and b = [b1, b2, b3],
        a x b = [a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1]

    Plain English:
        The result is a new vector perpendicular to both original 3D vectors.
    """
    left_values = _validate_vector(left, "left")
    right_values = _validate_vector(right, "right")

    if len(left_values) != 3 or len(right_values) != 3:
        raise ValueError("Cross product requires two 3D vectors.")

    a1, a2, a3 = left_values
    b1, b2, b3 = right_values
    return [
        a2 * b3 - a3 * b2,
        a3 * b1 - a1 * b3,
        a1 * b2 - a2 * b1,
    ]


def _validate_vector(vector: Vector, name: str) -> list[float]:
    """Return a vector as floats, or raise an error."""
    values = list(vector)

    if not values:
        raise ValueError(f"{name} vector must contain at least one component.")

    for value in values:
        if not isinstance(value, int | float):
            raise TypeError(f"{name} vector components must be numeric.")

    return [float(value) for value in values]
