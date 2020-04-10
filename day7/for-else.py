for i in range(1, 5):
    print(i)
else:
    print("Loop exited normally")
for i in range(5, 9):
    print(i)
    if(i == 7):
        break
else:
    print("Loop exited normally")