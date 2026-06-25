"""Interactive-style graph analysis for user-entered functions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from calculator_pro.core import compile_math_expression


@dataclass(frozen=True)
class GraphAnalysis:
    """Key graph features estimated numerically."""

    roots: list[float]
    maxima: list[tuple[float, float]]
    minima: list[tuple[float, float]]


def plot_expression_analysis(
    expression: str,
    x_min: float,
    x_max: float,
    *,
    points: int = 400,
    output_path: str | Path | None = None,
    zoom_ranges: list[tuple[float, float]] | None = None,
    show: bool = False,
) -> tuple[Figure, GraphAnalysis]:
    """Plot f(x), f'(x), roots, extrema, and optional zoom panels."""
    function = compile_math_expression(expression)
    _validate_range(x_min, x_max, points)
    ranges = [(x_min, x_max)] + (zoom_ranges or [])

    figure, axes = plt.subplots(len(ranges), 1, figsize=(8, 4 * len(ranges)))
    if len(ranges) == 1:
        axes = [axes]

    full_analysis: GraphAnalysis | None = None
    for axis, (start, stop) in zip(axes, ranges):
        x_values = _linspace(start, stop, points)
        y_values = [function(x_value) for x_value in x_values]
        derivative_values = [_central_difference(function, x_value) for x_value in x_values]
        analysis = _analyze_graph(x_values, y_values, derivative_values)
        if full_analysis is None:
            full_analysis = analysis

        axis.plot(x_values, y_values, label=f"f(x) = {expression}")
        axis.plot(x_values, derivative_values, linestyle="--", label="f'(x)")
        axis.axhline(0, color="black", linewidth=0.8)
        axis.axvline(0, color="black", linewidth=0.8)
        _mark_roots(axis, function, analysis.roots)
        _mark_extrema(axis, analysis.maxima, "max", "tab:red")
        _mark_extrema(axis, analysis.minima, "min", "tab:green")
        axis.grid(True, alpha=0.3)
        axis.set_title(f"Graph analysis on [{start:g}, {stop:g}]")
        axis.set_xlabel("x")
        axis.set_ylabel("y")
        axis.legend()

    figure.tight_layout()
    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(path)
    if show:
        plt.show()

    if full_analysis is None:
        full_analysis = GraphAnalysis([], [], [])
    return figure, full_analysis


def _analyze_graph(
    x_values: list[float],
    y_values: list[float],
    derivative_values: list[float],
) -> GraphAnalysis:
    roots = _estimate_zero_crossings(x_values, y_values)
    derivative_roots = _estimate_zero_crossings(x_values, derivative_values)
    maxima: list[tuple[float, float]] = []
    minima: list[tuple[float, float]] = []

    for root in derivative_roots:
        left_derivative = _nearest_value(x_values, derivative_values, root - 1e-3)
        right_derivative = _nearest_value(x_values, derivative_values, root + 1e-3)
        y_value = _nearest_value(x_values, y_values, root)
        if left_derivative > 0 and right_derivative < 0:
            maxima.append((root, y_value))
        elif left_derivative < 0 and right_derivative > 0:
            minima.append((root, y_value))

    return GraphAnalysis(roots=roots[:5], maxima=maxima[:5], minima=minima[:5])


def _estimate_zero_crossings(x_values: list[float], y_values: list[float]) -> list[float]:
    roots: list[float] = []
    for index in range(1, len(x_values)):
        y0 = y_values[index - 1]
        y1 = y_values[index]
        if y0 == 0:
            roots.append(x_values[index - 1])
        elif y0 * y1 < 0:
            x0 = x_values[index - 1]
            x1 = x_values[index]
            roots.append(x0 - y0 * (x1 - x0) / (y1 - y0))
    return roots


def _central_difference(function: object, x_value: float, step: float = 1e-5) -> float:
    return (function(x_value + step) - function(x_value - step)) / (2 * step)


def _nearest_value(x_values: list[float], y_values: list[float], x_target: float) -> float:
    index = min(range(len(x_values)), key=lambda i: abs(x_values[i] - x_target))
    return y_values[index]


def _mark_roots(axis: object, function: object, roots: list[float]) -> None:
    for root in roots:
        axis.scatter([root], [0], color="black", zorder=5)
        axis.annotate("root", (root, 0), textcoords="offset points", xytext=(6, 6), fontsize=8)


def _mark_extrema(
    axis: object,
    points: list[tuple[float, float]],
    label: str,
    color: str,
) -> None:
    for x_value, y_value in points:
        axis.scatter([x_value], [y_value], color=color, zorder=5)
        axis.annotate(label, (x_value, y_value), textcoords="offset points", xytext=(6, 6), fontsize=8)


def _linspace(start: float, stop: float, points: int) -> list[float]:
    step = (stop - start) / (points - 1)
    return [start + index * step for index in range(points)]


def _validate_range(x_min: float, x_max: float, points: int) -> None:
    if not isinstance(x_min, int | float) or not isinstance(x_max, int | float):
        raise TypeError("x_min and x_max must be numeric.")
    if x_min >= x_max:
        raise ValueError("x_min must be less than x_max.")
    if points < 3:
        raise ValueError("points must be at least 3.")
