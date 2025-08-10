# Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

# Task Description:
# You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

# polymorphism_demo.py:
# Base Class - Shape:

# Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
# Derived Class - Rectangle:

# Inherits from Shape.
# Attributes: length and width.
# Overrides the area() method to calculate the rectangle’s area using the formula: length × width.

# Derived Class - Circle:
# Inherits from Shape.
# Attributes: radius.
# Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}") 

if __name__ == "__main__":
    main()


