class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print(self.name, ": I am being constructed")
    def __del__(self):
        print(self.name, ": I am being destroyed")

p1 = Person("Sheldon", 23) # object creation
p2 = Person("Amy", 25)     # object creation

print(p1.name, p1.age)
print(p2.name, p2. age)

del p1 # p1 is destroyed
del p2 # p2 is destroyed
# print(p1.name, p1.age) # uncomment any try running, error occurs
                            # because p1 is already destroyed