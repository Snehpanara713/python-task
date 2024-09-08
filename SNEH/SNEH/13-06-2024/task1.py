# -	Create a base class Shape with methods to calculate area and perimeter. 
# 	Derive classes Circle and Rectangle from it and override the methods.

import math

class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    
    
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi*self.radius**2
    
    
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def calculate_area(self):
        return self.length*self.width
    
    def calculate_perimeter(self):
        return 2 *(self.length + self.width)
        
    
        
        
r=7
circle=Circle(r)
circle_area=circle.calculate_area()
circle_perimeter=circle.calculate_perimeter()

print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)



l = 5
w = 7
rectangle = Rectangle(l,w)
rectangle_area=rectangle.calculate_area()
rectangle_perimeter=rectangle.calculate_perimeter()

print("\nRectangle: Length =", l, " Width =", w)
print("Rectangle Perimeter:",rectangle_area)
print("Rectangle Perimeter:",rectangle_perimeter)

