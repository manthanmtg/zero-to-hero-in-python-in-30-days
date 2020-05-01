fp = open("data.txt") # default mode is "r"

data = dict()  # creating a dictionary
for line in fp:
    name, email = line.split()
    data[name] = email
print(data)

fp.close()