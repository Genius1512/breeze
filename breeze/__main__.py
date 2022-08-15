from argparse import (
    ArgumentError,
    ArgumentParser,
    Namespace,
)
import os
import re
from sys import argv, exit


MAIN_SCRIPT = """from breeze.core import Game


def main():
    game = Game("{}")

    try:
        while game.update():
            pass
    except KeyboardInterrupt:
        pass

    game.update()


if __name__ == "__main__":
    main()
"""


COMPONENT_CODE = """from breeze.core import Component


class {0}(Component):
    def __init__(self):
        super().__init__("{0}")

    # Called when the Component is added to a GameObject
    def init(self) -> None:
        pass
    
    # Called every frame
    def update(self) -> bool:
        return True

    # Called when the Component is deleted
    def quit(self) -> None:
        pass
"""


GAMEOBJECT_CODE = """from breeze.core import GameObject


class {0}(GameObject):
    def __init__(self):
        super().__init__("{0}")

    # Called when the GameObject is added to a Game
    def init(self) -> None:
        pass

    # Called every frame
    def update(self) -> bool:
        return True

    # Called when the GameObject is deleted
    def quit(self) -> None:
        pass
"""


def parse_args(args: list[str]) -> Namespace:
    parser = ArgumentParser()

    action = parser.add_subparsers(
        dest="action",
        description="The action to make",
    )
    action.required = True

    new_parser = action.add_parser(
        "new",
        help="Add a Gameobject or a Component to the project",
    )
    new_parser.add_argument(
        "type",
        choices=["game_object", "component"],
        help="Add a GameObject or a Component",
    )
    new_parser.add_argument(
        "name",
        help="The name of the GameObject/Component to add",
    )

    init_parser = action.add_parser(
        "init", help="Create a new project"
    )
    init_parser.add_argument(
        "name", help="The name of the project"
    )
    init_parser.add_argument(
        "-o",
        "--out",
        default=".",
        help="The directory to create the project in.",
    )

    return parser.parse_args(args)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if args.action == "init":
        project_name = args.name
        project_dir = args.out

        os.mkdir(
            os.path.join(
                project_dir, project_name
            )
        )
        os.mkdir(
            os.path.join(
                project_dir,
                project_name,
                "scripts",
            )
        )

        with open(
            os.path.join(
                project_dir,
                project_name,
                "scripts",
                "main.py",
            ),
            "w",
        ) as f:
            f.write(
                MAIN_SCRIPT.format(project_name)
            )

        with open(
            os.path.join(
                project_dir,
                project_name,
                "requirements.txt",
            ),
            "w",
        ) as f:
            f.write("breeze\n")

    if args.action == "new":
        type_: str = args.type
        entity_name: str = args.name

        text: str = ""

        match type_:
            case "component":
                text = COMPONENT_CODE.format(
                    entity_name
                )

            case "game_object":
                text = GAMEOBJECT_CODE.format(
                    entity_name
                )

        entity_name = re.sub(
            r"(?<!^)(?=[A-Z])", "_", entity_name
        ).lower()

        with open(f"{entity_name}.py", "w") as f:
            f.write(text)

    return 0


if __name__ == "__main__":
    exit(main(argv[1:]))
