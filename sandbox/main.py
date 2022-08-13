from breeze.core import Game
from breeze.builtin.game_objects import (
    DebugGameObject,
)
from breeze.builtin.components import (
    DebugComponent,
)


def main():
    game = Game("Game")

    obj = game.add_game_object(
        DebugGameObject("Obj")
    )
    cmp1 = obj.add_component(
        DebugComponent("Cmp1")
    )
    cmp2 = obj.add_component(
        DebugComponent("Cmp2")
    )

    try:
        while game.update():
            pass
    except KeyboardInterrupt:
        pass

    game.quit()


if __name__ == "__main__":
    main()
