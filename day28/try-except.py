print("Line 1")
lis = [1, 2, 3]
try:
    print(lis[5])
except Exception as e:
    print("Exception occured:", e)
print("Line 3")