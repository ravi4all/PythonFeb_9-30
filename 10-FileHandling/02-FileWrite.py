file = open('demo_1.txt','w')

# data = "This file is written using python script"

data = [
    {'name' : 'Ram', 'age' : 16},
    {'name' : 'Ramesh', 'age' : 17},
    {'name' : 'Raman', 'age' : 15}
]

file.write(str(data))

file.close()