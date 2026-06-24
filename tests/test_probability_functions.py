"""Tests for probability and combinatorics functions."""

import pytest

from calculator_pro.probability import (
    binomial_probability,
    combinations,
    conditional_probability,
    factorial,
    permutations,
)


def test_factorial_positive_number() -> None:
    assert factorial(5) == 120


def test_factorial_zero() -> None:
    assert factorial(0) == 1


def test_permutations() -> None:
    assert permutations(5, 2) == 20


def test_combinations() -> None:
    assert combinations(5, 2) == 10


def test_conditional_probability() -> None:
    assert conditional_probability(0.2, 0.5) == pytest.approx(0.4)


def test_binomial_probability() -> None:
    assert binomial_probability(5, 2, 0.4) == pytest.approx(0.3456)


def test_binomial_probability_all_failures() -> None:
    assert binomial_probability(3, 0, 0.25) == pytest.approx(0.421875)


def test_factorial_rejects_negative_number() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-1)


def test_factorial_rejects_non_integer() -> None:
    with pytest.raises(TypeError, match="integer"):
        factorial(3.5)  # type: ignore[arg-type]


def test_permutations_rejects_r_greater_than_n() -> None:
    with pytest.raises(ValueError, match="less than or equal"):
        permutations(3, 4)


def test_combinations_rejects_negative_r() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        combinations(3, -1)


def test_conditional_probability_rejects_zero_denominator() -> None:
    with pytest.raises(ValueError, match="greater than 0"):
        conditional_probability(0, 0)


def test_conditional_probability_rejects_invalid_probability() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        conditional_probability(1.2, 0.5)


def test_conditional_probability_rejects_impossible_intersection() -> None:
    with pytest.raises(ValueError, match="cannot be greater"):
        conditional_probability(0.8, 0.5)


def test_binomial_probability_rejects_negative_trials() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        binomial_probability(-1, 0, 0.5)


def test_binomial_probability_rejects_invalid_success_count() -> None:
    with pytest.raises(ValueError, match="between 0 and n"):
        binomial_probability(3, 4, 0.5)


def test_binomial_probability_rejects_invalid_success_probability() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        binomial_probability(3, 1, -0.1)
