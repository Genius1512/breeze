from breeze.core import Game
from breeze.color import White


def main():
    game = Game("Game", 800, 600, White())

    try:
        while game.update():
            pass
    except KeyboardInterrupt:
        pass

    game.quit()


if __name__ == "__main__":
    main()
