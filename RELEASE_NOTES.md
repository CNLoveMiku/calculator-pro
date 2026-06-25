# Release Notes

## v3.0.0

IB Math Toolbox v3.0.0 upgrades `calculator-pro` into a portfolio-grade
IB Math + AI learning system.

### New Core Capabilities

- AI Explanation Engine
  - Generates intuitive explanations, formal mathematical solutions, and IB exam strategy tips.
  - Uses `OPENAI_API_KEY` when available.
  - Falls back automatically to rule-based explanations when no API key exists.
- Interactive Graph System
  - Accepts user-entered expressions such as `x^2 - 4`, `sin(x)`, and `exp(-x^2)`.
  - Plots function curve and numerical derivative curve.
  - Estimates roots, maxima, and minima.
  - Supports zoom-like replotting with additional graph panels.
- IB Math Study Mode
  - Adds a structured five-step study flow:
    concept introduction, guided example, practice question, solution check, reflection.
- Export System
  - Exports solution reports as PDF.
  - Includes problem statement, final answer, explanation, steps, and optional graph images.
- System Design Upgrade
  - Adds clean architecture layers: `core`, `ui`, `visualization`, `ai`, `export`, and `study`.
  - Introduces a reusable menu controller for CLI flow.

### Improvements Over v2.0.1

- Learning Mode now includes AI/rule-based explanations in addition to formula and derivation.
- Visualization supports user-entered functions and derivative analysis.
- Study Session mode supports educational product flow rather than isolated calculations only.
- PDF export turns solutions and graphs into reusable study artifacts.
- Test coverage expanded for AI fallback, expression safety, graph analysis, study sessions, and PDF export.

### Validation

- `python -m pytest`
- `python main.py`

### Compatibility

- Existing v2 calculation modules and imports remain available.
- CLI remains text-based.
- AI is optional; no API key is required for local use.

## v2.0.1 Quality Patch

Enhances the v2.0.0 educational experience without changing the public package
structure.

### Fixes and Enhancements

- Learning Mode now prints formula, derivation steps, and a short "why valid"
  explanation for each CLI calculation.
- Added Exam Mode for final-answer-only checking under exam-style conditions.
- Main CLI menu is grouped more intuitively around Algebra, Probability,
  Visualization, and Learning Mode Settings while keeping legacy tool menus.
- Function and polynomial plots can include tangent lines using derivative
  approximation.
- Function plots label key points such as endpoints, approximate intercepts,
  and tangent points.
- Matrix transformation visualization now shows separate BEFORE and AFTER
  geometric panels.
- Input handling is stricter for empty input, invalid matrix sizes, and
  non-numeric entries.
- Added tests for CLI Learning Mode and Exam Mode behavior.

## v2.0.0

IB Math AA HL ToolBox v2.0.0 upgrades the project from a calculation-focused
CLI into a more visual and simulation-ready educational toolbox.

## v1.0.0

Initial stable GitHub release of IB Math AA HL ToolBox.
