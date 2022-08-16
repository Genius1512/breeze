from __future__ import annotations

from typing import TYPE_CHECKING

from breeze.exceptions.game import (
    CannotRebindParentGame,
)
from breeze.exceptions.game_object import (
    CannotRebindParentGameObject,
)

if TYPE_CHECKING:
    from breeze.core import Game, GameObject


class Component:
    """
    A class to add functionality to GameObjects
    """

    def __init__(self, name: str) -> None:
        """
        Construct a Component.
        """

        self.__name = name

        self.__parent_game: Game = None  # type: ignore
        self.__set_parent_game: bool = False

        self.__parent_game_object: GameObject = None  # type: ignore
        self.__set_parent_game_object: bool = (
            False
        )

        self.is_active: bool = True

    def init(self) -> None:
        """
        This method is called when the Component gets added to a GameObject.
        """

    def update(self) -> bool:
        """
        This method is called every frame.

        :returns: True if the Game should continue, False if it should quit
        """

        return True

    def quit(self) -> None:
        """
        This method gets called when the Component is removed from it's parent GameObject.
        """

    @property
    def parent_game(self):
        """A reference to the parent game"""
        return self.__parent_game

    @parent_game.setter
    def parent_game(self, value):
        if not self.__set_parent_game:
            self._parent_game = value
            self.__set_parent_game = True
        else:
            raise CannotRebindParentGame()

    @property
    def parent_game_object(self):
        """A reference to the parent GameObject"""
        return self.__parent_game_object

    @parent_game_object.setter
    def parent_game_object(self, value):
        if not self.__set_parent_game_object:
            self._parent_game_object = value
            self.__set_parent_game_object = True
        else:
            raise CannotRebindParentGameObject()

    @property
    def name(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return f"breeze.core.Component({Component.name})"
