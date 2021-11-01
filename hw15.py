import math

class Figure():
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, x):
        self.x = x
    def area(self):
        return "Area: {}" .format(self.x * self.x)
    def perimeter(self):
        return "Perimeter: {}" .format(4 * self.x)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        if (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b:
            return "Perimeter: {}" .format(self.a + self.b + self.c)
        else:
            return "Impossible triangle measures given."
    def area(self):
        if (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b:
            return "Area: {}" .format(round(math.sqrt(((self.a + self.b + self.c)/2)
                            * (((self.a + self.b + self.c)/2) - self.a)
                            * (((self.a + self.b + self.c)/2) - self.b)
                            * (((self.a + self.b + self.c)/2) - self.c))), 2)
        else:
            return "Impossible triangle measures given."

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def area(self):
        return "Area: {}" .format(round(math.pi * self.r * self.r, 2))
    def perimeter(self):
        return "Perimeter: {}" .format(round(2 * math.pi * self.r, 2))


# Examples of using the class

# Square
square1 = Square(4)
print(square1.area())
print(square1.perimeter())

# Valid triangle
triangle1 = Triangle(18,24,30)
print(triangle1.area())
print(triangle1.perimeter())

# Invalid triangle
triangle1 = Triangle(1,2,3)
print(triangle1.area())
print(triangle1.perimeter())

# Circle
circle1 = Circle(5)
print(circle1.area())
print(circle1.perimeter())
