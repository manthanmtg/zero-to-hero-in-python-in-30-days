string = "Hello Everyone"

for i in string:
    print(i, end=" ") # for every iteration, i refers to chracter of string, left to right
print()
for i in range(len(string)):
    print(string[i], end=" ")
print()
i = 0
while(i < len(string)):
    print(string[i], end=" ")
    i += 1
