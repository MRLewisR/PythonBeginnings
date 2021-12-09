import random

number = random.randint(0, 101)

print("Guessing Game")

guess = True

while guess:
    answer = int(input("Enter a number between 0 and 100: "))
    if answer == number:
        print("Correct")
        guess = False
    elif answer > number:
        print("Guess is too high")
    elif answer < number:
        print("Guess is too low")