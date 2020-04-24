class MTGClass:
    def instance_method(self):
        print("self:", self)
        print("This is a instance method")

obj1 = MTGClass()
obj1.instance_method() # can also be called like: MTGClass.instance_method(obj1)
MTGClass.instance_method(obj1) # obj1 is passed which is referred to as self in method