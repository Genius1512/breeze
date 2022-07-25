from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import Component, Game

from breeze.exceptions.component import (ComponentAlreadyExistentException,
                                         ComponentNotFoundException)


class GameObject:
    def __init__(self, name: str) -> None:
        self.__name = name

        self.__components: dict[str, Component] = {}
        self.__components_to_delete: list[str] = []

        self.parent_game = None

    def _init_game_object(self, parent_game: Game):
        self.parent_game = parent_game

        self.init()

    def init(self) -> None:
        pass

    def _update_game_object(self) -> bool:
        for component in self.__components.values():
            if not component._update_component():
                return False

        for type_ in self.__components_to_delete:
            self.__components[type_]._quit_component()
            del self.__components[type_]

        return self.update()

    def update(self) -> bool:
        return True

    def _quit_game_object(self) -> None:
        self.quit()

    def quit(self) -> None:
        pass

    def add_component(self, component: Component) -> Component:
        if component.TYPE in self.__components:
            raise ComponentAlreadyExistentException(
                f"Cannot add component '{component.TYPE}' a second time"
            )

        component._init_component(self.parent_game, self)  # type: ignore
        self.__components[component.TYPE] = component

        return component

    def get_component(self, type_: str) -> Component:
        if type_ not in self.__components:
            raise ComponentNotFoundException(
                f"This type of component is not added to this GameObject"
            )

        return self.__components[type_]

    def get_all_components(self) -> dict[str, Component]:
        return self.__components

    def remove_component(self, type_: str) -> None:
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
