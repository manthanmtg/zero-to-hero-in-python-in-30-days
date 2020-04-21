def get_mid_three(string):
    mid_index = int(len(string) / 2)
    return string[mid_index-1:mid_index+2]
print(get_mid_three("JohnDipPeta"))