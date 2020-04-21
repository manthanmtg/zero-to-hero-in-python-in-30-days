a = int(input())
b = int(input())
print("Before swapping: a:", a, "b: ", b)
a, b = b, a
# a, b = (b, a)
# (a, b) = (b, a)
print("After swapping: a:", a, "b: ", b)