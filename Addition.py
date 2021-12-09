import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input(f"What is {number1} + {number2}? "))

print(f"{number1} + {number2} = {number1 + number2}")