fp = open("out2.txt", "w") # opening the file

lines_list = ["First Line\n", "Second Line\n", "Third Line"]
fp.writelines(lines_list)

fp.close()