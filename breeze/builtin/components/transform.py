from breeze.core import Component


class Transform(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float = 1,
        height: float = 1,
        rotation: float = 0,
    ):
        super().__init__("Transform")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    def init(self) -> None:
        pass

    def update(self) -> bool:
        return True

    def quit(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"breeze.builtin.components.Transform({self.x}, {self.y}, {self.width}, {self.height}, {self.rotation})"

    @property
    def rect(
        self,
    ) -> tuple[float, float, float, float]:
        return (
            self.x,
            self.y,
            self.width,
            self.height,
        )

    @property
    def top_left(self) -> tuple[float, float]:
        return self.x, self.y

    @property
    def top_right(self) -> tuple[float, float]:
        return self.x + self.width, self.y

    @property
    def bottom_left(self) -> tuple[float, float]:
        return self.x, self.y + self.height

    @property
    def bottom_right(self) -> tuple[float, float]:
        return (
            self.x + self.width,
            self.y + self.height,
        )
