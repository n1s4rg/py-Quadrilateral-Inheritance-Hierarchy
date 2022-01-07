import math
from builtins import round


# Base Class
class Quadrilateral:
    def _init_(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        # Length of each side
        s1 = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
        s2 = math.sqrt(math.pow((x3 - x2), 2) + math.pow((y3 - y2), 2))
        s3 = math.sqrt(math.pow((x4 - x3), 2) + math.pow((y4 - y3), 2))
        s4 = math.sqrt(math.pow((x1 - x4), 2) + math.pow((y1 - y4), 2))
        return s1, s2, s3, s4

    # Calculating Perimeter
    def perimeter(self, s1, s2, s3, s4):
        return str(round((s1 + s2 + s3 + s4), 2))


class Rectangle(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        s1, s2, s3, s4 = super()._init_(x1, y1, x2, y2, x3, y3, x4, y4)
        print("Perimeter of Rectangle is " + super().perimeter(s1, s2, s3, s4))
        print("Area of rectangle is " + str(round((s1 * s2), 2)))


class Trapezoid(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        s1, s2, s3, s4 = super()._init_(x1, y1, x2, y2, x3, y3, x4, y4)
        print("Perimeter of Trapezoid is " + super().perimeter(s1, s2, s3, s4))


class Square(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        s1, s2, s3, s4 = super()._init_(x1, y1, x2, y2, x3, y3, x4, y4)
        print("Perimeter of Square is " + super().perimeter(s1, s2, s3, s4))
        print("Area of Square is " + str(round(4 * s1, 2)))


class Parallelogram(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        s1, s2, s3, s4 = super()._init_(x1, y1, x2, y2, x3, y3, x4, y4)
        print("Perimeter of Parallelogram is " + super().perimeter(s1, s2, s3, s4))
        print("Area of Parallelogram is " + str(round((s1 * s2 * 0.86), 2)))



rectangle = Rectangle(2, 1, 2, 4, 6, 4, 6, 1)
trapezoid = Trapezoid(1, 1, 3, 3, 6, 3, 8, 1)
square = Square(1, 1, 1, 4, 4, 4, 4, 1)
parallelogram = Parallelogram(1, 1, 2, 4, 5, 4, 4, 1)
