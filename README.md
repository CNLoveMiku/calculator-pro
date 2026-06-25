# IB Math AA HL ToolBox

`calculator-pro` is now a portfolio-grade **IB Math + AI learning system**.
It began as a clean command-line calculator and has grown into a structured
learning tool for IB Mathematics: Analysis and Approaches HL students.

The design goal is simple: do not just output answers. Help students see the
idea, the formal method, the exam strategy, and the graph or report that makes
the solution reusable.

## Project Story

Version 1.0.0 introduced a modular calculator for matrices, functions,
probability, vectors, and statistics.

Version 2.0.0 added visualization, Monte Carlo simulation, and a stronger
learning mode.

Version 3.0.0 turns the project into an AI-assisted education product:

- optional AI explanations with rule-based fallback
- interactive function graph analysis
- IB Math Study Session flow
- PDF solution reports
- cleaner architecture layers for `core`, `ui`, `visualization`, `ai`, and `export`

## Learning Philosophy

The toolbox is built around five learning principles:

1. **Concept before computation**: students should understand what a formula
   means before substituting values.
2. **Formal method matters**: solutions show valid mathematical steps suitable
   for IB-style work.
3. **Strategy is teachable**: each AI explanation includes an IB exam tip.
4. **Graphs are evidence**: visualizations expose roots, derivatives, extrema,
   and transformations.
5. **Reflection improves transfer**: study sessions end with reflection prompts
   so students generalize beyond one question.

## v3.0.0 Features

### AI Explanation Engine

For each learning-mode calculation, the system can generate:

- intuitive explanation
- formal mathematical solution
- IB exam strategy tip

If `OPENAI_API_KEY` is not available, the engine automatically uses a
rule-based fallback, so the project remains fully usable offline.

### Interactive Graph System

Students can enter expressions such as:

```text
x^2 - 4
sin(x)
exp(-x^2)
```

The graph system plots:

- `f(x)`
- numerical derivative curve `f'(x)`
- estimated roots
- estimated maxima and minima
- optional zoom panels

### IB Math Study Mode

Study Session mode follows a five-step learning flow:

1. Concept introduction
2. Guided example
3. Practice question
4. Solution check
5. Reflection question

Built-in study topics include binomial probability, vectors, and polynomial
graphs. Custom topics use a generic IB revision structure.

### Export System

PDF reports can include:

- problem statement
- final answer
- explanation
- solution steps
- graph images

This makes it useful for revision logs, tutor feedback, or a portfolio demo.

## IB Math AA HL Relevance

- Algebra and functions: polynomial evaluation, graphing, roots, and turning points
- Calculus: derivative approximation, tangent lines, and gradient interpretation
- Probability: combinatorics, conditional probability, binomial models, simulation
- Vectors: dot product, cross product, magnitude, and angle
- Statistics: mean, variance, standard deviation, and distribution shape
- Matrices: operations, determinants, inverses, and geometric transformations

## Screenshots / ASCII Preview

Main menu:

```text
IB Math AA HL ToolBox
---------------------
Mode: Fast mode
1. Algebra tools
2. Probability tools
3. Visualization
4. Learning mode settings
5. Statistics tools
6. Matrix tools
7. Vector tools
8. Study Session
9. Export PDF report
0. Exit
```

Learning mode output:

```text
Formula: P(X = k) = nCk x p^k x (1 - p)^(n - k)
Derivation:
1. Count success positions using 5C2.
   Why valid: Exactly k successes can occur in that many unordered positions among n trials.

AI explanation layer (rule-based)
Intuitive explanation: ...
Formal mathematical solution: ...
IB exam strategy tip: ...
```

Interactive graph analysis:

```text
expression -> f(x) curve -> derivative curve -> roots/extrema -> zoom panel -> PNG
 x^2 - 4       parabola        line 2x          x = -2, 2       [-3, 0]
```

Matrix transformation:

```text
BEFORE panel              matrix A      AFTER panel
 (0,1)----(1,1)             [a b]          A(0,1)----A(1,1)
   |        |       -->     [c d]     -->    |          |
 (0,0)----(1,0)                            A(0,0)----A(1,0)
```

## Installation

```bash
git clone https://github.com/CNLoveMiku/calculator-pro.git
cd calculator-pro
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Optional editable install:

```bash
pip install -e .
```

Optional AI:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Without the key, rule-based explanations are used automatically.

## Usage

Run the CLI:

```bash
python main.py
```

Run tests:

```bash
python -m pytest
```

Python API example:

```python
from calculator_pro.ai import AIExplanationEngine
from calculator_pro.visualization import plot_expression_analysis
from calculator_pro.export import SolutionReport, export_solution_pdf

plot_expression_analysis("x^2 - 4", -5, 5, output_path="outputs/graph.png")

engine = AIExplanationEngine()
explanation = engine.explain(
    topic="polynomial graphs",
    problem="Find the roots of x^2 - 4",
    answer="x = -2, 2",
    formula="x^2 - 4 = 0",
    steps=[("Factor as (x-2)(x+2)=0.", "Difference of squares.")],
)

export_solution_pdf(
    SolutionReport(
        title="Polynomial roots",
        problem="Find the roots of x^2 - 4",
        answer="x = -2, 2",
        explanation=explanation.formal_solution,
        steps=["Set y = 0.", "Factor.", "Solve each factor."],
        graph_paths=["outputs/graph.png"],
    ),
    "outputs/report.pdf",
)
```

## Architecture

```text
src/calculator_pro/
├── ai/              optional AI + rule-based explanations
├── core/            safe math expression parsing
├── ui/              menu controller
├── cli/             command-line product experience
├── export/          PDF report generation
├── visualization/   plots, graph analysis, transformations
├── study/           structured IB study sessions
├── matrix/
├── probability/
├── functions/
├── vectors/
└── statistics/
```

## Release Status

Version: `v3.0.0`

## License

MIT License. See [LICENSE](LICENSE).
