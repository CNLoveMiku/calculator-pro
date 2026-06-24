# Release Notes

## v2.0.0

IB Math AA HL ToolBox v2.0.0 upgrades the project from a calculation-focused
CLI into a more visual and simulation-ready educational toolbox.

### New Features

- Visualization layer powered by matplotlib
  - Plot common functions such as `y = x`, `y = x^2`, `sin(x)`, and `cos(x)`
  - Plot polynomial graphs from coefficient input
  - Save basic 2x2 matrix transformation diagrams
- Probability simulation engine
  - Generic Monte Carlo probability estimation
  - Binomial trial simulation
  - Exact-success binomial probability estimation by simulation
  - Histogram output for simulation results
- Enhanced vector module
  - Dot product
  - 3D cross product
  - Magnitude
  - Angle between vectors in radians or degrees
- Improved CLI
  - New Visualization tools menu
  - Learning mode toggle now explicitly reads ON/OFF
  - Monte Carlo simulation added to Probability tools
  - Vector magnitude and angle calculations added to Vector tools

### Improvements Over v1.0.0

- Adds visual outputs for polynomial graphs, function graphs, histograms, and matrix transformations
- Expands educational coverage for IB Math AA HL vectors and probability simulation
- Keeps backward-compatible public functions from v1.0.0
- Updates package metadata to `2.0.0`
- Adds matplotlib as a runtime dependency
- Extends pytest coverage for vectors, simulation, and visualization

### Validation

- `python -m pytest`
- `python main.py`

### Notes

- Visualization output is saved to PNG files by default from the CLI.
- The CLI remains text-based; no GUI is included in v2.0.0.
- Learning mode gives concise method explanations, not full symbolic derivations.

## v1.0.0

Initial stable GitHub release of IB Math AA HL ToolBox.

### Highlights

- Text-based CLI with continuous menu navigation
- Fast mode for quick answers
- Learning mode with formulas, plain-English explanations, and calculation steps
- Matrix operations: addition, multiplication, determinant, and inverse
- Probability tools: factorial, permutations, combinations, conditional probability, and binomial probability
- Function tools: polynomial evaluation and numerical derivative approximation
- Vector tools: dot product and 3D cross product
- Statistics tools: mean, variance, and standard deviation
- Basic pytest suite for matrix operations, probability functions, and edge cases
- MIT license

### Validation

- `python -m pytest`
- `python main.py`
