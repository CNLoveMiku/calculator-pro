# IB Math AA HL ToolBox

IB Math AA HL ToolBox is a modular Python command-line calculator for students
practicing IB Mathematics: Analysis and Approaches Higher Level.

Version 2.0.0 adds graphing, Monte Carlo probability simulation, stronger
vector tools, and a more complete learning mode. The project is intentionally
transparent: functions are small, typed where useful, and paired with formulas
and plain-English explanations.

## v2.0.0 Features

- Visualization layer with matplotlib
  - Plot common functions, such as `y = x^2`, `sin(x)`, and `cos(x)`
  - Plot polynomial graphs from coefficients
  - Add optional tangent lines using derivative approximation
  - Label endpoints, approximate x-intercepts, and tangent points
  - Save 2x2 matrix transformation diagrams with BEFORE and AFTER panels
- Probability simulation engine
  - Monte Carlo probability estimation
  - Binomial trial simulation
  - Histogram output for simulation results
- Enhanced learning mode
  - Formula shown for each CLI calculation
  - Step-by-step derivation
  - Short explanation of why each step is valid
  - IB Math AA HL exam-style method language
- Exam Mode
  - Hides step-by-step solutions
  - Shows final answers only
  - Simulates exam-condition checking
- Extended vector module
  - Dot product
  - Cross product
  - Magnitude
  - Angle between vectors
- Existing v1 tools remain available
  - Matrix operations
  - Probability and combinatorics
  - Polynomial evaluation
  - Numerical derivative approximation
  - Simple statistics

## IB Math AA HL Relevance

This toolbox maps to common IB Math AA HL work:

- Algebra and functions: polynomial evaluation, graphing, roots and curve shape
- Calculus: numerical derivative approximation and gradient interpretation
- Vectors: scalar product, vector product, magnitude, and angle
- Probability: counting methods, conditional probability, binomial models, and simulation
- Statistics: mean, variance, standard deviation, and distribution shape
- Matrices: operations, determinants, inverses, and 2D transformations

The tool is designed for revision and method-checking. Students should still
follow classroom expectations and IB exam calculator rules.

## Requirements

- Python 3.11 or newer recommended
- matplotlib for visualization
- pytest for tests

## Installation

Clone the repository:

```bash
git clone https://github.com/CNLoveMiku/calculator-pro.git
cd calculator-pro
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional editable install:

```bash
pip install -e .
```

## Usage

Run the CLI directly:

```bash
python main.py
```

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
0. Exit
```

## CLI Examples

### Matrix Addition

```text
A + B =
[ 6  8 ]
[ 10  12 ]
```

### Learning Mode

```text
P(X = k) = 0.3456

Learning mode explanation
Formula: P(X = k) = nCk x p^k x (1 - p)^(n - k)
Derivation:
1. Count success positions using 5C2.
   Why valid: Exactly k successes can occur in that many unordered positions among n trials.
2. Multiply by p^k = 0.4^2.
   Why valid: Independent successes multiply their probabilities.
3. Multiply by (1 - p)^(n - k) = 0.6^3.
   Why valid: The remaining trials must be failures, each with probability 1 - p.
```

### Exam Mode

Exam Mode is controlled from Learning mode settings:

```text
Mode: EXAM MODE - final answers only

mean = 2
```

In Exam Mode, formulas and derivations are hidden so the CLI behaves like a
final-answer checking tool.
```

### Visualization Output

The CLI saves plots to `outputs/` by default:

```text
Graph saved to outputs/polynomial_graph.png
Histogram saved to outputs/simulation_histogram.png
Matrix transformation plot saved to outputs/matrix_transformation.png
```

ASCII sketch of a function plot workflow with tangent:

```text
coefficients -> evaluate y-values -> optional tangent -> labeled PNG
     [1 0 -4]          y = x^2 - 4       slope at x=a     outputs/polynomial_graph.png
```

ASCII sketch of matrix transformation visualization:

```text
BEFORE panel              matrix A      AFTER panel
 (0,1)----(1,1)             [a b]          A(0,1)----A(1,1)
   |        |       -->     [c d]     -->    |          |
 (0,0)----(1,0)                            A(0,0)----A(1,0)
```

## Python API Examples

```python
from calculator_pro.probability import estimate_binomial_probability
from calculator_pro.vectors import angle_between_vectors, magnitude
from calculator_pro.visualization import plot_polynomial

print(magnitude([3, 4]))
print(angle_between_vectors([1, 0], [0, 1], degrees=True))
print(estimate_binomial_probability(5, 2, 0.4, 1000, seed=42))

plot_polynomial(
    [1, 0, -4],
    -5,
    5,
    derivative_at=1,
    output_path="outputs/parabola.png",
)
```

## Running Tests

```bash
python -m pytest
```

The test suite covers matrix operations, probability functions, Monte Carlo
simulation, vector operations, visualization file output, and validation edge
cases, including CLI Learning Mode and Exam Mode behavior.

## Project Structure

```text
calculator-pro/
├── LICENSE
├── README.md
├── RELEASE_NOTES.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── src/
│   └── calculator_pro/
│       ├── cli/
│       ├── functions/
│       ├── matrix/
│       ├── probability/
│       ├── statistics/
│       ├── vectors/
│       └── visualization/
└── tests/
    ├── test_matrix_operations.py
    ├── test_probability_functions.py
    ├── test_probability_simulation.py
    ├── test_cli_modes.py
    ├── test_vectors.py
    └── test_visualization.py
```

## Release Status

Version: `v2.0.1`

## License

MIT License. See [LICENSE](LICENSE).
