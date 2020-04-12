def add(*args):
    num_sum = 0
    for i in args:
        num_sum += i
    return num_sum

print("sum:", add(2, 3, 4, 6))
