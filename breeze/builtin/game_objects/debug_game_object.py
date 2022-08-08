from breeze.core import GameObject


class DebugGameObject(GameObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def init(self) -> None:
        print(f"Added GameObject '{self.name}'")

    def update(self) -> bool:
        print(f"Updated GameObject '{self.name}'")

        return True

    def quit(self) -> None:
        print(f"Deleted GameObject '{self.name}'")
