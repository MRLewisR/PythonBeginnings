import random

guess = False

while guess == False:
    number1 = random.randint(0, 99)
    number2 = random.randint(0, 99)

    if number1 < number2:
        number1, number2 = number2, number1
    
    print(f"What is {number1} - {number2}?")
    answer = int(input())

    if answer == (number1 - number2):
        print("You are correct")
        print("")
        guess = True
    else:
        print("Incorrect")
        print("")