class Car:
    def __init__(self, model, fuel, make):   # initialize function
        self.model = model
        self.fuel = fuel
        self.make = make
    def start(self):
        print(self.model, ": starting...")
    def brake(self):
        print(self.model, ": brake applied...")
    def accelerate(self):
        print(self.model, ": accelerating...")

car1 = Car("Renault Duster", "Diesel", 2018)  # creatinng an object of Car class
# car1 is a variable which refers to an object of Car class
car2 = Car("TATA Hector", "Petrol", 2017)     # another object of Car class
# once we define a class, we can create as many objects of that class we want
car1.start()
car1.accelerate()
car1.brake()
car2.start()
car2.accelerate()
car1.accelerate()
print(car1.make)
print(car2.model)
print(type(car1))