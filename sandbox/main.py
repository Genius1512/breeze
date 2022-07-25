from breeze.builtin.components import (
    DebugComponent,
)
from breeze.builtin.game_objects import (
    DebugGameObject,
)
from breeze.core import Game


def main():
    game = Game("Game")

    debug_obj = game.add_game_object(
        DebugGameObject("GameObject")
    )

    debug_component = debug_obj.add_component(
        DebugComponent()
    )

    while game.update():
        pass


if __name__ == "__main__":
    main()
