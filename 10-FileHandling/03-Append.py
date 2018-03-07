file = open('data.txt','a')

# data = "This file is written using python script"

data = [
    {'name' : 'Ram', 'age' : 16},
    {'name' : 'Ramesh', 'age' : 17},
    {'name' : 'Raman', 'age' : 15}
]

# file.write(str(data))

for d in data:
    file.write(str(d).strip('{}') + '\n')

file.close()