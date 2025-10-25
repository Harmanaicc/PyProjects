import random

def game():

    print("Your are playing  a game...")

    score = random.randint(1,62) 
    
    with open(r"C:\Users\harman\Documents\PyProjects\PyProjects\bigProjects.py\hiscore.txt") as f:

        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is: {score}")
    if(score > hiscore):
        with open(r"C:\Users\harman\Documents\PyProjects\PyProjects\bigProjects.py\hiscore.txt", "w") as f:

            f.write(str(score))

    print()
    return score

game()