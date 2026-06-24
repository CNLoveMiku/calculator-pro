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


def test_plot_function_can_include_tangent_line(tmp_path) -> None:
    output_path = tmp_path / "function_tangent.png"

    figure = plot_function(
        lambda x: x**2,
        -2,
        2,
        derivative_at=1,
        output_path=output_path,
    )

    assert output_path.exists()
    assert len(figure.axes[0].lines) >= 2


def test_plot_polynomial_saves_file(tmp_path) -> None:
    output_path = tmp_path / "polynomial.png"

    figure = plot_polynomial([1, 0, 0], -2, 2, output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 1


def test_plot_matrix_transformation_saves_file(tmp_path) -> None:
    output_path = tmp_path / "matrix.png"

    figure = plot_matrix_transformation([[1, 0], [0, 1]], output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 2
    assert figure.axes[0].get_title().startswith("BEFORE")
    assert figure.axes[1].get_title().startswith("AFTER")


def test_plot_function_rejects_invalid_range() -> None:
    with pytest.raises(ValueError, match="less than"):
        plot_function(lambda x: x, 2, 2)
