"""Vector operations for calculator-pro."""

from collections.abc import Sequence
from math import acos, degrees as to_degrees, sqrt


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


def magnitude(vector: Vector) -> float:
    """Calculate vector magnitude.

    Formula:
        |a| = sqrt(a1^2 + a2^2 + ... + an^2)

    Plain English:
        The magnitude is the length of the vector.
    """
    values = _validate_vector(vector, "vector")
    return sqrt(sum(value**2 for value in values))


def angle_between_vectors(
    left: Vector,
    right: Vector,
    *,
    degrees: bool = False,
) -> float:
    """Calculate the angle between two vectors.

    Formula:
        cos(theta) = (a . b) / (|a||b|)

    Plain English:
        Use the dot product and the two vector lengths to find the angle
        between their directions.
    """
    left_values = _validate_vector(left, "left")
    right_values = _validate_vector(right, "right")

    if len(left_values) != len(right_values):
        raise ValueError("Vectors must have the same number of components.")

    left_magnitude = magnitude(left_values)
    right_magnitude = magnitude(right_values)
    if left_magnitude == 0 or right_magnitude == 0:
        raise ValueError("Angle is undefined for the zero vector.")

    cosine_theta = dot_product(left_values, right_values) / (
        left_magnitude * right_magnitude
    )
    cosine_theta = max(-1.0, min(1.0, cosine_theta))
    angle = acos(cosine_theta)

    if degrees:
        return to_degrees(angle)
    return angle


def _validate_vector(vector: Vector, name: str) -> list[float]:
    """Return a vector as floats, or raise an error."""
    values = list(vector)

    if not values:
        raise ValueError(f"{name} vector must contain at least one component.")

    for value in values:
        if not isinstance(value, int | float):
            raise TypeError(f"{name} vector components must be numeric.")

    return [float(value) for value in values]
