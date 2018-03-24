def withdraw():
    total_bal = 10000
    amount = int(input("Enter the amount you want to withdraw : "))
    if amount > total_bal:
        print("Insufficient balance")
    else:
        total_bal = total_bal - amount
        print("Remaining Balance is",total_bal)

def bal_enquiry():
    pass

# withdraw()

print("""
1. Withdraw
2. Balance Enquiry
3. PIN Change
4. Exit
""")
user_choice = input("Enter your choice : ")
if user_choice == "1":
    withdraw()
elif user_choice == "2":
    bal_enquiry()
else:
    print("Wrong Choice...")