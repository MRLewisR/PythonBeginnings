import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

if number1 < number2:
    number1, number2 = number2, number1

guess = False

while guess == False:
    answer = int(input(f"What is {number1} - {number2}? "))
    if answer == (number1 - number2):
        print("Correct")
        print("")
        guess = True
    else:
        print("Incorrect, try again")
        print("")