import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x_, y_):
        self.x = x_
        self.y = y_

    def distance(self, other_value):
        return math.sqrt((self.x - other_value.x) **2 + (self.y - other_value.y)**2)
        

    def __repr__(self):
        return f"({self.x}, {self.y})"

a = Point(2, 4)
b = Point(5, 6)

print(a)  # Output: Point(2, 4)
print(b)  # Output: Point(5, 6)

print(a.distance(b))
