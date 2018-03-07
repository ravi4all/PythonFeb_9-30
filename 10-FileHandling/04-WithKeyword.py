# file = open('demo.txt')

with open('demo.txt') as file:
    data = file.read()
    print(data)