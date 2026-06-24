"""Command-line entry point for calculator-pro."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from calculator_pro.cli.menu import run_cli


def main() -> None:
    """Start the calculator-pro CLI."""
    run_cli()


if __name__ == "__main__":
    main()
