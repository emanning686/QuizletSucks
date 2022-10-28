# Quizlet got me hooked then pulled the rug on the one good mode so here we are
# 10/25/2022

action = input("Choose a task (CF create file, EF edit file, P practice): ")
if action.upper() == "CF":
    fileName = input("What would you like to name your file?: ")
else:
    fileName = input("What file would you like to open?: ")

currentFile = f"{fileName}.txt"

with open(currentFile, "r") as file:
    currentSet = {}
    lines = file.readlines()
    fileLength = len(lines)
    for l in lines:
        currentCard = l.split("|")
        frontSide = currentCard[0]
        backSide = currentCard[1]
        currentSet[frontSide] = backSide

if action.upper() == "EF":
    editAction = input("Would you like to A add or R remove?: ")
    if editAction.upper() == "A":
        while True:
            newCardFront = input("Type the card front (or & to end): ")
            if newCardFront == "&":
                break
            newCardBack = input("Type the card back: ")
            with open(currentFile, "a") as file:
                if fileLength == 0:
                    file.write(f"{newCardFront}|{newCardBack}")
                    fileLength += 1
                else:
                    file.write(f"{newCardFront}|{newCardBack}\n")
                    fileLength += 1
            currentSet[newCardFront] = newCardBack
            print(currentSet)