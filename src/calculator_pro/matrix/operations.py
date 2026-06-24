"""Matrix operations for calculator-pro."""

from calculator_pro.matrix.types import Matrix


def add(left: Matrix, right: Matrix) -> Matrix:
    """Add two matrices of the same size.

    Formula:
        If C = A + B, then each entry is c_ij = a_ij + b_ij.

    Plain English:
        Add matching positions in the two matrices.
    """
    left_values = _validate_matrix(left)
    right_values = _validate_matrix(right)

    if _shape(left_values) != _shape(right_values):
        raise ValueError("Matrices must have the same dimensions for addition.")

    return [
        [left_value + right_value for left_value, right_value in zip(left_row, right_row)]
        for left_row, right_row in zip(left_values, right_values)
    ]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    """Multiply two compatible matrices.

    Formula:
        If C = AB, then c_ij is the dot product of row i of A
        and column j of B.

    Plain English:
        Each answer entry comes from multiplying across a row and down a column,
        then adding those products.
    """
    left_values = _validate_matrix(left)
    right_values = _validate_matrix(right)
    left_rows, left_columns = _shape(left_values)
    right_rows, right_columns = _shape(right_values)

    if left_columns != right_rows:
        raise ValueError(
            "Number of columns in the left matrix must equal the number of rows "
            "in the right matrix."
        )

    result: list[list[float]] = []
    for row_index in range(left_rows):
        result_row: list[float] = []
        for column_index in range(right_columns):
            entry = sum(
                left_values[row_index][k] * right_values[k][column_index]
                for k in range(left_columns)
            )
            result_row.append(entry)
        result.append(result_row)

    return result


def determinant(matrix: Matrix) -> float:
    """Calculate the determinant of a square matrix recursively.

    Formula:
        For a 2x2 matrix [[a, b], [c, d]], det = ad - bc.
        For larger matrices, expand along the first row:
        det(A) = sum((-1)^j * a_0j * det(minor_0j)).

    Plain English:
        The determinant is a single number that tells useful facts about a
        square matrix, including whether it has an inverse.
    """
    values = _validate_square_matrix(matrix)
    size = len(values)

    if size == 1:
        return values[0][0]

    if size == 2:
        return values[0][0] * values[1][1] - values[0][1] * values[1][0]

    total = 0.0
    for column_index, entry in enumerate(values[0]):
        sign = -1 if column_index % 2 else 1
        total += sign * entry * determinant(_minor(values, 0, column_index))

    return total


def inverse(matrix: Matrix) -> Matrix:
    """Calculate the inverse of a square matrix.

    Formula:
        For a 2x2 matrix [[a, b], [c, d]],
        A^-1 = (1 / det(A)) * [[d, -b], [-c, a]].

        For larger matrices, this uses the adjugate formula:
        A^-1 = adj(A) / det(A), where adj(A) is the transpose of
        the cofactor matrix.

    Plain English:
        The inverse matrix reverses the effect of the original matrix, similar
        to how division reverses multiplication.
    """
    values = _validate_square_matrix(matrix)
    size = len(values)
    det = determinant(values)

    if det == 0:
        raise ValueError("Matrix is singular and does not have an inverse.")

    if size == 1:
        return [[1 / values[0][0]]]

    if size == 2:
        a, b = values[0]
        c, d = values[1]
        return [[d / det, -b / det], [-c / det, a / det]]

    cofactors: list[list[float]] = []
    for row_index in range(size):
        cofactor_row: list[float] = []
        for column_index in range(size):
            sign = -1 if (row_index + column_index) % 2 else 1
            cofactor = sign * determinant(_minor(values, row_index, column_index))
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = _transpose(cofactors)
    return [[entry / det for entry in row] for row in adjugate]


def _validate_matrix(matrix: Matrix) -> list[list[float]]:
    """Return a rectangular matrix as lists, or raise ValueError."""
    rows = [list(row) for row in matrix]

    if not rows:
        raise ValueError("Matrix must contain at least one row.")

    column_count = len(rows[0])
    if column_count == 0:
        raise ValueError("Matrix rows must contain at least one value.")

    for row in rows:
        if len(row) != column_count:
            raise ValueError("All matrix rows must have the same length.")
        for value in row:
            if not isinstance(value, int | float):
                raise TypeError("Matrix values must be numeric.")

    return [[float(value) for value in row] for row in rows]


def _validate_square_matrix(matrix: Matrix) -> list[list[float]]:
    """Return a square matrix as lists, or raise ValueError."""
    values = _validate_matrix(matrix)
    rows, columns = _shape(values)

    if rows != columns:
        raise ValueError("Matrix must be square.")

    return values


def _shape(matrix: Matrix) -> tuple[int, int]:
    """Return the number of rows and columns in a matrix."""
    return len(matrix), len(matrix[0])


def _minor(matrix: Matrix, removed_row: int, removed_column: int) -> list[list[float]]:
    """Return the matrix left after removing one row and one column."""
    return [
        [
            value
            for column_index, value in enumerate(row)
            if column_index != removed_column
        ]
        for row_index, row in enumerate(matrix)
        if row_index != removed_row
    ]


def _transpose(matrix: Matrix) -> list[list[float]]:
    """Swap rows and columns in a matrix."""
    rows, columns = _shape(matrix)
    return [[matrix[row_index][column_index] for row_index in range(rows)] for column_index in range(columns)]
