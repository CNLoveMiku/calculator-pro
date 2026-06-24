# IB Math AA HL ToolBox

IB Math AA HL ToolBox is a clean, text-based Python calculator for students
practicing IB Mathematics: Analysis and Approaches Higher Level.

The project focuses on transparent mathematical methods rather than black-box
answers. It includes a fast mode for quick calculations and a learning mode
that prints the formula, a plain-English explanation, and calculation steps.

## Features

- Matrix tools
  - Matrix addition
  - Matrix multiplication
  - Recursive determinant calculation with a 2x2 base case
  - Matrix inverse for 2x2 and larger square matrices
- Probability tools
  - Factorial
  - Permutations, `nPr`
  - Combinations, `nCr`
  - Conditional probability
  - Exact binomial probability, `P(X = k)`
- Function tools
  - Polynomial evaluation using Horner's method
  - Numerical derivative approximation using central difference
- Vector tools
  - Dot product
  - 3D cross product
- Statistics tools
  - Mean
  - Variance
  - Standard deviation
- CLI modes
  - Fast mode for concise answers
  - Learning mode for formulas, explanations, and step-by-step output

## IB Math AA HL Relevance

This toolbox maps directly to common IB Math AA HL topics:

- Algebra and functions: polynomial evaluation and numerical slopes
- Calculus: derivative approximation and interpretation of gradients
- Vectors: scalar product and vector product in 3D
- Probability: counting methods, conditional probability, and binomial models
- Statistics: measures of center and spread
- Matrices: operations, determinants, invertibility, and transformations

The goal is to support revision, checking work, and understanding method steps.
Students should still follow their teacher's guidance and IB exam calculator
rules.

## Requirements

- Python 3.11 or newer recommended
- No runtime third-party dependencies
- `pytest` is required only for running tests

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/calculator-pro.git
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

Install test dependencies:

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

After launching, choose from the main menu:

```text
IB Math AA HL ToolBox
---------------------
Mode: fast
1. Matrix tools
2. Probability tools
3. Function tools
4. Vector tools
5. Statistics tools
6. Switch fast/learning mode
0. Exit
```

### Example: Matrix Addition

```text
Select an option: 1
Select an option: 1

Enter the first matrix.
Number of rows: 2
Number of columns: 2
Row 1 (2 numbers separated by spaces): 1 2
Row 2 (2 numbers separated by spaces): 3 4

Enter the second matrix.
Number of rows: 2
Number of columns: 2
Row 1 (2 numbers separated by spaces): 5 6
Row 2 (2 numbers separated by spaces): 7 8

A + B =
[ 6  8 ]
[ 10  12 ]
```

### Example: Learning Mode

Switch to learning mode from the main menu:

```text
Select an option: 6
Mode switched to learning.
```

For a binomial probability calculation, learning mode adds method context:

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

### Example: Importing Functions

```python
from calculator_pro.matrix import determinant
from calculator_pro.probability import combinations
from calculator_pro.statistics import standard_deviation
from calculator_pro.vectors import dot_product

print(determinant([[1, 2], [3, 4]]))
print(combinations(5, 2))
print(standard_deviation([1, 2, 3, 4]))
print(dot_product([1, 2, 3], [4, 5, 6]))
```

## Running Tests

```bash
python -m pytest
```

The v1.0.0 test suite covers matrix operations, probability functions, and
edge cases such as invalid dimensions, negative values, impossible
probabilities, and singular matrices.

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
│       └── vectors/
└── tests/
    ├── conftest.py
    ├── test_matrix_operations.py
    └── test_probability_functions.py
```

## Release Status

Version: `v1.0.0`

This release is ready for GitHub publication as a lightweight educational CLI
toolbox.

## License

MIT License. See [LICENSE](LICENSE).
