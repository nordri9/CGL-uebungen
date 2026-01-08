import numpy as np
from dataclasses import dataclass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return np.pi*(self.radius**2)
    def __repr__(self):
        return f"Person(radius={self.radius})"
        
        
c = Circle(3) # Radius
print(c.area())

print(Circle(3))

@dataclass
class Rectangle:
    hight : int
    width : int

    def area(self):
        return self.hight*self.width
    
print(Rectangle(2,3))