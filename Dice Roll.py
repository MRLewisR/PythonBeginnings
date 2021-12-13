import random

carryOn = True

while carryOn:
    diceValue = int(input("How many numbers do you want your die to have? "))
    
    print("Roll Result:", random.randint(1, diceValue), "\n")

    repeat = str(input("Roll Again? (Y/N) ").upper())

    print("\n")

    if repeat == "Y":
        carryOn = True
    elif repeat == "N":
        carryOn = False
    else:
        print("ERROR \n")
        break