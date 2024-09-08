class Color:
    def __init__(self):
        self.__color_property = None

    @property
    def color(self) -> str:
        return self.__color_property

    @color.setter
    def color(self, color):
        self.__color_property = color

    def __repr__(self):
        return str(self.__color_property)
