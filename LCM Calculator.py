print("LCM Calculator")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    num1, num2 = num2, num1

num1List = []
num2List = []

notFound = True

i = 1

while notFound:
    result1 = num1 * i
    num1List.append(result1)
    if result1 in num2List:
        notFound = False
        print(f"{num1} x {i} = {result1}")
        break

    result2 = num2 * i
    num2List.append(result2)
    if result2 in num1List:
        notFound = False
    else:
        print(f"{num1} x {i} = {result1}")
        print(f"{num2} x {i} = {result2}")
        i += 1

print(f"The LCM of {num1} and {num2} is {result1}")