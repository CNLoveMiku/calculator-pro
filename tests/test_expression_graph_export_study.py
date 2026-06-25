"""Tests for v3 expression, graph, export, and study systems."""

import matplotlib

matplotlib.use("Agg")

from calculator_pro.core import compile_math_expression
from calculator_pro.export import SolutionReport, export_solution_pdf
from calculator_pro.study import create_study_session
from calculator_pro.visualization import plot_expression_analysis


def test_compile_math_expression_supports_common_math() -> None:
    function = compile_math_expression("x^2 - 4")

    assert function(3) == 5.0


def test_compile_math_expression_rejects_unsafe_names() -> None:
    try:
        compile_math_expression("__import__('os').system('echo bad')")
    except ValueError as error:
        assert "Unsupported" in str(error) or "approved" in str(error)
    else:
        raise AssertionError("Unsafe expression was accepted.")


def test_plot_expression_analysis_saves_graph_and_detects_roots(tmp_path) -> None:
    output_path = tmp_path / "analysis.png"

    figure, analysis = plot_expression_analysis(
        "x^2 - 4",
        -4,
        4,
        output_path=output_path,
        zoom_ranges=[(-3, 0)],
    )

    assert output_path.exists()
    assert len(figure.axes) == 2
    assert any(abs(root - 2) < 0.1 for root in analysis.roots)
    assert any(abs(root + 2) < 0.1 for root in analysis.roots)


def test_create_study_session_has_five_step_flow() -> None:
    session = create_study_session("vectors")

    assert session.topic == "vectors"
    assert [step.title for step in session.steps] == [
        "Concept introduction",
        "Guided example",
        "Practice question",
        "Solution check",
        "Reflection question",
    ]


def test_export_solution_pdf_creates_file(tmp_path) -> None:
    output_path = tmp_path / "report.pdf"
    report = SolutionReport(
        title="Vector magnitude",
        problem="Find |<3,4>|",
        answer="5",
        explanation="Use Pythagoras.",
        steps=["Square components.", "Add and square root."],
    )

    path = export_solution_pdf(report, output_path)

    assert path.exists()
    assert path.stat().st_size > 0
