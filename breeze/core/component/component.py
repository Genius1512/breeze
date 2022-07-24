from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import Game, GameObject


class Component:
    TYPE = "Component"

    def __init__(self) -> None:
        self.parent_game = None
        self.parent_game_object = None

    def _init_component(
        self, parent_game: Game, parent_game_object: GameObject
    ) -> None:
        self.parent_game = parent_game
        self.parent_game_object = parent_game_object

        self.init()

    def init(self) -> None:
        pass

    def _update_component(self) -> bool:
        return self.update()

    def update(self) -> bool:
        return True

    def _quit_component(self) -> None:
        self.quit()

    def quit(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"breeze.core.Component({Component.TYPE})"
