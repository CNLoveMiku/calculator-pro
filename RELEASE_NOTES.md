# Release Notes

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

### Known Scope

- No GUI in v1.0.0
- No graphing or symbolic algebra
- Learning-mode steps are concise explanations, not full handwritten-style derivations

### Suggested v2.0 Improvements

- Add graph visualization for functions, derivatives, and probability distributions
- Add AI-guided explanation mode for adaptive hints and worked examples
- Add symbolic algebra support for exact simplification where appropriate
- Add exportable solution reports as Markdown or PDF
- Add interactive plots for matrices, vectors, and statistics
- Add a GUI or web interface while keeping the CLI available
- Expand test coverage to CLI flows, vectors, statistics, and function tools
