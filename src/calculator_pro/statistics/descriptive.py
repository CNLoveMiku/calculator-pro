"""Simple descriptive statistics for calculator-pro."""

from collections.abc import Sequence
from math import sqrt


def mean(values: Sequence[float]) -> float:
    """Calculate the arithmetic mean.

    Formula:
        mean = (sum of all values) / (number of values)

    Plain English:
        Add all values, then divide by how many values there are.
    """
    data = _validate_data(values)
    return sum(data) / len(data)


def variance(values: Sequence[float], sample: bool = False) -> float:
    """Calculate variance.

    Formula:
        Population variance = sum((x - mean)^2) / n
        Sample variance = sum((x - mean)^2) / (n - 1)

    Plain English:
        Variance measures how spread out the data is from the mean.
    """
    data = _validate_data(values)

    if sample and len(data) < 2:
        raise ValueError("Sample variance requires at least two values.")

    average = mean(data)
    squared_differences = [(value - average) ** 2 for value in data]
    divisor = len(data) - 1 if sample else len(data)
    return sum(squared_differences) / divisor


def standard_deviation(values: Sequence[float], sample: bool = False) -> float:
    """Calculate standard deviation.

    Formula:
        standard deviation = square root of variance

    Plain English:
        Standard deviation is the typical distance from the mean, measured in
        the same units as the original data.
    """
    return sqrt(variance(values, sample=sample))


def _validate_data(values: Sequence[float]) -> list[float]:
    """Return numeric data as floats, or raise an error."""
    data = list(values)

    if not data:
        raise ValueError("At least one value is required.")

    for value in data:
        if not isinstance(value, int | float):
            raise TypeError("All values must be numeric.")

    return [float(value) for value in data]
