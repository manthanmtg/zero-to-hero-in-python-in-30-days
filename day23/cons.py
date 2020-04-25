class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print("Constructor called", self.name, self.age)

p1 = Person("Sheldon", 23) # object creation
p2 = Person("Amy", 25)     # object creation