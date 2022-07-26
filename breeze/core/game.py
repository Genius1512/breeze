from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import GameObject

from breeze.exceptions.game_object import (
    GameObjectNotFoundException,
    ObjectNameAlreadyTakenException,
)


class Game:
    """
    The main class of breeze. It represents a game.
    """

    def __init__(self, title: str) -> None:
        """
        Construct a game.

        :param title: The title of the game. Will be displayed in the title bar of the window.
        """
        self.__title: str = title

        self.__game_objects: dict[
            str, GameObject
        ] = {}
        self.__game_objects_to_delete: list[
            str
        ] = []

    def update(self) -> bool:
        """
        Update the game.

        :returns: True if the game should continue, otherwise False
        """

        for (
            game_object
        ) in (
            self.__game_objects.values()
        ):  # Loop over game_objects
            if (
                game_object.is_active
            ):  # Check if the GameObject is active
                if (
                    not game_object.update()
                ):  # Update the GameObject
                    return False  # Quit if should quit

                for (
                    component
                ) in (
                    game_object.get_all_components().values()
                ):  # Loop over Components of GameObject
                    if (
                        component.is_active
                    ):  # Check if the GameObject is active
                        if (
                            not component.update()
                        ):  # Update the Component
                            return False  # Quit if should quit

            for (
                name
            ) in (
                game_object.components_to_delete
            ):  # Loop over the Components to delete of the Component
                game_object.get_component(
                    name
                ).quit()  # Call the quit method
                del game_object.__components[
                    name
                ]  # Delete the Component

        for (
            name
        ) in (
            self.__game_objects_to_delete
        ):  # Loop over the GameObjects to delete
            for component in (
                self.__game_objects[name]
                .get_all_components()
                .values()
            ):  # Loop over its Components
                component.quit()  # Call the quit method

            self.__game_objects[
                name
            ].quit()  # Call the quit method
            del self.__game_objects[
                name
            ]  # Delete the GameObject

        return True

    def add_game_object(
        self, game_object: GameObject
    ) -> GameObject:
        """
        Add the given GameObject to the game.
        Raises NameAlreadyTakenException when there is already a GameObject with this name.

        :param game_object: The GameObject to add
        :returns: The given GameObject. This is to enable
                  a syntax like this: player = game.add_game_object(GameObject("Player"))
        """

        if (
            game_object.name
            in self.__game_objects
        ):
            raise ObjectNameAlreadyTakenException(
                f"A GameObject with name '{game_object.name}' is already added to the game"
            )

        game_object.parent_game = self
        game_object.init()

        self.__game_objects[
            game_object.name
        ] = game_object

        return game_object

    def get_game_object(
        self, name: str
    ) -> GameObject:
        """
        Get the GameObject with the given name.
        Raises GameObjectNotFoundException if there is no GameObject with this name.

        :param name: The name of the GameObject to get

        :returns: The GameObject with the given name
        """

        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name '{name}' could not be found"
            )

        return self.__game_objects[name]

    def get_all_game_objects(
        self,
    ) -> dict[str, GameObject]:
        """
        Get all GameObjects added to the game.

        :returns: A dictionary of GameObjects with their name as keys
        """

        return self.__game_objects

    def remove_game_object(
        self, name: str
    ) -> None:
        """
        Remove the GameObject with the given name from the game.
        This calls the 'quit' method of the GameObject
        Raises GameObjectNotFoundException if there is no GameObject
        with the given name.

        :param name: The name of the GameObject to remove
        """

        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name {name} could not be found"
            )

        self.__game_objects_to_delete.append(name)

    def quit(self) -> None:
        for (
            game_object
        ) in self.__game_objects.values():
            game_object.quit()

            for (
                component
            ) in (
                game_object.get_all_components().values()
            ):
                component.quit()

    @property
    def title(self) -> str:
        """
        The title of the GameObjet.
        """

        return self.__title

    def __repr__(self) -> str:
        return f"breeze.core.Game(title={self.__title})"
