# BaseException
# ZeroDivisionError AssertionError ValueError

def calc():
    try:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        add = num_1 + num_2
        sub = num_1 - num_2
        div = num_1 / num_2
        mul = num_1 * num_2

    except ZeroDivisionError:
        print("Cannot divide by zero")
        calc()

    except ValueError:
        print("Try Again")
        calc()

    else:
        print("Result is :", add, sub, div, mul)

# print("This is outside except Block...")
calc()