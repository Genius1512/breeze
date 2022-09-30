import pygame
from breeze.color.color import Color

from breeze.core import Component


class RectangleRenderer(Component):
    def __init__(self, color: Color):
        super().__init__("RectangleRenderer")

        self.color = color

    # Called when the Component is added to a GameObject
    def init(self) -> None:
        pass

    # Called every frame
    def update(self) -> bool:
        pygame.draw.rect(
            self.parent_game.window.screen,
            self.color.rgba,
            self.parent_game_object.get_component(
                "Transform"
            ).rect,
        )

        return True

    # Called when the Component is deleted
    def quit(self) -> None:
        pass
