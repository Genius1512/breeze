from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import GameObject

from breeze.exceptions.game_object import (GameObjectNotFoundException,
                                           NameAlreadyTakenException)


class Game:
    def __init__(self, title: str) -> None:
        self.__title: str = title

        self.__game_objects: dict[str, GameObject] = {}
        self.__game_objects_to_delete: list[str] = []

    def update(self) -> bool:
        """
        Update the game.

        :returns: True if the game should continue, otherwise False
        """

        for game_object in self.__game_objects.values():
            if not game_object.update():
                return False

        for name in self.__game_objects_to_delete:
            self.__game_objects[name]._quit_game_object()
            del self.__game_objects[name]

        self.__game_objects_to_delete = []

        return True

    def add_game_object(self, game_object: GameObject) -> GameObject:
        if game_object.name in self.__game_objects:
            raise NameAlreadyTakenException(
                f"A GameObject with name '{game_object.name}' is already added to the game"
            )

        game_object._init_game_object(self)
        self.__game_objects[game_object.name] = game_object

        return game_object

    def get_game_object(self, name: str) -> GameObject:
        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name '{name}' could not be found"
            )

        return self.__game_objects[name]

    def get_all_game_objects(self) -> dict[str, GameObject]:
        return self.__game_objects

    def remove_game_object(self, name: str) -> None:
        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name {name} could not be found"
            )

        self.__game_objects_to_delete.append(name)

    @property
    def title(self) -> str:
        return self.__title

    def __repr__(self) -> str:
        return f"breeze.core.Game(title={self.__title})"
