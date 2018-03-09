def atm():
    total_bal = 10000
    withdrawAmount = int(input("Enter amount you want to withdraw : "))

    try:
        if withdrawAmount > total_bal:
            raise ValueError("Not sufficient balance")
        else:
            print("Withdraw successfull")
    except ValueError as err:
        print(err)

atm()