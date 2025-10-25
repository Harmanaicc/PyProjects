import random

choices = ("rock", "paper", "scissors")

while True:
    user = input("Enter your move (or 'quit' to exit): ").lower()

    if user == "quit":
        print("Game over, User Quitted")
        break  # exit loop

    if user not in choices:
        print("Invalid move. Please choose rock, paper, or scissors.")
        continue

    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("User Won!")
    else:
        print("Computer Won!")

    print()  # adds space between rounds
