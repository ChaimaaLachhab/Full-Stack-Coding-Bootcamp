# Exercise 1 : Geometry

import math

class Circle:
    def __init__(self, radius=1.0):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def compute_perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def compute_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def description(self):
        """Prints the definition of a circle."""
        print("A circle is a shape with all points equidistant from its center.")

# Example usage:
circle1 = Circle(5)
print("Perimeter:", circle1.compute_perimeter())
print("Area:", circle1.compute_area())
circle1.description()
