class Game:
    def __init__(self, title: str) -> None:
        self.title: str = title

    def update(self) -> bool:
        """
        Update the game.

        :return: True if the game should continue, otherwise False
        """
        return True

    def __repr__(self) -> str:
        return f"breeze.core.Game(title={self.title})"
