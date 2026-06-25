"""Optional AI explanation layer with rule-based fallback."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from urllib import request


@dataclass(frozen=True)
class AIExplanation:
    """Structured explanation suitable for IB Math AA HL learning."""

    intuitive: str
    formal_solution: str
    exam_strategy_tip: str
    source: str = "rule-based"


class AIExplanationEngine:
    """Generate explanations using an API key when available, otherwise fallback."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        model: str = "gpt-4o-mini",
        timeout_seconds: int = 20,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.timeout_seconds = timeout_seconds

    def explain(
        self,
        *,
        topic: str,
        problem: str,
        answer: str,
        formula: str,
        steps: list[tuple[str, str]],
    ) -> AIExplanation:
        """Return intuitive, formal, and exam-strategy explanations."""
        fallback = self._rule_based_explanation(topic, problem, answer, formula, steps)
        if not self.api_key:
            return fallback

        try:
            return self._openai_explanation(topic, problem, answer, formula, steps)
        except Exception:
            return fallback

    def _rule_based_explanation(
        self,
        topic: str,
        problem: str,
        answer: str,
        formula: str,
        steps: list[tuple[str, str]],
    ) -> AIExplanation:
        derivation = " ".join(step for step, _ in steps)
        reasons = " ".join(reason for _, reason in steps)
        return AIExplanation(
            intuitive=(
                f"For {topic}, focus on what the quantities represent before calculating. "
                f"Here, the problem is: {problem}."
            ),
            formal_solution=(
                f"Use {formula}. {derivation} Therefore the final answer is {answer}. "
                f"The method is valid because {reasons}"
            ),
            exam_strategy_tip=(
                "In an IB Math AA HL response, state the formula first, substitute values "
                "clearly, keep exact values where possible, and check that the answer has "
                "the expected domain or units."
            ),
        )

    def _openai_explanation(
        self,
        topic: str,
        problem: str,
        answer: str,
        formula: str,
        steps: list[tuple[str, str]],
    ) -> AIExplanation:
        prompt = {
            "topic": topic,
            "problem": problem,
            "answer": answer,
            "formula": formula,
            "steps": [{"step": step, "why_valid": why} for step, why in steps],
            "instruction": (
                "Return concise JSON with keys intuitive, formal_solution, "
                "exam_strategy_tip for IB Math AA HL students."
            ),
        }
        payload = json.dumps(
            {
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an IB Math AA HL tutor. Return valid JSON only.",
                    },
                    {"role": "user", "content": json.dumps(prompt)},
                ],
                "temperature": 0.2,
            }
        ).encode("utf-8")
        api_request = request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with request.urlopen(api_request, timeout=self.timeout_seconds) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        return AIExplanation(
            intuitive=parsed["intuitive"],
            formal_solution=parsed["formal_solution"],
            exam_strategy_tip=parsed["exam_strategy_tip"],
            source="ai",
        )
