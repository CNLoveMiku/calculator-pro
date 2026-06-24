"""Probability and combinatorics tools."""

from calculator_pro.probability.combinatorics import (
    combinations,
    factorial,
    permutations,
)
from calculator_pro.probability.probability import (
    binomial_probability,
    conditional_probability,
)
from calculator_pro.probability.simulation import (
    estimate_binomial_probability,
    monte_carlo_probability,
    plot_simulation_histogram,
    simulate_binomial_trials,
)

__all__ = [
    "binomial_probability",
    "combinations",
    "conditional_probability",
    "estimate_binomial_probability",
    "factorial",
    "monte_carlo_probability",
    "permutations",
    "plot_simulation_histogram",
    "simulate_binomial_trials",
]
