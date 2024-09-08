from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    SHAPE_NAME = "Square"

    @classmethod
    def get_name(cls):
        return cls.SHAPE_NAME

    def __init__(self, side, color):
        self.__side = side
        super().__init__(self.__side, self.__side, color)

    def area(self):
        return self.__side ** 2

    def __repr__(self):
        return "{} {} with side = {} and area = {}".format(
            self.color.color,
            self.get_name(),
            self.__side,
            self.area()
        )
