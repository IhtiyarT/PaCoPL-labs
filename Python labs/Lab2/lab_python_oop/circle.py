from lab_python_oop.shape import Shape
from lab_python_oop.shape_color import Color
from math import pi


class Circle(Shape):
    SHAPE_NAME = "Circle"

    @classmethod
    def get_name(cls):
        return cls.SHAPE_NAME

    def __init__(self, radius, color="Blue"):
        if radius < 0:
            raise TypeError
        self.__radius = radius
        self.color = Color()
        self.color.color = color

    def area(self):
        return round(pi * self.__radius ** 2, 1)

    def __repr__(self):
        return "{} {} with radius = {} and area = {}".format(
            self.color.color,
            self.get_name(),
            self.__radius,
            self.area()
        )
