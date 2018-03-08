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
        print("Result is :",add,sub,div,mul)

    # except BaseException as err:
        # print("Some Exception...")
        # print("Exception is :",err)

    except ZeroDivisionError:
        print("Cannot divide by zero")
        calc()

    except ValueError:
        print("Try Again")
        calc()

# print("This is outside except Block...")
calc()