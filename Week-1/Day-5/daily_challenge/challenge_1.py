import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        # If radius is provided, use it. If diameter is provided, calculate radius.
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")
    
    # Getter for diameter
    @property
    def diameter(self):
        return self.radius * 2

    # Setter for diameter (updates the radius)
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    # Method to compute the area
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # String representation of the Circle
    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area():.2f}"
    
    # Dunder method to add two circles
    def __add__(self, other):
        # Add the radii of two circles and return a new circle
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    # Dunder method to compare circles based on size (radius)
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
    
    # Dunder method to check if circles are equal
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

# Testing the Circle class
circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)

# Print circles
print(circle1)
print(circle2)

# Adding circles
circle3 = circle1 + circle2
print(f"New circle created by adding circle1 and circle2: {circle3}")

# Compare circles (which is bigger)
print(f"Is circle1 smaller than circle2? {circle1 < circle2}")
print(f"Are circle1 and circle2 equal? {circle1 == circle2}")

# Sort circles in a list
circles = [Circle(radius=4), Circle(radius=10), Circle(radius=6)]
sorted_circles = sorted(circles)
print("Sorted circles by radius:")
for circle in sorted_circles:
    print(circle)
