"""Tests for vector operations."""

import pytest

from calculator_pro.vectors import (
    angle_between_vectors,
    cross_product,
    dot_product,
    magnitude,
)


def test_dot_product() -> None:
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32.0


def test_cross_product() -> None:
    assert cross_product([1, 0, 0], [0, 1, 0]) == [0.0, 0.0, 1.0]


def test_magnitude() -> None:
    assert magnitude([3, 4]) == 5.0


def test_angle_between_vectors_in_degrees() -> None:
    assert angle_between_vectors([1, 0], [0, 1], degrees=True) == pytest.approx(90.0)


def test_angle_rejects_zero_vector() -> None:
    with pytest.raises(ValueError, match="zero vector"):
        angle_between_vectors([0, 0], [1, 0])


def test_dot_product_rejects_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="same number"):
        dot_product([1, 2], [1, 2, 3])
