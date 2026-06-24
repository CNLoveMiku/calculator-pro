"""CLI mode behavior tests."""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _run_cli(user_input: str) -> str:
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=PROJECT_ROOT,
        input=user_input,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def test_learning_mode_prints_formula_derivation_and_why_valid() -> None:
    output = _run_cli("4\n1\n\n0\n5\n1\n1 2 3\n\n0\n0\n")

    assert "Learning mode ON" in output
    assert "Formula: mean = sum of values / number of values" in output
    assert "Derivation:" in output
    assert "Why valid:" in output


def test_exam_mode_hides_learning_steps() -> None:
    output = _run_cli("4\n2\n\n0\n5\n1\n1 2 3\n\n0\n0\n")

    assert "Exam mode ON" in output
    assert "mean = 2" in output
    assert "Derivation:" not in output
    assert "Why valid:" not in output
