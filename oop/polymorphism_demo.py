import math

# Base class
class Shape:
    def area(self):
        """Base area method meant to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override this method")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle using the formula π * r^2."""
        return math.pi * (self.radius ** 2)
