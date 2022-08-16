from breeze.core import Game
from breeze.core.game_object import GameObject


def main():
    game = Game("Game")

    try:
        while game.update():
            pass
    except KeyboardInterrupt:
        pass

    game.quit()


if __name__ == "__main__":
    main()
