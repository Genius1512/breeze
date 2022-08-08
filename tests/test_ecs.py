import breeze


class TstingGameObject(breeze.core.GameObject):
    def __init__(self, log: list[str]) -> None:
        super().__init__("obj")

        self.log = log
    
    def init(self) -> None:
        self.log.append("init obj")

    def update(self) -> bool:
        self.log.append("update obj")
        return True

    def quit(self) -> None:
        self.log.append("quit obj")


class TstingComponent(breeze.core.Component):
    TYPE = "cmp"

    def __init__(self, log: list[str]) -> None:
        super().__init__("cmp")

        self.log = log

    def init(self) -> None:
        self.log.append("init cmp")

    def update(self) -> bool:
        self.log.append("update cmp")
        return True

    def quit(self) -> None:
        self.log.append("quit cmp")

 
def test_ecs():
    log: list[str] = []

    game = breeze.core.Game("Test")

    obj = game.add_game_object(TstingGameObject(log))
    _ = obj.add_component(TstingComponent(log))

    game.update()

    game.quit()

    assert log == [
            "init obj",
            "init cmp",
            "update obj",
            "update cmp",
            "quit obj",
            "quit cmp"
            ]

