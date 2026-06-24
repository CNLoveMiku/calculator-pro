"""Monte Carlo probability simulations."""

from collections.abc import Callable, Sequence
from pathlib import Path
import random

from matplotlib import pyplot as plt
from matplotlib.figure import Figure


def monte_carlo_probability(
    experiment: Callable[[random.Random], bool],
    trials: int,
    *,
    seed: int | None = None,
) -> float:
    """Estimate probability with repeated random trials.

    Formula:
        estimated probability = successful trials / total trials

    Plain English:
        Run the same random experiment many times and count how often the event
        happens. More trials usually produce a better estimate.
    """
    _validate_trials(trials)
    if not callable(experiment):
        raise TypeError("experiment must be callable.")

    rng = random.Random(seed)
    successes = 0
    for _ in range(trials):
        if experiment(rng):
            successes += 1

    return successes / trials


def simulate_binomial_trials(
    n: int,
    p: float,
    trials: int,
    *,
    seed: int | None = None,
) -> list[int]:
    """Simulate binomial trials and return the success count from each run.

    Formula:
        X is the number of successes in n independent Bernoulli trials.

    Plain English:
        Repeat an n-trial experiment many times, where each trial has success
        probability p, and record how many successes occurred each time.
    """
    _validate_binomial_inputs(n, p)
    _validate_trials(trials)

    rng = random.Random(seed)
    results: list[int] = []
    for _ in range(trials):
        successes = sum(1 for _ in range(n) if rng.random() < p)
        results.append(successes)

    return results


def estimate_binomial_probability(
    n: int,
    k: int,
    p: float,
    trials: int,
    *,
    seed: int | None = None,
) -> float:
    """Estimate P(X = k) for a binomial model using Monte Carlo simulation."""
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if k < 0 or k > n:
        raise ValueError("k must be between 0 and n.")

    results = simulate_binomial_trials(n, p, trials, seed=seed)
    return sum(1 for result in results if result == k) / trials


def plot_simulation_histogram(
    values: Sequence[int | float],
    *,
    bins: int | None = None,
    title: str = "Monte Carlo simulation histogram",
    output_path: str | Path | None = None,
    show: bool = False,
) -> Figure:
    """Plot a histogram from simulation output.

    Formula:
        Histogram bars count how often values fall into each interval.

    Plain English:
        A histogram lets you see the shape of the simulated results.
    """
    data = list(values)
    if not data:
        raise ValueError("At least one simulated value is required.")
    for value in data:
        if not isinstance(value, int | float):
            raise TypeError("Simulation values must be numeric.")

    figure, axis = plt.subplots()
    axis.hist(data, bins=bins or "auto", edgecolor="black", alpha=0.75)
    axis.set_title(title)
    axis.set_xlabel("Value")
    axis.set_ylabel("Frequency")
    axis.grid(True, axis="y", alpha=0.3)
    figure.tight_layout()

    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(path)
    if show:
        plt.show()

    return figure


def _validate_trials(trials: int) -> None:
    """Validate trial count."""
    if not isinstance(trials, int):
        raise TypeError("trials must be an integer.")
    if trials <= 0:
        raise ValueError("trials must be positive.")


def _validate_binomial_inputs(n: int, p: float) -> None:
    """Validate binomial simulation parameters."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    if not isinstance(p, int | float):
        raise TypeError("p must be numeric.")
    if p < 0 or p > 1:
        raise ValueError("p must be between 0 and 1.")
