"""Safe math expression parsing for user-entered functions."""

from __future__ import annotations

import ast
from collections.abc import Callable
from math import acos, asin, atan, cos, e, exp, log, pi, sin, sqrt, tan


AllowedFunction = Callable[..., float]

ALLOWED_NAMES: dict[str, float | AllowedFunction] = {
    "x": 0.0,
    "pi": pi,
    "e": e,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "sqrt": sqrt,
    "log": log,
    "exp": exp,
    "asin": asin,
    "acos": acos,
    "atan": atan,
    "abs": abs,
}

ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Call,
    ast.Name,
    ast.Load,
    ast.Constant,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.USub,
    ast.UAdd,
)


def compile_math_expression(expression: str) -> Callable[[float], float]:
    """Compile a safe single-variable math expression into f(x).

    Supported examples:
        x^2 - 4, sin(x), cos(x), sqrt(x + 4), exp(-x^2)
    """
    normalized = expression.strip().replace("^", "**")
    if not normalized:
        raise ValueError("Expression cannot be empty.")

    tree = ast.parse(normalized, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError(f"Unsupported expression element: {type(node).__name__}.")
        if isinstance(node, ast.Name) and node.id not in ALLOWED_NAMES:
            raise ValueError(f"Unsupported name: {node.id}.")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in ALLOWED_NAMES:
                raise ValueError("Only approved math functions can be called.")

    code = compile(tree, "<math-expression>", "eval")

    def function(x: float) -> float:
        namespace = dict(ALLOWED_NAMES)
        namespace["x"] = x
        value = eval(code, {"__builtins__": {}}, namespace)
        if not isinstance(value, int | float):
            raise ValueError("Expression must evaluate to a number.")
        return float(value)

    return function
