class MTGClass:
    def instance_method(self):
        print("self:", self)
        print("This is a instance method")
    @classmethod
    def class_method(cls):
        print("cls:", cls)
        print("This is a class method")

obj1 = MTGClass()
obj2 = MTGClass()
MTGClass.class_method()
obj1.class_method()
obj2.class_method()