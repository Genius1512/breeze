from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import Component, Game

from breeze.exceptions.component import (
    ComponentAlreadyExistentException,
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
        self.__components_to_delete: list[
            str
        ] = []

        self.parent_game = None
        self.is_active: bool = True

    def _init_game_object(
        self, parent_game: Game
    ):  # TODO: add this as a private method to the Game class
        """
        This method is used by breeze. Please don't override or call it.
        """

        self.parent_game = parent_game

        self.init()

    def init(self) -> None:
        """
        Called when the GameObject is added to a game.
        Add components to the GameObject in this function.
        """

    def _update_game_object(self) -> bool:
        """
        This method is used by breeze. Please don't override or call it.
        """

        for (
            component
        ) in self.__components.values():
            if not component._update_component():
                return False

        for type_ in self.__components_to_delete:
            self.__components[
                type_
            ]._quit_component()
            del self.__components[type_]

        return self.update()

    def update(self) -> bool:
        """
        This method gets called every frame.
        Implement GameObject specific logic here.

        :returns: Returns True if the game should continue, false otherwise
        """

        return True

    def _quit_game_object(self) -> None:
        """
        This method is used by breeze. Don't override or call it.
        """

        self.quit()

    def quit(self) -> None:
        """
        This method gets called when the GameObject is removed.
        """

    def add_component(
        self, component: Component
    ) -> Component:
        if component.TYPE in self.__components:
            raise ComponentAlreadyExistentException(
                f"Cannot add component '{component.TYPE}' a second time"
            )

        component._init_component(self.parent_game, self)  # type: ignore
        self.__components[
            component.TYPE
        ] = component

        return component

    def get_component(
        self, type_: str
    ) -> Component:
        if type_ not in self.__components:
            raise ComponentNotFoundException(
                f"This type of component is not added to this GameObject"
            )

        return self.__components[type_]

    def get_all_components(
        self,
    ) -> dict[str, Component]:
        return self.__components

    def remove_component(
        self, type_: str
    ) -> None:
        if type_ not in self.__components:
            raise ComponentNotFoundException(
                f"Component with type '{type_}' could not be found"
            )

        self.__components_to_delete.append(type_)

    @property
    def name(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return f"breeze.core.GameObject(name={self.__name})"
