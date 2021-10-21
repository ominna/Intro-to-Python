class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)


# Checking with an example

v1 = Vector(2, 3)
v2 = Vector(4, 5)
b = 2

print(f"({v1.x},{v1.y}) + ({v2.x},{v2.y}) = ({v1.__add__(v2).x}, {v1.__add__(v2).y})")
print(f"({v1.x},{v1.y}) - ({v2.x},{v2.y}) = ({v1.__sub__(v2).x}, {v1.__sub__(v2).y})")
print(f"({v1.x},{v1.y}) * {b} = ({v1.__mul__(b).x}, {v1.__mul__(b).y})")
