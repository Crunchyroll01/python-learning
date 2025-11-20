
# TODO: Create Car with make, model, year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
# Test:
# my_car = Car("Toyota", "Camry", 2020)
# print(f"{my_car.year} {my_car.make} {my_car.model}")`
# TODO: Add mileage and drive() method
class Car:
    def __init__(self, make, model, year):
        # Your code here
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        # Add miles to mileage
        self.mileage += miles
        # Print total mileage
        print(f"Total mileage: {self.mileage} miles")
        
class Book:
    def __init__(self, title):
        self.title = title
        print(f"Book '{self.title}' opened!")
    def __del__(self):
        print(f"Book '{self.title}' closed!")
my_book = Book("Python Fun")
print(my_book.title)
del my_book
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal Added: {self.name}")
    def __del__(self):
        print(f"Animal Released: {self.name}")
class Zoo:
    def __init__(self):
        self.animals = []
    def add(self, animal):
        self.animals.append(animal)
zoo = Zoo()
zoo.add(Animal("Lion"))
zoo.add(Animal("Monkey"))
print([a.name for a in zoo.animals])
del zoo