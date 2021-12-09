def greet(firstName, secondName):
    print(f"Hello {firstName} {secondName}")

greet("Steve", "Smith")

print("")

def greet2(name, greeting="Hello"):
    return f"{greeting} {name}"

greetingForMe = greet2("Billy", greeting="Hi")
print(greetingForMe)

print("")

def addCalc(num1, num2):
    answer = num1 + num2
    return answer

addedNum = addCalc(2, 3)
print(addedNum)