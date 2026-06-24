"""Tests for matrix operations."""

import pytest

from calculator_pro.matrix import add, determinant, inverse, multiply


def test_add_matrices() -> None:
    result = add([[1, 2], [3, 4]], [[5, 6], [7, 8]])

    assert result == [[6.0, 8.0], [10.0, 12.0]]


def test_multiply_matrices() -> None:
    result = multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])

    assert result == [[19.0, 22.0], [43.0, 50.0]]


def test_determinant_2_by_2() -> None:
    result = determinant([[1, 2], [3, 4]])

    assert result == -2.0


def test_determinant_3_by_3() -> None:
    result = determinant([[6, 1, 1], [4, -2, 5], [2, 8, 7]])

    assert result == -306.0


def test_inverse_2_by_2() -> None:
    result = inverse([[4, 7], [2, 6]])

    assert result == [[0.6, -0.7], [-0.2, 0.4]]


def test_inverse_identity_matrix() -> None:
    result = inverse([[1, 0], [0, 1]])

    assert result == [[1.0, 0.0], [0.0, 1.0]]


def test_add_rejects_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="same dimensions"):
        add([[1, 2]], [[1], [2]])


def test_multiply_rejects_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="columns"):
        multiply([[1, 2]], [[1, 2]])


def test_determinant_rejects_non_square_matrix() -> None:
    with pytest.raises(ValueError, match="square"):
        determinant([[1, 2, 3], [4, 5, 6]])


def test_inverse_rejects_singular_matrix() -> None:
    with pytest.raises(ValueError, match="singular"):
        inverse([[1, 2], [2, 4]])


def test_matrix_rejects_empty_matrix() -> None:
    with pytest.raises(ValueError, match="at least one row"):
        add([], [])


def test_matrix_rejects_non_numeric_values() -> None:
    with pytest.raises(TypeError, match="numeric"):
        determinant([[1, "x"], [3, 4]])  # type: ignore[list-item]
