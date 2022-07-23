class Game:
    def __init__(self, title: str) -> None:
        self.title: str = title

    def __repr__(self) -> str:
        return f"breeze.core.Game(title={self.title})"
