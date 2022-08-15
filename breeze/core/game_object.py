from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import Component, Game

from breeze.exceptions.component import (
    ComponentNameAlreadyTakenException,
    ComponentNotFoundException,
)


class GameObject:
    """
    A class to represents objects like players or walls in the game.
    """

    def __init__(self, name: str) -> None:
        """
        Construct a GameObject.

        :param name: The name of the GameObject
        """

        self.__name = name

        self.__components: dict[
            str, Component
        ] = {}
        self.components_to_delete: list[str] = []

        self.parent_game: Game = None  # type: ignore
        self.is_active: bool = True

    def init(self) -> None:
        """
        Called when the GameObject is added to a game.
        Add components to the GameObject in this function.
        """

    def update(self) -> bool:
        """
        This method gets called every frame.
        Implement GameObject specific logic here.

        :returns: Returns True if the game should continue, false otherwise
        """

        return True

    def quit(self) -> None:
        """
        This method gets called when the GameObject is removed.
        """

    def add_component(
        self, component: Component
    ) -> Component:
        """
        Add the given component to the GameObject.
        The init() method of the Component will be called.
        If a Component of this type has already been added to the GameObject,
        ComponentAlreadyExistentException will be raised.

        :param component: The Component to add
        """
        if component.name in self.__components:
            raise ComponentNameAlreadyTakenException(
                f"A Component with name {component.name} is already added to the GameObject"
            )

        component.parent_game = self.parent_game
        component.parent_game_object = self
        component.init()

        self.__components[
            component.name
        ] = component

        return component

    def get_component(
        self, name: str
    ) -> Component:
        """
        Get the Component with the given type.
        If there is no such Component, ComponentNotFoundException will
        be raised.

        :param type_: The type of the Component to get
        """
        if name not in self.__components:
            raise ComponentNotFoundException(
                f"This type of component is not added to this GameObject"
            )

        return self.__components[name]

    def get_all_components(
        self,
    ) -> dict[str, Component]:
        """
        Get all Components of the GameObject.

        :returns: A dictionary with all Components with their type as keys
        """
        return self.__components

    def remove_component(self, name: str) -> None:
        """
        Remove the Component with the given type.
        This will call the quit() method of the component.
        Raises ComponentNotFoundException, if there is no Component with the given type.

        :param type_: The type of the Component to remove
        """
        if name not in self.__components:
            raise ComponentNotFoundException(
                f"Component with type '{name}' could not be found"
            )

        self.components_to_delete.append(name)

    @property
    def name(self) -> str:
        """
        The name of the GameObject
        """
        return self.__name

    def __repr__(self) -> str:
        return f"breeze.core.GameObject(name={self.__name})"
