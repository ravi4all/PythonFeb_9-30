def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y if x > y else y - x
    print("Difference is",z)

def mul(x,y):
    z = x * y
    print("Multiplication is",z)

def div(x,y):
    z = x / y
    print("Divison is",z)

add(13,15)
sub(15,12)
div(23,2)
mul(12,12)
