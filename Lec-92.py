# Working of class, constructor, method and object:

class Circle:
    pi= 22/7 #class object attribute
    def __init__(self,r):
        self.radius = r

    def circumference (self):
        return 2*self.pi*self.radius

    def area (self):
        return Circle.pi* (self.radius**2) # Circle.pi is a class object attribute

circle_1 = Circle(21)
print(circle_1.circumference())
print(circle_1.area())

circle_2 = Circle(7)
print(circle_2.area())
# **************************************************************************************
class rectangle:
    def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area (self):
        return self.length*self.breadth

    def perimeter (self):
        return 2*(self.length + self.breadth)

rect_1 = rectangle (5,2)
print(rect_1.area())
print(rect_1.perimeter())