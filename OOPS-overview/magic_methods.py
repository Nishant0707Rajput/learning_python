class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, age= {self.age}"

    def __repr__(self):
        return f"<(Person = {self.name}, age = {self.age})>"


a_person = Person("Bob", 22)
print(Person)
print(a_person)                         #  magic methods are called automatically on the class
print(a_person.__repr__())              #  same as __str__ but more priority to __str__