# TODO: Create Person class with private _age
class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age # Private

    def get_age(self):
        # Return the private age
        return self._age
# TODO: Add set_age() with validation
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        # Only allow age between 0 and 150
        if 0 <= new_age <= 150:
            self._age = new_age
        else:
            print("Error: Invalid age")
