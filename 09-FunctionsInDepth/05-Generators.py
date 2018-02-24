# Generators - Yield

def calc():
    x = 10
    y = 13
    yield x + y
    x = 13
    y = 15
    yield x - y
    x = 15
    y = 17
    yield x * y

#print(calc())
for result in calc():
    print(result)
