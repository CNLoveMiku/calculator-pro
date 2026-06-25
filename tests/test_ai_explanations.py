"""Tests for AI explanation fallback behavior."""

from calculator_pro.ai import AIExplanationEngine


def test_ai_engine_uses_rule_based_fallback_without_api_key(monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    engine = AIExplanationEngine(api_key=None)

    explanation = engine.explain(
        topic="vectors",
        problem="Find |<3,4>|",
        answer="5",
        formula="|a| = sqrt(a1^2 + a2^2)",
        steps=[("Square and add components.", "Pythagoras applies to vector length.")],
    )

    assert explanation.source == "rule-based"
    assert "vectors" in explanation.intuitive
    assert "5" in explanation.formal_solution
    assert "IB Math AA HL" in explanation.exam_strategy_tip
