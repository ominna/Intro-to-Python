import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Converting Cartesian coordinates to Polar coordinates
    def to_polar(self):
        r = str(round(math.sqrt(self.x * self.x + self.y * self.y),2))   # radius
        theta = math.atan(self.y / self.x)                               # angle in radians
        theta = 180 * theta / math.pi                                    # angle in degrees
        result = (r, theta)
        return result

# Checking on a point
p1 = Point(x=1, y=1)
print(p1.to_polar())
