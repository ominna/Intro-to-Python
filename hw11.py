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
        print(f"The Polar coordinates are: r={r}; theta={theta}")

# Checking on a point
p1 = Point(x=1, y=1)
p1.to_polar()