from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import Game, GameObject


class Component:
    """
    A class to add functionality to GameObjects
    """

    TYPE = "Component"

    def __init__(self) -> None:
        """
        Construct a Component.
        """

        self.parent_game = None
        self.parent_game_object = None

    def _init_component(
        self,
        parent_game: Game,
        parent_game_object: GameObject,
    ) -> None:
        """
        This method is used by breeze. Please do not override or call it.
        """

        self.parent_game = parent_game
        self.parent_game_object = (
            parent_game_object
        )

        self.init()

    def init(self) -> None:
        """
        This method is called when the Component gets added to a GameObject.
        """

    def _update_component(self) -> bool:
        """
        This method is used by breeze. Please do not override or call it.
        """

        return self.update()

    def update(self) -> bool:
        """
        This method is called every frame.

        :returns: True if the Game should continue, False if it should quit
        """

        return True

    def _quit_component(self) -> None:
        """
        This method is used by breeze. Please do not override or call it.
        """

        self.quit()

    def quit(self) -> None:
        """
        This method gets called when the Component is removed from it's parent GameObject.
        """

    def __repr__(self) -> str:
        return f"breeze.core.Component({Component.TYPE})"
