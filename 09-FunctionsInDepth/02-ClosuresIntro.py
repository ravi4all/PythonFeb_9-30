# Closures

def outer():
    x = "Hello"

    def inner_1():
        return x + " world"

    def inner_2():
        return x + " python"

    #print(inner_1())
    #print(inner_2())

    #inner_1()
    #inner_2()

    return inner_1, inner_2

#func_1 = outer()
#print(func_1)
#print(type(func_1))
#print(func_1())

func_1, func_2 = outer()
print(func_1())
