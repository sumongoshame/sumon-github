# Hangman game

word = "sumon"
chances = 5
GuessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end = " ")
        else:
            print("_", end ="")

    myguess = input(f"your changes is {chances}, Guess the letter: ")
    GuessAdd.append(myguess.lower())
    if myguess.lower() not in word.lower():     #ai line condination r nisar line ta statement
        chances -= 1
        if chances == 0:
            break

        done = True
        for letter in word:
            if letter.lower() not in GuessAdd:
                done = False
if done:    #condition
    print(F"yes, you have won the game, the word is {word} ")   # statement
else:
    print("you game is over")