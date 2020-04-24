class Person:
    class_var = "Hello World!!!"  # this is a class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Here self.name and self.age are instance variables

obj1 = Person("Sheldon", 24)
obj2 = Person("Leonard", 26)
print(obj1.name)
print(obj2.name)
print(id(obj1.name))
print(id(obj2.name))
print(Person.class_var)
print(obj1.class_var)
print(obj2.class_var)
print(id(Person.class_var))
print(id(obj1.class_var))
print(id(obj2.class_var))
print(obj1.__class__())