from breeze import builtin
from breeze.core import Game


def main():
    game = Game("Game")

    dbg_game_object = game.add_game_object(builtin.game_objects.DebugGameObject("Player"))
    dbg_component = dbg_game_object.add_component(builtin.components.DebugComponent())

    try:
        for _ in range(10):
            game.update()
    except KeyboardInterrupt:
        pass

    game.quit()


if __name__ == "__main__":
    main()

