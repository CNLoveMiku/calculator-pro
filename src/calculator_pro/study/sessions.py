"""Structured IB Math AA HL study sessions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class StudyStep:
    """One stage in a guided study flow."""

    title: str
    prompt: str


@dataclass(frozen=True)
class StudySession:
    """A five-step IB Math study session."""

    topic: str
    steps: list[StudyStep]


def create_study_session(topic: str) -> StudySession:
    """Create a structured study flow for a chosen topic."""
    normalized = topic.strip() or "binomial probability"
    templates = {
        "binomial probability": _binomial_session,
        "vectors": _vector_session,
        "polynomial graphs": _polynomial_session,
    }
    builder = templates.get(normalized.lower(), _generic_session)
    return builder(normalized)


def _binomial_session(topic: str) -> StudySession:
    return StudySession(
        topic=topic,
        steps=[
            StudyStep("Concept introduction", "A binomial model counts successes in fixed independent trials."),
            StudyStep("Guided example", "Example: For X ~ B(5, 0.4), calculate P(X = 2)."),
            StudyStep("Practice question", "Try: For X ~ B(8, 0.25), calculate P(X = 3)."),
            StudyStep("Solution check", "Use nCk p^k (1-p)^(n-k), then compare with your calculator result."),
            StudyStep("Reflection question", "How would the distribution change if p increased?"),
        ],
    )


def _vector_session(topic: str) -> StudySession:
    return StudySession(
        topic=topic,
        steps=[
            StudyStep("Concept introduction", "Vectors encode magnitude and direction using components."),
            StudyStep("Guided example", "Example: Find a . b for a=<1,2,3> and b=<4,5,6>."),
            StudyStep("Practice question", "Try: Find the angle between <1,0> and <1,1>."),
            StudyStep("Solution check", "Use cos(theta)=(a.b)/(|a||b|) and check the angle is sensible."),
            StudyStep("Reflection question", "What does a zero dot product imply geometrically?"),
        ],
    )


def _polynomial_session(topic: str) -> StudySession:
    return StudySession(
        topic=topic,
        steps=[
            StudyStep("Concept introduction", "Polynomial graphs connect algebraic roots, turning points, and end behavior."),
            StudyStep("Guided example", "Example: Sketch y=x^2-4 and identify roots."),
            StudyStep("Practice question", "Try: Sketch y=x^3-3x and estimate stationary points."),
            StudyStep("Solution check", "Compare roots, derivative signs, and plotted key points."),
            StudyStep("Reflection question", "How does the leading coefficient affect end behavior?"),
        ],
    )


def _generic_session(topic: str) -> StudySession:
    return StudySession(
        topic=topic,
        steps=[
            StudyStep("Concept introduction", f"State the key definition or formula for {topic}."),
            StudyStep("Guided example", "Work one example slowly, naming each substitution."),
            StudyStep("Practice question", "Create a similar question and solve it without notes."),
            StudyStep("Solution check", "Compare your method, not only your final answer."),
            StudyStep("Reflection question", "What error would be easiest to make under exam pressure?"),
        ],
    )
