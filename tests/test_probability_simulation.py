"""Tests for Monte Carlo probability simulation."""

import matplotlib

matplotlib.use("Agg")

import pytest

from calculator_pro.probability import (
    estimate_binomial_probability,
    monte_carlo_probability,
    plot_simulation_histogram,
    simulate_binomial_trials,
)


def test_monte_carlo_probability_with_certain_event() -> None:
    estimate = monte_carlo_probability(lambda rng: True, 10, seed=1)

    assert estimate == 1.0


def test_simulate_binomial_trials_with_certain_success() -> None:
    results = simulate_binomial_trials(3, 1.0, 5, seed=1)

    assert results == [3, 3, 3, 3, 3]


def test_estimate_binomial_probability_with_impossible_success() -> None:
    estimate = estimate_binomial_probability(3, 2, 0.0, 20, seed=1)

    assert estimate == 0.0


def test_simulation_rejects_invalid_trials() -> None:
    with pytest.raises(ValueError, match="positive"):
        simulate_binomial_trials(3, 0.5, 0)


def test_simulation_histogram_saves_file(tmp_path) -> None:
    output_path = tmp_path / "histogram.png"

    figure = plot_simulation_histogram([0, 1, 1, 2], output_path=output_path)

    assert output_path.exists()
    assert len(figure.axes) == 1
