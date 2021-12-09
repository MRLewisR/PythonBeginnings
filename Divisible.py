number = eval(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
    print(f"Your number, {number},  is divisible by 2 and 3")
if number % 2 == 0 or number % 3 == 0:
    print(f"Your number, {number}, is divisbile by 2 or 3")
if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print(f"Your number, {number}, is divisible by 2 or 3, but not both")