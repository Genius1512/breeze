import pygame

from breeze.color import Color


class Window:
    def __init__(
            self, title: str, width: int, height: int, background: Color
    ) -> None:
        self.__title: str = title
        self.__width: int = width
        self.__height: int = height
        self.background: Color = background

        self.__fps: float = 0
        self.__framecount: int = 0
        self.__delta_time: float = 0

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.__width, self.__height)
        )
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()

    def update(self) -> bool:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.screen.fill(self.background.hex)

        self.__fps = self.clock.get_fps()
        self.__framecount += 1
        self.__delta_time = self.clock.tick(60) / 1000
    
        return True

    @property
    def title(self) -> str:
        return self.__title

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def fps(self) -> float:
        return self.__fps

    @property
    def framecount(self) -> int:
        return self.__framecount

    @property
    def delta_time(self) -> float:
        return self.__delta_time
