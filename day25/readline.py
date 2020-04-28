fp = open("data.txt", "r") # Opening the file

print(fp.readline()) # first line
print(fp.readline()) # second line

# Now lets check the current position being read
print(fp.tell())
fp.seek(0) # change the cursor to initial position

print(fp.readline()) # first line
print(fp.readline()) # second line
fp.close() # Closing the file