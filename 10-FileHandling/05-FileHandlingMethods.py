file = open('data.txt')

# data = file.readlines()

# data = file.readline()

# data = file.read(-1)
file.seek(15)

# data = file.tell()
# data = file.read()

# data = file.write("This is inserted text...")

data = file.read(25)

print(data)

file.close()