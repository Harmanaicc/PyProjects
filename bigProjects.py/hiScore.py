import random

def game():

    print("Your are playing  a game...")

    score = random.randint(1,62) 
    
    with open("Hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is: {score}")
    if(score > hiscore):
        with open("Hiscore.txt", "w") as f:
            f.write(str(score))

    print()
    return score

game()