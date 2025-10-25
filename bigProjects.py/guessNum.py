import random

target = random.randint(1,100)


while True:
    userGuess = input("Guess the number or Quit(Q): ")
    if (userGuess == "Q"):
        print("Quitted")
        break
    userGuess = int(userGuess)
    if (userGuess == target):
        print("Correct Guess!!")
        break
    elif userGuess > target:
        print("Your guess is too big. Try guessing smaller number")
    else:
        print("Your guess is too small. Try guessing bigger number")


print("----GAME OVER----")