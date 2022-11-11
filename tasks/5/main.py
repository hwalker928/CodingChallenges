# Task 5 - Fruit Machine

import random

BALANCE = 100
GOES = 0
COST_PER_GO = 20

items = ["CHERRY", "BELL", "LEMON", "ORANGE", "STAR", "SKULL"]


def enterKey(message="Press enter to roll!"):
    input(message)


while True:
    print("CURRENT BALANCE: ", BALANCE)
    print(f"{COST_PER_GO} per roll\n")

    enterKey()

    BALANCE = BALANCE - COST_PER_GO
    if BALANCE < 0:
        print("\n\nYou do not have enough money to play this game!\n\n")
        BALANCE = BALANCE + COST_PER_GO
        break

    roll1 = random.choice(items)
    roll2 = random.choice(items)
    roll3 = random.choice(items)

    print(f"{roll1} {roll2} {roll3}\n")
    if roll1 == roll2 and roll2 == roll3:
        if roll1 == 5:  # 3 skulls
            print("You lost", BALANCE, "credits due to rolling 3 skulls!\n\n")
            BALANCE = 0
        elif roll1 == 1:  # 3 bells
            print("You won 500 credits due to rolling 3 bells!\n\n")
            BALANCE = BALANCE + 500
        else:  # 3 of the same, anything else
            print("You won 100 credits due to rolling 3 of the same!\n\n")
            BALANCE = BALANCE + 100
    elif roll1 == roll2 or roll1 == roll3 or roll2 == roll3:
        if roll1 == 5 and roll2 == 5 or roll1 == 5 and roll3 == 5 or roll2 == 5 and roll3 == 5:  # 2 skulls
            print("You lost 100 credits due to rolling 2 skulls!\n\n")
            BALANCE = BALANCE - 100
        else:  # 2 of the same, anything else
            print("You won 50 credits due to rolling 2 of the same!\n\n")
            BALANCE = BALANCE + 50

print("CURRENT BALANCE: ", BALANCE)
