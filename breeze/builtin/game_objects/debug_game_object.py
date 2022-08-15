from breeze.core import GameObject
from breeze.logger import Logger


class DebugGameObject(GameObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.__logger = Logger(name)

    def init(self) -> None:
        self.__logger.log(f"Added GameObject")

    def update(self) -> bool:
        self.__logger.log(f"Updated GameObject")

        return True

    def quit(self) -> None:
        self.__logger.log(f"Deleted GameObject")
