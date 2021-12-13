from random import *

carryOn1 = True

while carryOn1:
    number = int(input("Enter a number: "))

    carryOn2 = True

    while carryOn2:
        if (number % 2) == 0:
            number = number / 2
            print(number)
        elif number == 1:
            break
        else:
            number = (number * 3) + 1
            print(number)