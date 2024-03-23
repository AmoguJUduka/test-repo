class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Serialize:
    def serialize(self):
        print(",".join([f"{k} = {v}" for k, v in self.__dict__.items()]))

class Rectangle(Shape,Serialize):
    def __init__(self,x, y, width, height):
        super().__init__(x,y)
        self.width = width
        self.height = height

class Circle(Shape, Serialize):
    def __init__(self, x,y,radius):
        super().__init__(x,y)
        self.radius = radius


r = Rectangle(0, 0, 100, 50)
c = Circle(0, 0, 40)
r.serialize()
c.serialize()

