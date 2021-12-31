print("LCM Calculator")

def coloured(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

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
        print("")
        print(coloured(255, 0, 0, f"{num1} x {i} = {result1}"))
        break

    result2 = num2 * i
    num2List.append(result2)
    if result2 in num1List:
        notFound = False
    else:
        print(f"{num1} x {i} = {result1}")
        print(f"{num2} x {i} = {result2}")
        i += 1

result2 == result1
place = int(result1/num2)
print(coloured(255, 0, 0, f"{num2} x {place} = {result1} \n"))

print(f"The LCM of {num1} and {num2} is {result1}")