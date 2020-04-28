fp = open("data.txt", "r") # Opening the file

contents = fp.read()
print(contents)
print("-----------")
print(repr(contents)) # print representation

fp.close() # Closing the file