"""Tests for matplotlib visualizations."""

import matplotlib

matplotlib.use("Agg")

import pytest

from calculator_pro.visualization import (
    plot_function,
    plot_matrix_transformation,
    plot_polynomial,
)


def test_plot_function_saves_file(tmp_path) -> None:
    output_path = tmp_path / "function.png"

    figure = plot_function(lambda x: x**2, -2, 2, output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 1


def test_plot_polynomial_saves_file(tmp_path) -> None:
    output_path = tmp_path / "polynomial.png"

    figure = plot_polynomial([1, 0, 0], -2, 2, output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 1


def test_plot_matrix_transformation_saves_file(tmp_path) -> None:
    output_path = tmp_path / "matrix.png"

    figure = plot_matrix_transformation([[1, 0], [0, 1]], output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 1


def test_plot_function_rejects_invalid_range() -> None:
    with pytest.raises(ValueError, match="less than"):
        plot_function(lambda x: x, 2, 2)
