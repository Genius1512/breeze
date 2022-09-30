class Color:
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    @property
    def rgb(self) -> tuple[int, int, int]:
        return self.r, self.g, self.b

    @property
    def rgba(self) -> tuple[int, int, int, int]:
        return self.r, self.g, self.b, self.a

    @property
    def hex(self) -> str:
        return "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

    def __repr__(self) -> str:
        return f"breeze.color.Color({self.r}, {self.g}, {self.b}, {self.a})"


class Transparent(Color):
    def __init__(self):
        super().__init__(0, 0, 0, 0)


class Black(Color):
    def __init__(self):
        super().__init__(0, 0, 0)


class White(Color):
    def __init__(self):
        super().__init__(255, 255, 255)


class Red(Color):
    def __init__(self):
        super().__init__(255, 0, 0, 0)


class Green(Color):
    def __init__(self):
        super().__init__(0, 255, 0)


class Blue(Color):
    def __init__(self):
        super().__init__(0, 0, 255)


class Yellow(Color):
    def __init__(self):
        super().__init__(255, 255, 0)


class Cyan(Color):
    def __init__(self):
        super().__init__(0, 255, 255)


class Magenta(Color):
    def __init__(self):
        super().__init__(255, 0, 255)

