from breeze.core import Component


class TriangleRenderer(Component):
    def __init__(
        self,
        corner_one: tuple[float, float],
        corner_two: tuple[float, float],
        corner_three: tuple[float, float],
    ):
        super().__init__("TriangleRenderer")

        self.corner_one = corner_one
        self.corner_two = corner_two
        self.corner_three = corner_three

    # Called when the Component is added to a GameObject
    def init(self) -> None:
        pass

    # Called every frame
    def update(self) -> bool:
        return True

    # Called when the Component is deleted
    def quit(self) -> None:
        pass
