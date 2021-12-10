
print("############################################################################################ \n")

print("Enter number first")
print("Then enter the operator")
print("Then enter the second number")
print("Repeat \n")

print("############################################################################################ \n")

number1 = float(input("Enter a number: "))

repeat = True

while repeat:
    def add(num):
        number2 = float(input("Enter a number: "))
        global number1
        number1 = num + number2
        print(number1)
    
    def subtract(num):
        number2 = float(input("Enter a number: "))
        global number1
        number1 = num - number2
        print(number1)
    
    def multiply(num):
        number2 = float(input("Enter a number: "))
        global number1
        number1 = num * number2
        print(number1)
    
    def divide(num):
        number2 = float(input("Enter a number: "))
        global number1
        number1 = num / number2
        print(number1)

    operator = str(input("Enter your operator: "))

    if operator == "+":
        add(number1)
    
    elif operator == "-":
        subtract(number1)
    
    elif operator == "*":
        multiply(number1)
    
    elif operator == "/":
        divide(number1)

    else:
        print("ERROR \n")
        exit()
