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
  - Save basic 2x2 matrix transformation diagrams
- Probability simulation engine
  - Monte Carlo probability estimation
  - Binomial trial simulation
  - Histogram output for simulation results
- Enhanced learning mode
  - Formula shown for each CLI calculation
  - Plain-English explanation of the method
  - Step-by-step guidance for calculations and plots
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
Learning mode: OFF
1. Matrix tools
2. Probability tools
3. Function tools
4. Vector tools
5. Statistics tools
6. Visualization tools
7. Toggle learning mode ON/OFF
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

Learning mode
Formula: P(X = k) = nCk x p^k x (1 - p)^(n - k)
Meaning: Use this for exactly k successes in n independent trials.
Steps:
1. Count ways to place the successes: 5C2.
2. Multiply by p^k = 0.4^2.
3. Multiply by (1 - p)^(n - k) = 0.6^3.
```

### Visualization Output

The CLI saves plots to `outputs/` by default:

```text
Graph saved to outputs/polynomial_graph.png
Histogram saved to outputs/simulation_histogram.png
Matrix transformation plot saved to outputs/matrix_transformation.png
```

ASCII sketch of a function plot workflow:

```text
coefficients -> evaluate y-values -> matplotlib figure -> PNG file
     [1 0 -4]          y = x^2 - 4          curve          outputs/polynomial_graph.png
```

ASCII sketch of matrix transformation visualization:

```text
original unit square      matrix A      transformed square
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

plot_polynomial([1, 0, -4], -5, 5, output_path="outputs/parabola.png")
```

## Running Tests

```bash
python -m pytest
```

The test suite covers matrix operations, probability functions, Monte Carlo
simulation, vector operations, visualization file output, and validation edge
cases.

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
    ├── test_vectors.py
    └── test_visualization.py
```

## Release Status

Version: `v2.0.0`

## License

MIT License. See [LICENSE](LICENSE).
