from breeze.core import Component
from breeze.logger import Logger


class DebugComponent(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.__logger = Logger(name)

    def init(self) -> None:
        self.__logger.log(
            f"\tAdded Component to {self.parent_game_object.name}'"
        )

    def update(self) -> bool:
        self.__logger.log(
            f"\tUpdated Component of '{self.parent_game_object.name}'"
        )

        return True

    def quit(self) -> None:
        self.__logger.log(
            f"\tDeleted Component from '{self.parent_game_object.name}'"
        )
