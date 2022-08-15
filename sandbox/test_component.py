from breeze.core import Component


class TestComponent(Component):
    def __init__(self):
        super().__init__("TestComponent")

    # Called when the Component is added to a GameObject
    def init(self) -> None:
        print("init")

    # Called every frame
    def update(self) -> bool:
        return True

    # Called when the Component is deleted
    def quit(self) -> None:
        pass
