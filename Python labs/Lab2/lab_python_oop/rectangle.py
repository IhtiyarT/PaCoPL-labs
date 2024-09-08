from lab_python_oop.shape import Shape
from lab_python_oop.shape_color import Color


class Rectangle(Shape):
    SHAPE_NAME = "Rectangle"

    @classmethod
    def get_name(cls):
        return cls.SHAPE_NAME

    def __init__(self, hight, width, color):
        self.__hight = hight
        self.__width = width
        self.color = Color()
        self.color.color = color

    def area(self):
        return self.__hight * self.__width

    def __repr__(self):
        return "{} {} with params = {}/{} and area = {}".format(
            self.color.color,
            self.get_name(),
            self.__hight,
            self.__width,
            self.area()
        )
