carryOn = True

while carryOn:
    year = int(input("Enter a year: "))

    if (year % 4) == 0 or (year % 400) == 0:
        if year % 100 == 0:
            print(year, "is not a leap year \n")
        else:
            print(year, "is a leap year \n")

    else:
        print(year, "is not a leap year \n")