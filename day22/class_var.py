class MTGClass:
    class_var = 8456

obj1 = MTGClass()
obj2 = MTGClass()
print(MTGClass.class_var)
print(obj1.class_var)
print(obj2.class_var)
print(id(MTGClass.class_var))
print(id(obj1.class_var))
print(id(obj2.class_var))