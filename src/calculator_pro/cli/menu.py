"""Text-based CLI menu for the IB Math AA HL ToolBox."""

from collections.abc import Callable
from math import cos, sin

from calculator_pro.ai import AIExplanationEngine
from calculator_pro.export import SolutionReport, export_solution_pdf
from calculator_pro.functions import approximate_derivative, evaluate_polynomial
from calculator_pro.matrix import add, determinant, inverse, multiply
from calculator_pro.matrix.types import Matrix
from calculator_pro.probability import (
    binomial_probability,
    combinations,
    conditional_probability,
    factorial,
    plot_simulation_histogram,
    permutations,
    simulate_binomial_trials,
)
from calculator_pro.statistics import mean, standard_deviation, variance
from calculator_pro.study import create_study_session
from calculator_pro.ui import MenuController
from calculator_pro.vectors import (
    angle_between_vectors,
    cross_product,
    dot_product,
    magnitude,
)
from calculator_pro.visualization import (
    plot_expression_analysis,
    plot_function,
    plot_matrix_transformation,
    plot_polynomial,
)


MenuHandler = Callable[[], None]
LearningStep = tuple[str, str]
LearningDetails = tuple[str, list[LearningStep]]

LEARNING_MODE = False
EXAM_MODE = False
AI_ENGINE = AIExplanationEngine()


def run_cli() -> None:
    """Run the interactive IB Math AA HL ToolBox menu until the user exits."""
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Algebra tools", _algebra_menu),
        "2": ("Probability tools", _probability_menu),
        "3": ("Visualization", _visualization_menu),
        "4": ("Learning mode settings", _learning_settings_menu),
        "5": ("Statistics tools", _statistics_menu),
        "6": ("Matrix tools", _matrix_menu),
        "7": ("Vector tools", _vector_menu),
        "8": ("Study Session", _study_session_menu),
        "9": ("Export PDF report", _export_report_menu),
        "0": ("Exit", _exit_menu),
    }

    _run_menu("IB Math AA HL ToolBox", actions)


def _algebra_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Function tools", _function_menu),
        "2": ("Matrix tools", _matrix_menu),
        "3": ("Vector tools", _vector_menu),
        "0": ("Back", _back_menu),
    }

    _run_menu("Algebra tools", actions)


def _learning_settings_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Toggle learning mode ON/OFF", _toggle_learning_mode),
        "2": ("Toggle exam mode ON/OFF", _toggle_exam_mode),
        "0": ("Back", _back_menu),
    }

    _run_menu("Learning mode settings", actions)


def _matrix_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Matrix addition", _matrix_addition),
        "2": ("Matrix multiplication", _matrix_multiplication),
        "3": ("Determinant", _matrix_determinant),
        "4": ("Inverse", _matrix_inverse),
        "0": ("Back", _back_menu),
    }

    _run_menu("Matrix tools", actions)


def _probability_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Factorial", _probability_factorial),
        "2": ("Permutations nPr", _probability_permutations),
        "3": ("Combinations nCr", _probability_combinations),
        "4": ("Conditional probability", _probability_conditional),
        "5": ("Binomial probability P(X = k)", _probability_binomial),
        "6": ("Monte Carlo binomial simulation", _probability_binomial_simulation),
        "0": ("Back", _back_menu),
    }

    _run_menu("Probability tools", actions)


def _function_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Polynomial evaluation", _function_polynomial_evaluation),
        "2": ("Polynomial derivative approximation", _function_derivative),
        "0": ("Back", _back_menu),
    }

    _run_menu("Function tools", actions)


def _vector_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Dot product", _vector_dot_product),
        "2": ("Cross product", _vector_cross_product),
        "3": ("Magnitude", _vector_magnitude),
        "4": ("Angle between vectors", _vector_angle),
        "0": ("Back", _back_menu),
    }

    _run_menu("Vector tools", actions)


def _statistics_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Mean", _statistics_mean),
        "2": ("Variance", _statistics_variance),
        "3": ("Standard deviation", _statistics_standard_deviation),
        "0": ("Back", _back_menu),
    }

    _run_menu("Statistics tools", actions)


def _visualization_menu() -> None:
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Plot common function y = f(x)", _visualization_function),
        "2": ("Plot polynomial graph", _visualization_polynomial),
        "3": ("Plot 2x2 matrix transformation", _visualization_matrix),
        "4": ("Interactive expression graph analysis", _visualization_expression_analysis),
        "0": ("Back", _back_menu),
    }

    _run_menu("Visualization tools", actions)


def _run_menu(title: str, actions: dict[str, tuple[str, MenuHandler]]) -> None:
    """Display a menu and run actions until the user chooses 0."""
    MenuController(_current_mode_label).run(title, actions, _print_header)


def _matrix_addition() -> None:
    print("\nEnter the first matrix.")
    left = _read_matrix()
    print("\nEnter the second matrix.")
    right = _read_matrix()
    details = (
        "C = A + B, so c_ij = a_ij + b_ij",
        [
            (
                f"Compare dimensions: A is {_matrix_size(left)} and B is {_matrix_size(right)}.",
                "Matrix addition is defined only when both matrices have the same order.",
            ),
            (
                "Add entries in matching positions to form each c_ij.",
                "The definition of matrix addition is entry-wise addition.",
            ),
        ],
    )

    _run_calculation(lambda: _print_matrix("A + B", add(left, right)), details)


def _matrix_multiplication() -> None:
    print("\nEnter the left matrix A.")
    left = _read_matrix()
    print("\nEnter the right matrix B.")
    right = _read_matrix()
    details = (
        "C = AB, so c_ij = row i of A dot column j of B",
        [
            (
                f"Check compatibility: A is {_matrix_size(left)} and B is {_matrix_size(right)}.",
                "The number of columns in A must equal the number of rows in B.",
            ),
            (
                "Compute each entry using a row-column dot product.",
                "This is the formal definition of matrix multiplication used in IB matrices work.",
            ),
        ],
    )

    _run_calculation(lambda: _print_matrix("AB", multiply(left, right)), details)


def _matrix_determinant() -> None:
    matrix = _read_matrix()
    details = (
        "For 2x2: det([[a,b],[c,d]]) = ad - bc",
        [
            (
                "Confirm the matrix is square.",
                "Determinants are defined only for square matrices.",
            ),
            (
                "Use ad - bc for 2x2, or expand recursively along the first row.",
                "Cofactor expansion preserves determinant value and reduces the problem to smaller determinants.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value("det(A)", determinant(matrix)), details)


def _matrix_inverse() -> None:
    matrix = _read_matrix()
    details = (
        "A^-1 = adj(A) / det(A), and for 2x2 use (1/det)[[d,-b],[-c,a]]",
        [
            (
                "Confirm the matrix is square.",
                "Only square matrices can have a two-sided inverse.",
            ),
            (
                "Find det(A) and check it is not 0.",
                "A zero determinant means the transformation collapses space, so no inverse exists.",
            ),
            (
                "Use the 2x2 inverse rule or adj(A) / det(A).",
                "The adjugate formula constructs a matrix that multiplies with A to give the identity.",
            ),
        ],
    )

    _run_calculation(lambda: _print_matrix("A^-1", inverse(matrix)), details)


def _probability_factorial() -> None:
    n = _read_int("Enter n: ")
    details = (
        "n! = n x (n - 1) x ... x 2 x 1",
        [
            (
                f"Multiply every positive integer from 1 to {n}.",
                "Factorial counts ordered arrangements of n distinct items.",
            ),
            (
                "Use 0! = 1 if n is zero.",
                "The empty product is defined as 1, which keeps counting formulas consistent.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value(f"{n}!", factorial(n)), details)


def _probability_permutations() -> None:
    n = _read_int("Enter n: ")
    r = _read_int("Enter r: ")
    details = (
        "nPr = n! / (n - r)!",
        [
            (
                f"Choose {r} ordered items from {n} total items.",
                "A permutation treats AB and BA as different outcomes.",
            ),
            (
                "Divide n! by (n - r)! to cancel unused arrangements.",
                "Only the first r ordered positions are needed.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value(f"{n}P{r}", permutations(n, r)), details)


def _probability_combinations() -> None:
    n = _read_int("Enter n: ")
    r = _read_int("Enter r: ")
    details = (
        "nCr = n! / (r! x (n - r)!)",
        [
            (
                f"Start from the ordered count {n}P{r}.",
                "Permutations count the same group multiple times in different orders.",
            ),
            (
                "Divide by r! to remove internal ordering of the selected group.",
                "A combination treats the same selected items as one outcome.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value(f"{n}C{r}", combinations(n, r)), details)


def _probability_conditional() -> None:
    probability_a_and_b = _read_float("Enter P(A and B): ")
    probability_b = _read_float("Enter P(B): ")
    details = (
        "P(A|B) = P(A and B) / P(B)",
        [
            (
                f"Use the intersection probability P(A and B) = {_format_number(probability_a_and_b)}.",
                "Only outcomes where both A and B happen are favorable after conditioning on B.",
            ),
            (
                f"Divide by P(B) = {_format_number(probability_b)}.",
                "Conditioning changes the sample space to B, so P(B) becomes the new total.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value(
            "P(A|B)",
            conditional_probability(probability_a_and_b, probability_b),
        ),
        details,
    )


def _probability_binomial() -> None:
    n = _read_int("Enter number of trials n: ")
    k = _read_int("Enter exact successes k: ")
    p = _read_float("Enter success probability p: ")
    details = (
        "P(X = k) = nCk x p^k x (1 - p)^(n - k)",
        [
            (
                f"Count success positions using {n}C{k}.",
                "Exactly k successes can occur in that many unordered positions among n trials.",
            ),
            (
                f"Multiply by p^k = {_format_number(p)}^{k}.",
                "Independent successes multiply their probabilities.",
            ),
            (
                f"Multiply by (1 - p)^(n - k) = {_format_number(1 - p)}^{n - k}.",
                "The remaining trials must be failures, each with probability 1 - p.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value("P(X = k)", binomial_probability(n, k, p)),
        details,
    )


def _probability_binomial_simulation() -> None:
    n = _read_int("Enter number of trials per experiment n: ")
    k = _read_int("Enter exact successes k: ")
    p = _read_float("Enter success probability p: ")
    trials = _read_positive_int("Enter Monte Carlo simulation count: ")
    output_path = _read_output_path("simulation_histogram.png")
    details = (
        "estimated P(X = k) = matching simulated outcomes / total simulations",
        [
            (
                f"Simulate {trials} experiments.",
                "Monte Carlo estimates stabilize as the number of repeated trials increases.",
            ),
            (
                f"Each experiment has {n} Bernoulli trials with p = {_format_number(p)}.",
                "A binomial model requires independent trials with constant success probability.",
            ),
            (
                f"Count outcomes where the success count is {k} and divide by {trials}.",
                "Relative frequency estimates probability under repeated sampling.",
            ),
            (
                "Save a histogram of simulated success counts.",
                "The histogram shows the empirical distribution, which should resemble the binomial shape.",
            ),
        ],
    )

    def action() -> None:
        simulated_values = simulate_binomial_trials(n, p, trials)
        estimate = sum(1 for value in simulated_values if value == k) / trials
        plot_simulation_histogram(simulated_values, output_path=output_path)
        _print_value("estimated P(X = k)", estimate)
        print(f"Histogram saved to {output_path}")

    _run_calculation(action, details)


def _function_polynomial_evaluation() -> None:
    coefficients = _read_coefficients()
    x = _read_float("Enter x: ")
    details = (
        "Horner's method: result = result x x + next coefficient",
        [
            (
                f"Start with result = 0 and x = {_format_number(x)}.",
                "Horner's method builds the polynomial from highest power downward.",
            ),
            (
                "For each coefficient, multiply the current result by x and add the coefficient.",
                "This is algebraically equivalent to the expanded polynomial but avoids repeated powers.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value("f(x)", evaluate_polynomial(coefficients, x)),
        details,
    )


def _function_derivative() -> None:
    coefficients = _read_coefficients()
    x = _read_float("Enter x: ")
    step = _read_float("Enter step h, or press Enter for 0.00001: ", default=1e-5)

    def polynomial(value: float) -> float:
        return evaluate_polynomial(coefficients, value)

    details = (
        "f'(x) is approximately (f(x + h) - f(x - h)) / (2h)",
        [
            (
                f"Use x = {_format_number(x)} and h = {_format_number(step)}.",
                "A small h samples the function close to the target point.",
            ),
            (
                "Evaluate the polynomial at x + h and x - h.",
                "Central difference uses points on both sides to reduce one-sided error.",
            ),
            (
                "Divide the change in y by the horizontal distance 2h.",
                "Gradient is rise over run, matching the derivative interpretation in AA HL.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value(
            "f'(x)",
            approximate_derivative(polynomial, x, step),
        ),
        details,
    )


def _vector_dot_product() -> None:
    left = _read_vector("Enter vector a components: ")
    right = _read_vector("Enter vector b components: ")
    details = (
        "a . b = a1b1 + a2b2 + ... + anbn",
        [
            (
                "Check both vectors have the same number of components.",
                "Each component in a must pair with exactly one component in b.",
            ),
            (
                "Multiply matching components and add the products.",
                "This is the scalar product definition used for projections and angles.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value("a . b", dot_product(left, right)), details)


def _vector_cross_product() -> None:
    left = _read_vector("Enter 3D vector a components: ")
    right = _read_vector("Enter 3D vector b components: ")
    details = (
        "a x b = [a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1]",
        [
            (
                "Confirm both vectors have exactly 3 components.",
                "The cross product is defined for 3D vectors in this course context.",
            ),
            (
                "Apply the determinant-style component formulas.",
                "The resulting vector is perpendicular to both original vectors.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_vector("a x b", cross_product(left, right)),
        details,
    )


def _vector_magnitude() -> None:
    vector = _read_vector("Enter vector components: ")
    details = (
        "|a| = sqrt(a1^2 + a2^2 + ... + an^2)",
        [
            (
                "Square each component.",
                "Squaring measures each component's contribution to length without sign.",
            ),
            (
                "Add the squared components.",
                "This extends Pythagoras to vectors with any number of components.",
            ),
            (
                "Take the square root.",
                "The square root converts squared length back to actual length.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value("|a|", magnitude(vector)), details)


def _vector_angle() -> None:
    left = _read_vector("Enter vector a components: ")
    right = _read_vector("Enter vector b components: ")
    details = (
        "cos(theta) = (a . b) / (|a||b|)",
        [
            (
                "Find the dot product a . b.",
                "The scalar product connects vector components to the angle between vectors.",
            ),
            (
                "Find both magnitudes |a| and |b|.",
                "The formula compares direction after normalizing for vector lengths.",
            ),
            (
                "Use arccos to recover the angle in degrees.",
                "Cosine is inverted to get theta from the computed ratio.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value(
            "angle between vectors",
            angle_between_vectors(left, right, degrees=True),
        ),
        details,
    )


def _statistics_mean() -> None:
    values = _read_number_list("Enter data values: ")
    details = (
        "mean = sum of values / number of values",
        [
            (
                "Add all data values.",
                "The total combines all observations into one aggregate amount.",
            ),
            (
                f"Divide by the number of values, n = {len(values)}.",
                "Equal sharing of the total gives the arithmetic average.",
            ),
        ],
    )

    _run_calculation(lambda: _print_value("mean", mean(values)), details)


def _statistics_variance() -> None:
    values = _read_number_list("Enter data values: ")
    sample = _read_yes_no("Use sample variance with denominator n - 1? (y/n): ")
    divisor_text = "n - 1" if sample else "n"
    details = (
        f"variance = sum((x - mean)^2) / {divisor_text}",
        [
            (
                "Find the mean.",
                "Spread is measured relative to the central value.",
            ),
            (
                "Subtract the mean from each value and square each difference.",
                "Squaring removes signs and gives larger deviations more weight.",
            ),
            (
                f"Divide by {divisor_text}.",
                "Use n for a full population and n - 1 when estimating from a sample.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value("variance", variance(values, sample=sample)),
        details,
    )


def _statistics_standard_deviation() -> None:
    values = _read_number_list("Enter data values: ")
    sample = _read_yes_no("Use sample standard deviation with denominator n - 1? (y/n): ")
    details = (
        "standard deviation = square root of variance",
        [
            (
                "Calculate the variance.",
                "Variance is the average squared distance from the mean.",
            ),
            (
                "Take the square root.",
                "This returns the spread measure to the same units as the data.",
            ),
        ],
    )

    _run_calculation(
        lambda: _print_value(
            "standard deviation",
            standard_deviation(values, sample=sample),
        ),
        details,
    )


def _visualization_function() -> None:
    function_name, function = _read_common_function()
    x_min = _read_float("Enter minimum x: ")
    x_max = _read_float("Enter maximum x: ")
    derivative_at = _read_optional_tangent_point()
    output_path = _read_output_path(f"{function_name}_graph.png")
    details = (
        "y = f(x)",
        [
            (
                f"Use the selected function: {function_name}.",
                "The graph represents the set of ordered pairs (x, f(x)).",
            ),
            (
                f"Calculate y-values from x = {_format_number(x_min)} to x = {_format_number(x_max)}.",
                "Sampling the interval gives enough points for matplotlib to draw the curve.",
            ),
            (
                "Label endpoints, intercepts, and any requested tangent point.",
                "These features support AA HL graph interpretation and gradient reasoning.",
            ),
        ],
    )

    def action() -> None:
        plot_function(
            function,
            x_min,
            x_max,
            derivative_at=derivative_at,
            title=f"y = {function_name}",
            output_path=output_path,
        )
        print(f"\nGraph saved to {output_path}")

    _run_calculation(action, details)


def _visualization_polynomial() -> None:
    coefficients = _read_coefficients()
    x_min = _read_float("Enter minimum x: ")
    x_max = _read_float("Enter maximum x: ")
    derivative_at = _read_optional_tangent_point()
    output_path = _read_output_path("polynomial_graph.png")
    details = (
        "For coefficients [a,b,c], y = ax^2 + bx + c",
        [
            (
                "Read coefficients from highest power to constant term.",
                "This matches standard polynomial notation.",
            ),
            (
                "Evaluate the polynomial across the selected x-range.",
                "Graphing many function values reveals turning points and intercept behavior.",
            ),
            (
                "Save the plotted curve with labels and optional tangent.",
                "Annotated plots make key features visible for exam-style analysis.",
            ),
        ],
    )

    def action() -> None:
        plot_polynomial(
            coefficients,
            x_min,
            x_max,
            derivative_at=derivative_at,
            output_path=output_path,
        )
        print(f"\nGraph saved to {output_path}")

    _run_calculation(action, details)


def _visualization_matrix() -> None:
    print("\nEnter a 2x2 transformation matrix.")
    matrix = _read_matrix()
    output_path = _read_output_path("matrix_transformation.png")
    details = (
        "A transforms each point v into Av",
        [
            (
                "Plot the original unit square and basis vectors in the BEFORE panel.",
                "The original shape gives a geometric reference for the transformation.",
            ),
            (
                "Multiply each vertex and basis vector by the 2x2 matrix.",
                "A matrix transformation maps every point v to Av.",
            ),
            (
                "Plot the transformed shape in the AFTER panel.",
                "Comparing before and after shows stretch, shear, reflection, or rotation effects.",
            ),
        ],
    )

    def action() -> None:
        plot_matrix_transformation(matrix, output_path=output_path)
        print(f"\nMatrix transformation plot saved to {output_path}")

    _run_calculation(action, details)


def _visualization_expression_analysis() -> None:
    expression = _read_non_empty_text("Enter f(x), for example x^2 - 4 or sin(x): ")
    x_min = _read_float("Enter minimum x: ")
    x_max = _read_float("Enter maximum x: ")
    zoom_ranges = _read_zoom_ranges()
    output_path = _read_output_path("interactive_graph_analysis.png")
    details = (
        "Plot f(x) and estimate f'(x) using central difference",
        [
            (
                "Parse the entered expression as a safe function of x.",
                "Only approved math operations and functions are allowed, which keeps input controlled.",
            ),
            (
                "Graph f(x) and a numerical derivative curve on the same axes.",
                "The derivative curve shows gradient behavior across the interval.",
            ),
            (
                "Estimate roots and stationary points from sign changes.",
                "IB graph analysis often uses intercepts and turning points to interpret function behavior.",
            ),
            (
                "Replot requested zoom windows as additional panels.",
                "Zooming helps inspect local behavior without changing the original function.",
            ),
        ],
    )

    def action() -> None:
        _, analysis = plot_expression_analysis(
            expression,
            x_min,
            x_max,
            output_path=output_path,
            zoom_ranges=zoom_ranges,
        )
        print(f"\nGraph analysis saved to {output_path}")
        print(f"Estimated roots: {_format_points(analysis.roots)}")
        print(f"Estimated maxima: {_format_coordinate_points(analysis.maxima)}")
        print(f"Estimated minima: {_format_coordinate_points(analysis.minima)}")

    _run_calculation(action, details)


def _study_session_menu() -> None:
    topic = _read_non_empty_text(
        "Choose topic (binomial probability, vectors, polynomial graphs, or custom): "
    )
    session = create_study_session(topic)
    _print_header(f"Study Session: {session.topic}")
    for index, step in enumerate(session.steps, start=1):
        print(f"\n{index}. {step.title}")
        print(step.prompt)
        if index < len(session.steps):
            _pause()
    _pause()


def _export_report_menu() -> None:
    title = _read_non_empty_text("Report title: ")
    problem = _read_non_empty_text("Problem statement: ")
    answer = _read_non_empty_text("Final answer: ")
    explanation = _read_non_empty_text("Explanation summary: ")
    steps = _read_multiline_items("Enter solution steps, one per line. Blank line to finish:")
    graph_paths = _read_multiline_items("Enter graph image paths to include. Blank line to finish:")
    output_path = _read_output_path("solution_report.pdf")

    report = SolutionReport(
        title=title,
        problem=problem,
        answer=answer,
        explanation=explanation,
        steps=steps,
        graph_paths=graph_paths,
    )
    details = (
        "PDF report = problem + final answer + explanation + steps + optional graphs",
        [
            (
                "Collect the written solution and any graph image paths.",
                "A portfolio-grade learning artifact should preserve both reasoning and visual evidence.",
            ),
            (
                "Render the content into a PDF.",
                "PDF export makes the solution shareable for revision or teacher feedback.",
            ),
        ],
    )
    _run_calculation(
        lambda: print(f"\nPDF report saved to {export_solution_pdf(report, output_path)}"),
        details,
    )


def _read_matrix() -> Matrix:
    """Read matrix dimensions and row values from the user."""
    rows = _read_positive_int("Number of rows: ", maximum=10)
    columns = _read_positive_int("Number of columns: ", maximum=10)

    matrix: list[list[float]] = []
    for row_number in range(1, rows + 1):
        while True:
            row_text = input(
                f"Row {row_number} ({columns} numbers separated by spaces): "
            ).strip()
            if not row_text:
                print("Matrix rows cannot be empty.")
                continue

            try:
                row = [float(value) for value in row_text.split()]
            except ValueError:
                print("Each row must contain numbers only.")
                continue

            if len(row) != columns:
                print(f"Please enter exactly {columns} numbers.")
                continue

            matrix.append(row)
            break

    return matrix


def _read_non_empty_text(prompt: str) -> str:
    """Read non-empty text input."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


def _read_coefficients() -> list[float]:
    """Read polynomial coefficients in descending power order."""
    return _read_number_list("Enter coefficients from highest power to constant term: ")


def _read_vector(prompt: str) -> list[float]:
    """Read vector components from one line."""
    return _read_number_list(prompt)


def _read_number_list(prompt: str) -> list[float]:
    """Read a non-empty list of numbers from one line."""
    while True:
        text = input(prompt).strip()

        try:
            values = [float(value) for value in text.split()]
        except ValueError:
            print("Values must be numbers separated by spaces.")
            continue

        if not values:
            print("Enter at least one value.")
            continue

        return values


def _read_multiline_items(prompt: str) -> list[str]:
    """Read multiple lines until a blank line."""
    print(prompt)
    items: list[str] = []
    while True:
        text = input("> ").strip()
        if not text:
            return items
        items.append(text)


def _read_zoom_ranges() -> list[tuple[float, float]]:
    """Read optional zoom ranges for expression graphing."""
    ranges: list[tuple[float, float]] = []
    if not _read_yes_no("Add a zoom panel? (y/n): "):
        return ranges
    while True:
        start = _read_float("Zoom minimum x: ")
        stop = _read_float("Zoom maximum x: ")
        ranges.append((start, stop))
        if not _read_yes_no("Add another zoom panel? (y/n): "):
            return ranges


def _read_positive_int(prompt: str, maximum: int | None = None) -> int:
    """Read a positive integer, retrying until valid."""
    while True:
        value = _read_int(prompt)
        if value <= 0:
            print("Please enter a positive whole number.")
            continue
        if maximum is not None and value > maximum:
            print(f"Please enter a value no larger than {maximum}.")
            continue
        return value


def _read_int(prompt: str) -> int:
    """Read an integer, retrying until the input is valid."""
    while True:
        text = input(prompt).strip()
        if not text:
            print("Input cannot be empty. Please enter a whole number.")
            continue

        try:
            return int(text)
        except ValueError:
            print("Please enter a whole number.")


def _read_float(prompt: str, default: float | None = None) -> float:
    """Read a float, optionally accepting an empty value as a default."""
    while True:
        text = input(prompt).strip()

        if text == "" and default is not None:
            return default

        if not text:
            print("Input cannot be empty. Please enter a number.")
            continue

        try:
            return float(text)
        except ValueError:
            print("Please enter a number.")


def _read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer."""
    while True:
        text = input(prompt).strip().lower()
        if not text:
            print("Input cannot be empty. Please enter y or n.")
            continue

        if text in {"y", "yes"}:
            return True
        if text in {"n", "no"}:
            return False

        print("Please enter y or n.")


def _read_common_function() -> tuple[str, Callable[[float], float]]:
    """Read a simple built-in function choice for graphing."""
    functions: dict[str, tuple[str, Callable[[float], float]]] = {
        "1": ("x", lambda x: x),
        "2": ("x^2", lambda x: x**2),
        "3": ("x^3", lambda x: x**3),
        "4": ("sin(x)", sin),
        "5": ("cos(x)", cos),
    }

    while True:
        print("\nChoose a function to plot:")
        for key, (label, _) in functions.items():
            print(f"{key}. y = {label}")

        choice = input("Select a function: ").strip()
        function = functions.get(choice)
        if function is not None:
            return function

        print("Invalid option. Please enter one of the listed numbers.")


def _read_output_path(default_filename: str) -> str:
    """Read an output image path, defaulting to outputs/default_filename."""
    default_path = f"outputs/{default_filename}"
    text = input(f"Output image path [{default_path}]: ").strip()
    return text or default_path


def _read_optional_tangent_point() -> float | None:
    """Read an optional x-value for tangent-line visualization."""
    if not _read_yes_no("Add tangent line using derivative approximation? (y/n): "):
        return None
    return _read_float("Enter tangent x-value: ")


def _run_calculation(
    action: Callable[[], None],
    learning_details: LearningDetails,
) -> None:
    """Run one calculation and optionally print learning details."""
    try:
        action()
        if LEARNING_MODE and not EXAM_MODE:
            formula, steps = learning_details
            _print_learning_details(formula, steps)
    except (OSError, TypeError, ValueError) as error:
        print(f"\nError: {error}")
    finally:
        _pause()


def _print_learning_details(
    formula: str,
    steps: list[LearningStep],
) -> None:
    """Print formula, explanation, and calculation steps."""
    print("\nLearning mode explanation")
    print(f"Formula: {formula}")
    print("Derivation:")
    for index, (step, why_valid) in enumerate(steps, start=1):
        print(f"{index}. {step}")
        print(f"   Why valid: {why_valid}")

    explanation = AI_ENGINE.explain(
        topic="IB Math AA HL",
        problem="Current CLI calculation",
        answer="See final answer above",
        formula=formula,
        steps=steps,
    )
    print(f"\nAI explanation layer ({explanation.source})")
    print(f"Intuitive explanation: {explanation.intuitive}")
    print(f"Formal mathematical solution: {explanation.formal_solution}")
    print(f"IB exam strategy tip: {explanation.exam_strategy_tip}")


def _print_header(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def _print_value(label: str, value: float | int) -> None:
    print(f"\n{label} = {_format_number(value)}")


def _print_matrix(label: str, matrix: Matrix) -> None:
    print(f"\n{label} =")
    for row in matrix:
        formatted_row = "  ".join(_format_number(value) for value in row)
        print(f"[ {formatted_row} ]")


def _print_vector(label: str, vector: list[float]) -> None:
    formatted_vector = ", ".join(_format_number(value) for value in vector)
    print(f"\n{label} = <{formatted_vector}>")


def _format_number(value: float | int) -> str:
    """Format numbers without distracting trailing zeros."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))

    return f"{value:.8g}"


def _format_points(values: list[float]) -> str:
    if not values:
        return "none detected"
    return ", ".join(_format_number(value) for value in values)


def _format_coordinate_points(values: list[tuple[float, float]]) -> str:
    if not values:
        return "none detected"
    return ", ".join(
        f"({_format_number(x_value)}, {_format_number(y_value)})"
        for x_value, y_value in values
    )


def _matrix_size(matrix: Matrix) -> str:
    """Return a human-readable matrix size."""
    return f"{len(matrix)}x{len(matrix[0])}"


def _toggle_learning_mode() -> None:
    global LEARNING_MODE

    LEARNING_MODE = not LEARNING_MODE
    if LEARNING_MODE:
        _set_exam_mode(False)
    print(f"Learning mode {'ON' if LEARNING_MODE else 'OFF'}.")
    _pause()


def _toggle_exam_mode() -> None:
    _set_exam_mode(not EXAM_MODE)
    print(f"Exam mode {'ON' if EXAM_MODE else 'OFF'}.")
    _pause()


def _set_exam_mode(enabled: bool) -> None:
    global EXAM_MODE, LEARNING_MODE

    EXAM_MODE = enabled
    if enabled:
        LEARNING_MODE = False


def _current_mode_label() -> str:
    if EXAM_MODE:
        return "EXAM MODE - final answers only"
    if LEARNING_MODE:
        return "Learning mode ON"
    return "Fast mode"


def _pause() -> None:
    try:
        input("\nPress Enter to continue...")
    except EOFError:
        print()


def _back_menu() -> None:
    print("Returning to previous menu.")


def _exit_menu() -> None:
    print("Goodbye.")
