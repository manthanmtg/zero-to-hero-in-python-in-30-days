fp = open("data.txt", "r") # Opening the file

lines = fp.readlines()
print(lines)
print(type(lines))

fp.close() # Closing the file