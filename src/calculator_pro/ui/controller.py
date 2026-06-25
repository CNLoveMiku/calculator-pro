"""Reusable menu controller for text-based interfaces."""

from collections.abc import Callable


MenuAction = Callable[[], None]


class MenuController:
    """Small controller that owns menu rendering and dispatch."""

    def __init__(self, mode_label: Callable[[], str]) -> None:
        self.mode_label = mode_label

    def run(
        self,
        title: str,
        actions: dict[str, tuple[str, MenuAction]],
        print_header: Callable[[str], None],
    ) -> None:
        """Render a menu loop and call selected handlers."""
        while True:
            print_header(title)
            print(f"Mode: {self.mode_label()}")
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
