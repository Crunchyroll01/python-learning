from abc import ABC, abstractmethod
import math

# Cody Fancil, 11/18/2025
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        return "This is a "+type(self).__name__
    @staticmethod
    def validate_positive(value, name):
        try:
            num = float(value)
        except:
            print(f"Error: {name} must be a number.")
            return False   
        if num <= 0:
            print(f"Error: {name} must be positive.")
            return False   
        return True

class Circle(Shape):
    def __init__(self, radius):
        if not Shape.validate_positive(radius, 'radius'):
            raise ValueError('radius must be positive')
        self.radius = float(radius)
    
    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2 * math.pi*self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if not Shape.validate_positive(width, 'width') or not Shape.validate_positive(height, 'height'):
            raise ValueError('width and height must be positive')
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width+self.height)
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not (Shape.validate_positive(side1, 'side1') and 
                Shape.validate_positive(side2, 'side2') and 
                Shape.validate_positive(side3, 'side3')):
            raise ValueError('sides must be positive')
            
        a, b, c = float(side1), float(side2), float(side3)
        
        # Check if sides can form a triangle
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError('sides do not form a valid triangle')
            
        self.side1 = a
        self.side2 = b
        self.side3 = c
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class ShapeCollection:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        self.shapes.append(shape)
    
    def total_area(self):
        total = 0.0
        for shape in self.shapes:
            total += shape.area()
        return total
    
    def total_perimeter(self):
        total = 0.0
        for shape in self.shapes:
            total += shape.perimeter()
        return total
# Test your code
if __name__ == "__main__":
    # Create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    
    # Test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f" {shape.describe()}")
        print(f" Area: {shape.area():.2f}")
        print(f" Perimeter: {shape.perimeter():.2f}")
    
    # Test collection
    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")
    
    # Test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print(" Correctly rejected negative radius")