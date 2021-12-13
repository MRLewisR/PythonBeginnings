import random

rpsList = ["Rock", "Paper", "Scissors"]

cpuScore = 0

userScore = 0

carryOn = True

while carryOn:
    rpsCpu = random.choice(rpsList)
    rpsChoice = str(input("Choose: Rock (R), Paper(P), or Scissors (S) ")).upper()
    if rpsChoice == "R":
        if rpsCpu == rpsList[0]:
            print("Computer Chose Rock!")
            print("Draw! \n")
            print("Computer:", cpuScore)
            print(f"You: {userScore} \n")
        elif rpsCpu == rpsList[1]:
            print("Computer Chose Paper!")
            print("You Lost! \n")
            cpuScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
        elif rpsCpu == rpsList[2]:
            print("Computer Chose Scissors!")
            print("You Win! \n")
            userScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")

    elif rpsChoice == "P":
        if rpsCpu == rpsList[0]:
            print("Computer Chose Rock!")
            print("You Win! \n")
            userScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
        elif rpsCpu == rpsList[1]:
            print("Computer Chose Paper!")
            print("Draw! \n")
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
        elif rpsCpu == rpsList[2]:
            print("Computer Chose Scissors!")
            print("You Lose! \n")
            cpuScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")

    elif rpsChoice == "S":
        if rpsCpu == rpsList[0]:
            print("Computer Chose Rock!")
            print("You Lose! \n")
            cpuScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
        elif rpsCpu == rpsList[1]:
            print("Computer Chose Paper!")
            print("You Win! \n")
            userScore += 1
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
        elif rpsCpu == rpsList[2]:
            print("Computer Chose Scissors!")
            print("Draw! \n")
            print("Computer:", cpuScore)
            print(f"You {userScore} \n")
    else:
        print("\nERROR \n")
        exit()