import random
DiceRolling = True
while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Dou You Want To Roll Again [y/n]:")
    if PlayAgain == "y":
        continue
    else:
        print("Grame over")
        break

