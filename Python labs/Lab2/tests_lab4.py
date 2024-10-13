import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle


class TestShapesMethods(unittest.TestCase):
    # rectangle tests
    def test_rectangle_get_name(self):
        rect = Rectangle
        self.assertEqual(rect.get_name(), "Rectangle")

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(12, 21).area(), 252)
        self.assertEqual(Rectangle(2.4, 11.2,).area(), 26.88)
        with self.assertRaises(TypeError):
            Rectangle(-9, 4)

    # circle tests
    def test_circle_get_name(self):
        circle = Circle
        self.assertEqual(circle.get_name(), "Circle")

    def test_circle_area(self):
        self.assertEqual(Circle(12).area(), 452.4)
        self.assertEqual(Circle(9).area(), 254.5)
        with self.assertRaises(TypeError):
            Circle(-9)


if __name__ == '__main__':
    unittest.main()
