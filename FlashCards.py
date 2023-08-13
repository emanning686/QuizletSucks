# edit file menu
# created Aug 10, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call
import os
import time
from textwrap import wrap
import time

# define variables
sleepAmount = 0.083 / 2
# sleepAmount = 1

currentCard = 0
currentSide = 0

knowPile = []
dontKnowPile = []

defaultCardSet = []
cardSet = []
homeFileName = ""
fcHomeFileName = ""

initTime = 0

exitToMenu = False

# start time function
def startTime():
    global initTime

    initTime = time.time()

# create card set function
def createCardSet():
    global defaultCardSet, cardSet, homeFileName, fcHomeFileName

    fileList = os.listdir("Sets/")

    with open("CurrentSet.txt", "r") as file:
        homeFileName = file.readline().replace("\n", "")
        for line in file:
            card = line.replace("\n", "").split("|")
            defaultCardSet.append(card)

    fcExists = False
    fcHomeFileName = homeFileName.replace(".txt", ".fc.txt")
    for i in fileList:
        if i == fcHomeFileName:
            fcExists = True

    if not fcExists:
        with open(f"Sets/{fcHomeFileName}", "w") as file:
            for line in defaultCardSet:
                file.write(f"{line[0]}|{line[1]}\n")
        cardSet = list(defaultCardSet)
    else:
        with open (f"Sets/{fcHomeFileName}", "r") as file:
            for line in file:
                card = line.replace("\n", "").split("|")
                cardSet.append(card)
        if len(cardSet) == 0:
            cardSet = list(defaultCardSet)

# save card set function
def saveCardSet():
    with open(f"Sets/{fcHomeFileName}", "w") as file:
            for index, card in enumerate(cardSet):
                if index not in knowPile:
                    file.write(f"{cardSet[index][0]}|{cardSet[index][1]}\n")

# draw hud function
def drawHUD(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    text = "<  -> Dont know pile"
    stdscr.addstr(centerRow + 10, centerCol - 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 9, centerCol - 42, centerRow + 11, centerCol - 38)

    text = ">  -> Know pile"
    stdscr.addstr(centerRow + 10, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 9, centerCol + 21, centerRow + 11, centerCol + 25)

    text = f"Dont know pile : {len(dontKnowPile)}"
    stdscr.addstr(centerRow - 10, centerCol - 30 - len(text) // 2, text, white)

    text = f"Know Pile : {len(knowPile)}"
    stdscr.addstr(centerRow - 10, centerCol + 30 - len(text) // 2, text, white) 

    text = "space  -> Flip card"
    stdscr.addstr(centerRow + 13, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 12, centerCol + 19, centerRow + 14, centerCol + 27)

# draw cards screen function
def drawCardsScreen(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    cardString = cardSet[currentCard][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - curses.LINES // 2 + 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - curses.LINES // 2 + 10, boxTL[1], boxBR[0] - curses.LINES // 2 + 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - curses.LINES // 3 + 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - curses.LINES // 3 + 10, boxTL[1], boxBR[0] - curses.LINES // 3 + 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 4, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 4, boxTL[1], boxBR[0] - 4, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 2, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 2, boxTL[1], boxBR[0] - 2, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 1, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 1, boxTL[1], boxBR[0] - 1, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

# draw done screen function
def drawDoneScreen(stdscr):
    global cardSet, homeFileName, knowPile, dontKnowPile, exitToMenu, currentCard, currentSide

    finalTime = round(time.time() - initTime, 2)

    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    stdscr.clear()

    if len(dontKnowPile) == 0:
        text = wrap(f"You completed this round of {homeFileName[:-4]} in {finalTime} seconds! And you finished the set!", 15)
        for index, i in enumerate(text):
            stdscr.addstr(centerRow - 5 + index, centerCol - len(i) // 2, i, yellow)

        text = "Enter to restart, escape to go back to menu"
        stdscr.addstr(centerRow + 2, centerCol - len(text) // 2, text, magenta)

        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if chr(key) == "\n":
                knowPile = []
                dontKnowPile = []
                currentCard = 0
                currentSide = 0
                cardSet = list(defaultCardSet)
                drawCardsScreen(stdscr)
                startTime()
                break
            elif key == 27:
                file = open(f"Sets/{fcHomeFileName}", "w")
                file.close()
                exitToMenu = True
                break
    else:
        text = wrap(f"You completed this round of {homeFileName[:-4]} in {finalTime} seconds! You have {len(dontKnowPile)} left to learn!", 15)
        for index, i in enumerate(text):
            stdscr.addstr(centerRow - 5 + index, centerCol - len(i) // 2, i, yellow)

        text = "Enter to continue to next round, escape to go back to menu"
        stdscr.addstr(centerRow + 2, centerCol - len(text) // 2, text, magenta)

        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if chr(key) == "\n":
                setList = list(cardSet)
                cardSet = []
                for index, i in enumerate(setList):
                    if index in dontKnowPile:
                        cardSet.append(i)
                knowPile = []
                dontKnowPile = []
                currentCard = 0
                currentSide = 0
                drawCardsScreen(stdscr)
                startTime()
                break
            elif key == 27:
                saveCardSet()
                exitToMenu = True
                break

# draw card left function
def drawCardLeft(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    cardString = cardSet[currentCard][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - 3 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] - 3)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear() 
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - 6 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear() 
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - 12 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] - 12, boxBR[0], boxBR[1] - 12)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 4 + 15 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 4 + 15, boxBR[0], boxBR[1] - curses.COLS // 4 + 15)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 16 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 16, boxBR[0], boxBR[1] - curses.COLS // 2 + 16)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

# draw card right function
def drawCardRight(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    cardString = cardSet[currentCard][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol + 3 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear() 
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol + 6 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear() 
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol + 12 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

# move card function
def moveCard(stdscr, direction):
    global dontKnowPile, knowPile, currentCard, currentSide

    if direction == "left":
        dontKnowPile.append(currentCard)
        drawCardLeft(stdscr)
    elif direction == "right":
        knowPile.append(currentCard)
        drawCardRight(stdscr)

    currentSide = 0
    currentCard += 1
    if currentCard < len(cardSet):
        drawCardsScreen(stdscr)
    else:
        drawDoneScreen(stdscr)

# draw undo card function
def drawUndoCard(stdscr, pile):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    cardString = cardSet[currentCard + 1][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 1, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 1, boxTL[1], boxBR[0] - 1, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 2, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 2, boxTL[1], boxBR[0] - 2, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - 4, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 4, boxTL[1], boxBR[0] - 4, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - curses.LINES // 3 + 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - curses.LINES // 3 + 10, boxTL[1], boxBR[0] - curses.LINES // 3 + 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)


    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine - curses.LINES // 2 + 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - curses.LINES // 2 + 10, boxTL[1], boxBR[0] - curses.LINES // 2 + 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    cardString = cardSet[currentCard][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if pile == "know":
        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear() 
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol + 12 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear() 
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol + 6 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol + 3 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

    elif pile == "dontKnow":
        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 16 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 16, boxBR[0], boxBR[1] - curses.COLS // 2 + 16)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 4 + 15 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 4 + 15, boxBR[0], boxBR[1] - curses.COLS // 4 + 15)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear() 
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - 12 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] - 12, boxBR[0], boxBR[1] - 12)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear() 
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - 6 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - 3 - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] - 3)
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

        stdscr.clear()
        currentLine = -2
        for i in cardStringList:
            if currentLine <= 2:
                stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                currentLine += 1
        rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
        drawHUD(stdscr)
        stdscr.refresh()
        time.sleep(sleepAmount)

# undo card function
def undoCard(stdscr):
    global currentCard
    if currentCard != 0:
        currentCard -= 1

        for i in knowPile:
            if i == currentCard:
                knowPile.pop()
                drawUndoCard(stdscr, "know")
        for i in dontKnowPile:
            if i == currentCard:
                dontKnowPile.pop()
                drawUndoCard(stdscr, "dontKnow")

# draw flip card function
def drawFlipCard(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    if currentSide == 0:
        color = yellow
        cardString = cardSet[currentCard][1][:130]
    else:
        color = cyan
        cardString = cardSet[currentCard][0][:130]

    cardStringList = wrap(cardString, 27)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    stdscr.addstr(centerRow - 2, centerCol - 15, "                              ", white)
    rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    stdscr.addstr(centerRow - 2, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow - 1, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow, centerCol - 15, "                              ", white)
    rectangle(stdscr, boxTL[0] + 5, boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    stdscr.addstr(centerRow - 2, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow - 1, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow + 1, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow + 2, centerCol - 15, "                              ", white)
    rectangle(stdscr, boxTL[0] + 6, boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] + 5, boxTL[1], boxBR[0] - 1, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0] - 3, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0] - 5, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    cardString = cardSet[currentCard][currentSide][:130]
    cardStringList = wrap(cardString, 27)

    if currentSide == 0:
        color = cyan
        
    else:
        color = yellow

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    stdscr.addstr(centerRow + 2, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow + 1, centerCol - 15, "                              ", white)
    stdscr.addstr(centerRow, centerCol - 15, "                              ", white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 5, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    stdscr.addstr(centerRow + 2, centerCol - 15, "                              ", white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 3, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 1, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()

# flip card function
def flipCard(stdscr):
    global currentSide

    if currentSide == 0:
        currentSide = 1
    else:
        currentSide = 0

    drawFlipCard(stdscr)

# main function
def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    createCardSet()
    drawCardsScreen(stdscr)
    startTime()

    while True:
        if exitToMenu == False:
            key = stdscr.getch()
            if key == curses.KEY_LEFT:
                moveCard(stdscr, "left")
            elif key == curses.KEY_RIGHT:
                moveCard(stdscr, "right")
            elif key == curses.KEY_UP or key == curses.KEY_DOWN or key == ord(" "):
                flipCard(stdscr)
            elif key == ord("u"):
                undoCard(stdscr)
            elif key == 27:
                saveCardSet()
                break
        else:
            break

    call(["python", "Practice.py"])

wrapper(main)