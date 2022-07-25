from breeze.core import Component


class DebugComponent(Component):
    def __init__(self) -> None:
        super().__init__()

    def init(self) -> None:
        print(f"Added component '{self.TYPE}' to '{self.parent_game_object.name}'")  # type: ignore

    def update(self) -> bool:
        print(f"Updated component '{self.TYPE}' of '{self.parent_game_object.name}'")  # type: ignore

        return True

    def quit(self) -> None:
        print(f"Deleted component '{self.TYPE}' from '{self.parent_game_object.name}'")  # type: ignore
