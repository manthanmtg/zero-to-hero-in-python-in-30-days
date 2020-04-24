class MTGClass:
    class_var = "Hello World!!!"
    def instance_method(self):
        print("self:", self)
        print("This is a instance method")
    @classmethod
    def class_method(cls):
        print("cls:", cls)
        print("This is a class method")
    @staticmethod
    def static_method():
        print("This is a static method")

obj1 = MTGClass()
obj2 = MTGClass()
MTGClass.static_method()
obj1.static_method()
obj2.static_method()
