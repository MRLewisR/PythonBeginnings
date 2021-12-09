import random

number = random.randint(0, 100)

guess = -1

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Guess is too high")
    elif guess < number:
        print("Guess is too low")
    elif guess == number:
        print("Correct guess")
