import math
class Shape:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    

class TwoD(Shape):
    def __init__(self, sides=2, **kwargs):
        super().__init__(sides=sides,**kwargs)
        self.sides = sides


class ThreeD(Shape):

    #valid_shapes = ["Cube", "Cuboid", "Sphere"]

    def __init__(self, length=1, width=1, height=1,**kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.width = width
        self.height = height
        

class FourSides(TwoD):
    pass

class Polygon(TwoD):
    pass

class Circle(TwoD):
    pass

class Cube(ThreeD):

    def area(self):
        return 6 * (self.length ** 2)

    def volume(self):
        return self.length * self.height * self.width

class Cuboid(ThreeD):
    def area(self):
        return 2 *(self.length * self.height + self.width*self.length + self.height * self.width)
    
    def volume(self):
        return self.width * self.height * self.length

class Cylinder():
    def __init__(self,radius, heigth):
        self.radius = radius
        self.height = heigth

    def area(self):
        return math.pi * (self.radius ** 2) * (2 + self.height)
    
    def volume(self, radius=1):
        return math.pi * (self.radius ** 2) * self.height

class Sphere:
    def __init__(self,radius,**kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume(self):
        return 4/3 * math.pi * (self.radius ** 3)

class Rectangular(FourSides):
    pass

class Trapezium(FourSides):
    pass

class Parellogram(FourSides):
    pass

class Square(FourSides):
    pass

class Pentagon(Polygon):
    pass

class Hexagon(Polygon):
    pass

class Heptagon(Polygon):
    pass

class Hexagon(Polygon):
    pass

class Octagon(Polygon):
    pass

class Nonagon(Polygon):
    pass

class Decagon(Polygon):
    pass

a = Cube(2,2,2)
b = Sphere(4)
c = Cuboid(2,3,4)
d = Cylinder(4, 5)
print(d.area(),d.volume())

