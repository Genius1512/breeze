from os import path

import toml

import breeze


def test_version():
    with open(
        path.join(
            path.dirname(path.dirname(__file__)),
            "pyproject.toml",
        ),
        "r",
    ) as f:
        parsed_toml = toml.load(f)

    assert (
        breeze.__version__
        == parsed_toml["tool"]["poetry"][
            "version"
        ]
    )
