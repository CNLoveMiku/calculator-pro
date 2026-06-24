"""Matplotlib visualizations for IB Math AA HL topics."""

from collections.abc import Callable, Sequence
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from calculator_pro.functions import evaluate_polynomial
from calculator_pro.matrix.types import Matrix


def plot_function(
    function: Callable[[float], float],
    x_min: float,
    x_max: float,
    *,
    points: int = 200,
    derivative_at: float | None = None,
    derivative_step: float = 1e-5,
    title: str = "Function graph",
    output_path: str | Path | None = None,
    show: bool = False,
) -> Figure:
    """Plot y = f(x) over a chosen interval.

    Formula:
        y = f(x)

    Plain English:
        Choose many x-values between x_min and x_max, calculate the matching
        y-values, then draw the curve.
    """
    _validate_plot_range(x_min, x_max, points)
    if not callable(function):
        raise TypeError("function must be callable.")

    x_values = _linspace(x_min, x_max, points)
    y_values = [function(x_value) for x_value in x_values]

    figure, axis = plt.subplots()
    axis.plot(x_values, y_values, label="y = f(x)")
    axis.axhline(0, color="black", linewidth=0.8)
    axis.axvline(0, color="black", linewidth=0.8)
    _label_key_points(axis, x_values, y_values)

    if derivative_at is not None:
        if derivative_at < x_min or derivative_at > x_max:
            raise ValueError("derivative_at must lie within the plotting interval.")
        if derivative_step <= 0:
            raise ValueError("derivative_step must be positive.")
        tangent_y = function(derivative_at)
        slope = (function(derivative_at + derivative_step) - function(derivative_at - derivative_step)) / (
            2 * derivative_step
        )
        tangent_values = [
            slope * (x_value - derivative_at) + tangent_y for x_value in x_values
        ]
        axis.plot(x_values, tangent_values, linestyle="--", label="tangent line")
        axis.scatter([derivative_at], [tangent_y], color="tab:red", zorder=5)
        axis.annotate(
            f"tangent at x={derivative_at:.3g}",
            (derivative_at, tangent_y),
            textcoords="offset points",
            xytext=(8, 8),
        )

    axis.grid(True, alpha=0.3)
    axis.set_title(title)
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.legend()

    _finish_plot(figure, output_path, show)
    return figure


def plot_polynomial(
    coefficients: Sequence[float],
    x_min: float,
    x_max: float,
    *,
    points: int = 200,
    derivative_at: float | None = None,
    derivative_step: float = 1e-5,
    output_path: str | Path | None = None,
    show: bool = False,
) -> Figure:
    """Plot a polynomial graph.

    Formula:
        For coefficients [a, b, c], y = ax^2 + bx + c.

    Plain English:
        Evaluate the polynomial at many x-values, then draw the resulting
        points as a smooth curve.
    """
    if not coefficients:
        raise ValueError("At least one coefficient is required.")

    return plot_function(
        lambda x_value: evaluate_polynomial(coefficients, x_value),
        x_min,
        x_max,
        points=points,
        derivative_at=derivative_at,
        derivative_step=derivative_step,
        title="Polynomial graph",
        output_path=output_path,
        show=show,
    )


def plot_matrix_transformation(
    matrix: Matrix,
    *,
    output_path: str | Path | None = None,
    show: bool = False,
) -> Figure:
    """Visualize a 2x2 matrix transformation on basis vectors and a unit square.

    Formula:
        A transforms each point v into Av.

    Plain English:
        The plot shows where the original basis vectors and unit square move
        after multiplying by the matrix.
    """
    values = _validate_2_by_2_matrix(matrix)
    original_square = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]
    transformed_square = [_apply_2_by_2(values, point) for point in original_square]

    figure, axes = plt.subplots(1, 2, figsize=(10, 4))
    before_axis, after_axis = axes

    _draw_transformation_panel(
        before_axis,
        original_square,
        (1.0, 0.0),
        (0.0, 1.0),
        "BEFORE: original shape",
        "gray",
    )
    _draw_transformation_panel(
        after_axis,
        transformed_square,
        _apply_2_by_2(values, (1.0, 0.0)),
        _apply_2_by_2(values, (0.0, 1.0)),
        "AFTER: transformed by A",
        "tab:blue",
    )

    figure.suptitle("2x2 matrix transformation: before and after")

    _finish_plot(figure, output_path, show)
    return figure


def _validate_plot_range(x_min: float, x_max: float, points: int) -> None:
    """Validate numeric plot inputs."""
    if not isinstance(x_min, int | float) or not isinstance(x_max, int | float):
        raise TypeError("x_min and x_max must be numeric.")
    if x_min >= x_max:
        raise ValueError("x_min must be less than x_max.")
    if not isinstance(points, int):
        raise TypeError("points must be an integer.")
    if points < 2:
        raise ValueError("points must be at least 2.")


def _validate_2_by_2_matrix(matrix: Matrix) -> list[list[float]]:
    """Return a 2x2 numeric matrix as floats."""
    values = [list(row) for row in matrix]
    if len(values) != 2 or any(len(row) != 2 for row in values):
        raise ValueError("Matrix transformation visualization requires a 2x2 matrix.")
    for row in values:
        for value in row:
            if not isinstance(value, int | float):
                raise TypeError("Matrix values must be numeric.")
    return [[float(value) for value in row] for row in values]


def _linspace(start: float, stop: float, points: int) -> list[float]:
    """Create evenly spaced values without requiring NumPy."""
    step = (stop - start) / (points - 1)
    return [start + index * step for index in range(points)]


def _apply_2_by_2(matrix: list[list[float]], point: tuple[float, float]) -> tuple[float, float]:
    """Apply a 2x2 matrix to a 2D point."""
    x_value, y_value = point
    return (
        matrix[0][0] * x_value + matrix[0][1] * y_value,
        matrix[1][0] * x_value + matrix[1][1] * y_value,
    )


def _plot_polygon(axis: object, points: list[tuple[float, float]], label: str, color: str) -> None:
    """Plot a closed polygon on an axis."""
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    axis.plot(x_values, y_values, marker="o", label=label, color=color)


def _label_key_points(axis: object, x_values: list[float], y_values: list[float]) -> None:
    """Label endpoints and approximate x-intercepts on a function plot."""
    key_points = [
        ("start", x_values[0], y_values[0]),
        ("end", x_values[-1], y_values[-1]),
    ]

    for index in range(1, len(x_values)):
        previous_y = y_values[index - 1]
        current_y = y_values[index]
        if previous_y == 0 or previous_y * current_y < 0:
            key_points.append(("x-intercept", x_values[index], y_values[index]))
            if len(key_points) >= 5:
                break

    for label, x_value, y_value in key_points:
        axis.scatter([x_value], [y_value], zorder=4)
        axis.annotate(
            label,
            (x_value, y_value),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=8,
        )


def _draw_transformation_panel(
    axis: object,
    square: list[tuple[float, float]],
    i_vector: tuple[float, float],
    j_vector: tuple[float, float],
    title: str,
    color: str,
) -> None:
    """Draw one before/after panel for a 2D matrix transformation."""
    _plot_polygon(axis, square, "shape", color)
    axis.quiver(0, 0, *i_vector, angles="xy", scale_units="xy", scale=1, color="tab:red", label="i vector")
    axis.quiver(0, 0, *j_vector, angles="xy", scale_units="xy", scale=1, color="tab:green", label="j vector")
    axis.axhline(0, color="black", linewidth=0.8)
    axis.axvline(0, color="black", linewidth=0.8)
    axis.grid(True, alpha=0.3)
    axis.set_aspect("equal", adjustable="box")
    axis.set_title(title)
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.legend()
    axis.relim()
    axis.autoscale_view()


def _finish_plot(
    figure: Figure,
    output_path: str | Path | None,
    show: bool,
) -> None:
    """Save and/or display a matplotlib figure."""
    figure.tight_layout()
    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(path)
    if show:
        plt.show()
