# Passing function as an argument

def disp():
    print("This is display function")


def show(x):
    return x


#print(show(disp()))

y = show(disp)
y()
