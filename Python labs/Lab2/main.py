from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

if __name__ == "__main__":
    rect = Rectangle(21, 21, "Blue")
    circle = Circle(21, "Green")
    square = Square(21, "Red")
    print(rect, circle, square, sep='\n')
