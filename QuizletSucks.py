# Quizlet got me hooked then pulled the rug on the one good mode so here we are
# 10/25/2022

from unittest import skip
import time
import random

fileContinue = False

while True:
    returnToStart = False
    action = input("Choose a task (CF create file, EF edit file, P practice, R reset, Q quit): ")
    if fileContinue and action.upper() != "CF" and action.upper() != "EF" and action.upper() != "P" and action.upper() != "R" and action.upper() != "Q":
        print("Bad Input")
        continue
    elif action.upper() == "CF":
        fileName = input("What would you like to name your file?: ")
    elif action.upper() == "Q":
        exit()
    elif fileContinue:
        skip
    elif action.upper() == "EF" or action.upper() == "P":
        fileName = input("What file would you like to open?: ")
    elif action.upper() == "R":
        continue
    else:
        print("Bad Input")
        continue

    currentFile = f"{fileName}.txt"

    if action.upper() == "CF":
        try:
            open(currentFile, "x")
        except FileExistsError:
            while True:
                openExistingFile = input("File already exists, open it (Y yes, N no)")
                if openExistingFile.upper() == "N":
                    returnToStart = True
                    continue
                elif openExistingFile.upper() != "Y":
                    print("Bad Input")
                    continue
                break
            if returnToStart:
                continue
    fileContinue = False

    with open(currentFile, "r") as file:
        currentSet = {}
        lines = file.readlines()
        fileLength = len(lines)
        for l in lines:
            currentCard = l.split("|")
            frontSide = currentCard[0]
            backSide = currentCard[1].replace("\n", "")
            currentSet[frontSide] = backSide

    if action.upper() == "EF":
        editAction = input("Would you like to A add or R remove?: ")
        
        if editAction.upper() == "A":
            while True:
                cardExists = False
                newCardFront = input('Type the card front (& to end, R to reset): ')
                if newCardFront == "&":
                    fileContinue = True
                    break
                elif newCardFront.upper() == "R":
                    break
                for card in currentSet:
                    if newCardFront == card:
                        print("This card already exists")
                        cardExists = True
                if cardExists:
                    continue
                newCardBack = input("Type the card back: ")
                with open(currentFile, "a") as file:
                    if fileLength == 0:
                        file.write(f"{newCardFront}|{newCardBack}")
                        fileLength += 1
                    else:
                        file.write(f"\n{newCardFront}|{newCardBack}")
                        fileLength += 1
                currentSet[newCardFront] = newCardBack
                print(currentSet)

        elif editAction.upper() == "R":
            while True:
                print(currentSet)
                frontDelete = input('Which card (the front) would you like to delete? (& to end, R to reset): ')
                if frontDelete == "&":
                    fileContinue = True
                    break
                elif frontDelete.upper() == "R":
                    break
                del currentSet[frontDelete]
                with open(currentFile, 'r+') as file:
                    file.truncate(0)
                    fileLength = 0
                    for card in currentSet:
                        if fileLength == 0:
                            file.write(f"{card}|{currentSet[card]}")
                            fileLength += 1
                        else:
                            file.write(f"\n{card}|{currentSet[card]}")
                            fileLength += 1
    elif action.upper() == "P":
        practiceType = input("How would you like to practice? (FC flash cards, L learn, & to end, R to reset): ")
        if practiceType == "&":
            fileContinue = True
            break
        elif practiceType.upper() == "R":
            break
        elif practiceType.upper() == "FC":
            newPracticeSet = {}
            practiceSet = currentSet.copy()
            originalPracticeSet = practiceSet.copy()
            originalConcurrentPracticeSet = practiceSet.copy()
            practiceFronts = list(practiceSet.keys())
            practiceBacks = list(practiceSet.values())
            round = 1
            setShuffled = False
            while True:
                print(f"Round {round}")
                time.sleep(1)
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(.5)
                print("Go!")
                index = 0
                printFront = True
                while index < len(practiceFronts):
                    if printFront:
                        print(practiceFronts[index])
                    else:
                        print(practiceBacks[index])
                    flashCardsAction = input("Press enter to flip, 1 for good stack, 2 for bad stack, R to shuffle, O to set to original order: ")
                    if flashCardsAction == "2":
                        practiceSet.pop(practiceFronts[index])
                        originalPracticeSet.pop(practiceFronts[index])
                        newPracticeSet.update({practiceFronts.pop(index): practiceBacks.pop(index)})
                        printFront = True
                        continue
                    elif flashCardsAction == "1":
                        practiceSet.pop(practiceFronts[index])
                        originalPracticeSet.pop(practiceFronts[index])
                        originalConcurrentPracticeSet.pop(practiceFronts[index])
                        practiceFronts.pop(index)
                        practiceBacks.pop(index)
                        printFront = True
                        continue
                    elif flashCardsAction.upper() == "R":
                        setShuffled = True
                        random.shuffle(practiceFronts)
                        shuffledPracticeSet = dict()
                        for cardFront in practiceFronts:
                            shuffledPracticeSet.update({cardFront: practiceSet[cardFront]})
                        practiceSet = shuffledPracticeSet.copy()
                        practiceFronts = list(practiceSet.keys())
                        practiceBacks = list(practiceSet.values())
                        printFront = True
                        continue
                    elif flashCardsAction.upper() == "O":
                        setShuffled = False
                        practiceSet = originalPracticeSet.copy()
                        practiceFronts = list(practiceSet.keys())
                        practiceBacks = list(practiceSet.values())
                        printFront = True
                        continue
                    else:
                        printFront = not printFront
                        continue
                newPracticeSet = {}
                practiceSet = originalConcurrentPracticeSet.copy()
                originalPracticeSet = originalConcurrentPracticeSet.copy()
                practiceFronts = list(practiceSet.keys())
                practiceBacks = list(practiceSet.values())
                if setShuffled:
                    random.shuffle(practiceFronts)
                    shuffledPracticeSet = dict()
                    for cardFront in practiceFronts:
                        shuffledPracticeSet.update({cardFront: practiceSet[cardFront]})
                    practiceSet = shuffledPracticeSet.copy()
                    practiceFronts = list(practiceSet.keys())
                    practiceBacks = list(practiceSet.values())
                round += 1