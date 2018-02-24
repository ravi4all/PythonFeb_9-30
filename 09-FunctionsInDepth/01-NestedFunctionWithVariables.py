x = "Hello"
def outer():
    y = "Bye"

    def inner():
        z = "hey"
        print("Inside Inner value of x,y,z",x,y,z)

    print("Inside Outer value of x,y",x,y)
    inner()

outer()
