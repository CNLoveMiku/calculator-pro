"""Text-based CLI menu for the IB Math AA HL ToolBox."""

from collections.abc import Callable

from calculator_pro.functions import approximate_derivative, evaluate_polynomial
from calculator_pro.matrix import add, determinant, inverse, multiply
from calculator_pro.matrix.types import Matrix
from calculator_pro.probability import (
    binomial_probability,
    combinations,
    conditional_probability,
    factorial,
    permutations,
)
from calculator_pro.statistics import mean, standard_deviation, variance
from calculator_pro.vectors import cross_product, dot_product


MenuHandler = Callable[[], None]
LearningDetails = tuple[str, str, list[str]]

LEARNING_MODE = False


def run_cli() -> None:
    """Run the interactive IB Math AA HL ToolBox menu until the user exits."""
    actions: dict[str, tuple[str, MenuHandler]] = {
        "1": ("Matrix tools", _matrix_menu),
        "2": ("Probability tools", _probability_menu),
        "3": ("Function tools", _function_menu),
        "4": ("Vector tools", _vector_menu),
        "5": ("Statistics tools", _statistics_menu),
        "6": ("Switch fast/learning mode", _toggle_learning_mode),
        "0": ("Exit", _exit_menu),
    }

    _run_menu("IB Math AA HL ToolBox", actions)


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


def _run_menu(title: str, actions: dict[str, tuple[str, MenuHandler]]) -> None:
    """Display a menu and run actions until the user chooses 0."""
    while True:
        _print_header(title)
        print(f"Mode: {'learning' if LEARNING_MODE else 'fast'}")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")

        try:
            choice = input("Select an option: ").strip()
        except EOFError:
            print()
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid option. Please enter one of the listed numbers.")
            continue

        _, handler = action
        handler()

        if choice == "0":
            break


def _matrix_addition() -> None:
    print("\nEnter the first matrix.")
    left = _read_matrix()
    print("\nEnter the second matrix.")
    right = _read_matrix()
    details = (
        "C = A + B, so c_ij = a_ij + b_ij",
        "Add entries in matching positions.",
        [
            f"Check dimensions: A is {_matrix_size(left)}, B is {_matrix_size(right)}.",
            "Add each matching pair of entries.",
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
        "Multiply across rows and down columns, then add.",
        [
            f"Check dimensions: A is {_matrix_size(left)}, B is {_matrix_size(right)}.",
            "Each result entry is a row-column dot product.",
        ],
    )

    _run_calculation(lambda: _print_matrix("AB", multiply(left, right)), details)


def _matrix_determinant() -> None:
    matrix = _read_matrix()
    details = (
        "For 2x2: det([[a,b],[c,d]]) = ad - bc",
        "The determinant is a single number for a square matrix.",
        [
            "Confirm the matrix is square.",
            "Use the 2x2 rule or expand recursively along the first row.",
        ],
    )

    _run_calculation(lambda: _print_value("det(A)", determinant(matrix)), details)


def _matrix_inverse() -> None:
    matrix = _read_matrix()
    details = (
        "A^-1 = adj(A) / det(A), and for 2x2 use (1/det)[[d,-b],[-c,a]]",
        "The inverse reverses the effect of multiplying by the original matrix.",
        [
            "Confirm the matrix is square.",
            "Find det(A); an inverse exists only when det(A) is not 0.",
            "Divide the adjugate matrix by det(A).",
        ],
    )

    _run_calculation(lambda: _print_matrix("A^-1", inverse(matrix)), details)


def _probability_factorial() -> None:
    n = _read_int("Enter n: ")
    details = (
        "n! = n x (n - 1) x ... x 2 x 1",
        "Multiply all whole numbers from n down to 1.",
        [f"Start at 1 and multiply by every integer from 2 to {n}."],
    )

    _run_calculation(lambda: _print_value(f"{n}!", factorial(n)), details)


def _probability_permutations() -> None:
    n = _read_int("Enter n: ")
    r = _read_int("Enter r: ")
    details = (
        "nPr = n! / (n - r)!",
        "Use permutations when order matters.",
        [f"Choose {r} ordered items from {n} total items."],
    )

    _run_calculation(lambda: _print_value(f"{n}P{r}", permutations(n, r)), details)


def _probability_combinations() -> None:
    n = _read_int("Enter n: ")
    r = _read_int("Enter r: ")
    details = (
        "nCr = n! / (r! x (n - r)!)",
        "Use combinations when order does not matter.",
        [f"Choose {r} unordered items from {n} total items."],
    )

    _run_calculation(lambda: _print_value(f"{n}C{r}", combinations(n, r)), details)


def _probability_conditional() -> None:
    probability_a_and_b = _read_float("Enter P(A and B): ")
    probability_b = _read_float("Enter P(B): ")
    details = (
        "P(A|B) = P(A and B) / P(B)",
        "Restrict attention to cases where B happened, then find how often A also happened.",
        [
            f"Use P(A and B) = {_format_number(probability_a_and_b)}.",
            f"Divide by P(B) = {_format_number(probability_b)}.",
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
        "Use this for exactly k successes in n independent trials.",
        [
            f"Count ways to place the successes: {n}C{k}.",
            f"Multiply by p^k = {_format_number(p)}^{k}.",
            f"Multiply by (1 - p)^(n - k) = {_format_number(1 - p)}^{n - k}.",
        ],
    )

    _run_calculation(
        lambda: _print_value("P(X = k)", binomial_probability(n, k, p)),
        details,
    )


def _function_polynomial_evaluation() -> None:
    coefficients = _read_coefficients()
    x = _read_float("Enter x: ")
    details = (
        "Horner's method: result = result x x + next coefficient",
        "Evaluate the polynomial efficiently from highest power to constant term.",
        [
            f"Start with result = 0 and x = {_format_number(x)}.",
            "For each coefficient, multiply the current result by x and add the coefficient.",
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
        "Estimate the slope using points just to the right and left of x.",
        [
            f"Use x = {_format_number(x)} and h = {_format_number(step)}.",
            "Evaluate the polynomial at x + h and x - h.",
            "Divide the difference by 2h.",
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
        "Multiply matching components, then add the products.",
        [
            "Check both vectors have the same number of components.",
            "Multiply each matching pair and add.",
        ],
    )

    _run_calculation(lambda: _print_value("a . b", dot_product(left, right)), details)


def _vector_cross_product() -> None:
    left = _read_vector("Enter 3D vector a components: ")
    right = _read_vector("Enter 3D vector b components: ")
    details = (
        "a x b = [a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1]",
        "The cross product gives a vector perpendicular to both input vectors.",
        [
            "Confirm both vectors have exactly 3 components.",
            "Apply the 3D cross product component formulas.",
        ],
    )

    _run_calculation(
        lambda: _print_vector("a x b", cross_product(left, right)),
        details,
    )


def _statistics_mean() -> None:
    values = _read_number_list("Enter data values: ")
    details = (
        "mean = sum of values / number of values",
        "The mean is the balancing point or average of the data.",
        [
            "Add all data values.",
            f"Divide by the number of values, n = {len(values)}.",
        ],
    )

    _run_calculation(lambda: _print_value("mean", mean(values)), details)


def _statistics_variance() -> None:
    values = _read_number_list("Enter data values: ")
    sample = _read_yes_no("Use sample variance with denominator n - 1? (y/n): ")
    divisor_text = "n - 1" if sample else "n"
    details = (
        f"variance = sum((x - mean)^2) / {divisor_text}",
        "Variance measures spread by averaging squared distances from the mean.",
        [
            "Find the mean.",
            "Subtract the mean from each value and square each difference.",
            f"Divide by {divisor_text}.",
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
        "Standard deviation is a typical distance from the mean.",
        [
            "Calculate the variance.",
            "Take the square root so the answer uses the original data units.",
        ],
    )

    _run_calculation(
        lambda: _print_value(
            "standard deviation",
            standard_deviation(values, sample=sample),
        ),
        details,
    )


def _read_matrix() -> Matrix:
    """Read matrix dimensions and row values from the user."""
    rows = _read_positive_int("Number of rows: ")
    columns = _read_positive_int("Number of columns: ")

    matrix: list[list[float]] = []
    for row_number in range(1, rows + 1):
        while True:
            row_text = input(
                f"Row {row_number} ({columns} numbers separated by spaces): "
            ).strip()

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


def _read_positive_int(prompt: str) -> int:
    """Read a positive integer, retrying until valid."""
    while True:
        value = _read_int(prompt)
        if value > 0:
            return value
        print("Please enter a positive whole number.")


def _read_int(prompt: str) -> int:
    """Read an integer, retrying until the input is valid."""
    while True:
        text = input(prompt).strip()

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

        try:
            return float(text)
        except ValueError:
            print("Please enter a number.")


def _read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer."""
    while True:
        text = input(prompt).strip().lower()

        if text in {"y", "yes"}:
            return True
        if text in {"n", "no"}:
            return False

        print("Please enter y or n.")


def _run_calculation(
    action: Callable[[], None],
    learning_details: LearningDetails,
) -> None:
    """Run one calculation and optionally print learning details."""
    try:
        action()
        if LEARNING_MODE:
            formula, explanation, steps = learning_details
            _print_learning_details(formula, explanation, steps)
    except (TypeError, ValueError) as error:
        print(f"\nError: {error}")
    finally:
        _pause()


def _print_learning_details(
    formula: str,
    explanation: str,
    steps: list[str],
) -> None:
    """Print formula, explanation, and calculation steps."""
    print("\nLearning mode")
    print(f"Formula: {formula}")
    print(f"Meaning: {explanation}")
    print("Steps:")
    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


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


def _matrix_size(matrix: Matrix) -> str:
    """Return a human-readable matrix size."""
    return f"{len(matrix)}x{len(matrix[0])}"


def _toggle_learning_mode() -> None:
    global LEARNING_MODE

    LEARNING_MODE = not LEARNING_MODE
    print(f"Mode switched to {'learning' if LEARNING_MODE else 'fast'}.")
    _pause()


def _pause() -> None:
    try:
        input("\nPress Enter to continue...")
    except EOFError:
        print()


def _back_menu() -> None:
    print("Returning to previous menu.")


def _exit_menu() -> None:
    print("Goodbye.")
