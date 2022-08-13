from argparse import (
    ArgumentError,
    ArgumentParser,
    Namespace,
)
import os
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

    print(args)

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
        type_ = args.type
        entity_name = args.name

    return 0


if __name__ == "__main__":
    exit(main(argv[1:]))
