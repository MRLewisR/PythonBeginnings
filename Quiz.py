import random
import time

correctCount = 0
count = 0
numberOfQuestions = 5

startTime = time.time()

while count < numberOfQuestions:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if number1 < number2:
        number1, number2 = number2, number1

    answer = eval(input(f"What is {number1} - {number2}? "))

    if answer == (number1 - number2):
        print("Correct")
        print("")
        count += 1
        correctCount += 1
    else:
        print(f"Wrong. {number1} - {number2} = {number1 - number2}")
        print("")
        count += 1

endTime = time.time()

testTime = int(endTime-startTime)

print(f"You got {correctCount} out of {numberOfQuestions} in {testTime} seconds.")