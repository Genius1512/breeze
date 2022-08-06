from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from breeze.core import GameObject

import glfw
from OpenGL.GL import *

from breeze.exceptions.game import (
    GLFWCouldNotCreateWindowException,
    GlFWInitException
)

from breeze.exceptions.game_object import (
    GameObjectNotFoundException,
    NameAlreadyTakenException,
)


class Game:
    """
    The main class of breeze. It represents a game.
    """

    def __init__(self, title: str) -> None:
        """
        Construct a game.

        :param title: The title of the game. Will be displayed in the title bar of the window.
        """
        self.__title: str = title

        self.__game_objects: dict[
            str, GameObject
        ] = {}
        self.__game_objects_to_delete: list[
            str
        ] = []

        # OpenGL stuff
        if not glfw.init():
            raise GlFWInitException("Could not init GLFW")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.__window = glfw.create_window(800, 600, self.__title, None, None)
        if not self.__window:
            self.quit()
            raise GLFWCouldNotCreateWindowException("Could not create window")

        glfw.make_context_current(self.__window)
        glfw.set_framebuffer_size_callback(self.__window, self.__framebuffer_size_callback)

    def update(self) -> bool:
        """
        Update the game.

        :returns: True if the game should continue, otherwise False
        """

        if glfw.window_should_close(self.__window):
            return False

        self.__process_input(self.__window)

        for (
            game_object
        ) in self.__game_objects.values():
            if game_object.is_active:
                if (
                    not game_object._update_game_object()
                ):  # TODO: make non-overridable
                    return False

        for name in self.__game_objects_to_delete:
            self.__game_objects[
                name
            ]._quit_game_object()
            del self.__game_objects[name]

        self.__game_objects_to_delete = []

        glfw.swap_buffers(self.__window)
        glfw.poll_events()

        return True

    def add_game_object(
        self, game_object: GameObject
    ) -> GameObject:
        """
        Add the given GameObject to the game.
        Raises NameAlreadyTakenException when there is already a GameObject with this name.

        :param game_object: The GameObject to add
        :returns: The given GameObject. This is to enable
                  a syntax like this: player = game.add_game_object(GameObject("Player"))
        """

        if (
            game_object.name
            in self.__game_objects
        ):
            raise NameAlreadyTakenException(
                f"A GameObject with name '{game_object.name}' is already added to the game"
            )

        game_object._init_game_object(self)
        self.__game_objects[
            game_object.name
        ] = game_object

        return game_object

    def get_game_object(
        self, name: str
    ) -> GameObject:
        """
        Get the GameObject with the given name.
        Raises GameObjectNotFoundException if there is no GameObject with this name.

        :param name: The name of the GameObject to get

        :returns: The GameObject with the given name
        """

        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name '{name}' could not be found"
            )

        return self.__game_objects[name]

    def get_all_game_objects(
        self,
    ) -> dict[str, GameObject]:
        """
        Get all GameObjects added to the game.

        :returns: A dictionary of GameObjects with their name as keys
        """

        return self.__game_objects

    def remove_game_object(
        self, name: str
    ) -> None:
        """
        Remove the GameObject with the given name from the game.
        This calls the 'quit' method of the GameObject
        Raises GameObjectNotFoundException if there is no GameObject
        with the given name.

        :param name: The name of the GameObject to remove
        """

        if name not in self.__game_objects:
            raise GameObjectNotFoundException(
                f"A GameObject with name {name} could not be found"
            )

        self.__game_objects_to_delete.append(name)

    def quit(self) -> None:
        for game_object in self.__game_objects.values():
            game_object._quit_game_object()

        glfw.terminate()

    # GLFW
    def __framebuffer_size_callback(self, window, width: int, height: int):
        glViewport(0, 0, width, height)

    def __process_input(self, window):
        pass

    @property
    def title(self) -> str:
        """
        The title of the GameObjet.
        """

        return self.__title

    def __repr__(self) -> str:
        return f"breeze.core.Game(title={self.__title})"
