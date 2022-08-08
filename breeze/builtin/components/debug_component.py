from breeze.core import Component


class DebugComponent(Component):
    def __init__(self) -> None:
        super().__init__()

    def init(self) -> None:
        print(f"\tAdded Component '{self.TYPE}' to '{self.parent_game_object.name}'")

    def update(self) -> bool:
        print(f"\tUpdated Component '{self.TYPE}' of '{self.parent_game_object.name}'")

        return True

    def quit(self) -> None:
        print(f"\tDeleted Component '{self.TYPE}' from '{self.parent_game_object.name}'")
