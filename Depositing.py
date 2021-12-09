password = str(input("Create a password: "))

depositLimit = 200

depositAmount = int(input("Enter a deposit amount: "))

if depositAmount > depositLimit:
    print("You are unable to deposit that amount of money")
else:
    password1 = str(input("Enter your password: "))
    if password1 == password:
        print("Money has been deposited")
    else:
        print("Incorrect password, money has not been deposited")