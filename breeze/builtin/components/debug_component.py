from breeze.core import Component


class DebugComponent(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def init(self) -> None:
        print(f"\tAdded Component '{self.name}' to '{self.parent_game_object.name}'")

    def update(self) -> bool:
        print(f"\tUpdated Component '{self.name}' of '{self.parent_game_object.name}'")

        return True

    def quit(self) -> None:
        print(f"\tDeleted Component '{self.name}' from '{self.parent_game_object.name}'")
