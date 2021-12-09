import random

lottery = random.randint(1, 99)

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

guess = int(input("Enter a number between 1 and 99: "))
guessDigit1 = guess // 10
guessDigit2 = guess % 10

if guessDigit1 == lotteryDigit1 and guessDigit2 == lotteryDigit2:
    print("You won £10,000")
elif guessDigit1 == lotteryDigit2 and guessDigit2 == lotteryDigit1:
    print("You won £5,000")
elif guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2:
    print("You won £1,000")
elif guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2:
    print("You won £1,000")

print("The lottery number was", lottery)