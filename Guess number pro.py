secret_number = 5
gruss_number = 1
limit_number = 3
while gruss_number < limit_number:
    user_gruss_number = int(input("How to gress number: "))
    gruss_number += 1
    if user_gruss_number == secret_number:
        print("you are win the game...")
        break

else:
    print("loss the game")