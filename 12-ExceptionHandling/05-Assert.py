def atm():
    total_bal = 10000
    withdrawAmount = int(input("Enter amount you want to withdraw : "))

    try:
        assert (withdrawAmount < total_bal), "Not sufficient balance"
        print("Withdraw successfull")
    except AssertionError as err:
        print(err)

atm()