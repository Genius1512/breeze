from breeze.core import Game


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
