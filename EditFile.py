# edit file menu
# created Aug 7, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call
import time
from textwrap import wrap

# define variables
sleepAmount = 0.083 / 2
# sleepAmount = 1

currentCard = 0
displayedCard = 0
currentSide = 0

textList1 = []
textList2 = []

cardSet = []
homeFileName = ""

# create card set function
def createCardSet():
    global cardSet, homeFileName

    with open("CurrentSet.txt", "r") as file:
        homeFileName = file.readline().replace("\n", "")
        for line in file:
            card = line.replace("\n", "").split("|")
            cardSet.append(card)

# save set function
def saveSet():
    global cardSet, homeFileName

    setFileLines = []
    fileLoc = f"Sets/{homeFileName}"
    with open(fileLoc, "w") as file:
        for i in cardSet:
            file.write(f"{i[0]}|{i[1]}\n")
    with open(fileLoc, "r") as file:
        for line in file:
                setFileLines.append(line)
    with open("CurrentSet.txt", "w") as file:
        file.write(f"{homeFileName}\n")
        for line in setFileLines:
            file.write(line)

# draw hud function
def drawHUD(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    text = "D  -> Delete card"
    stdscr.addstr(centerRow + 10, centerCol - 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 9, centerCol - 40, centerRow + 11, centerCol - 36)

    text = "enter  -> Edit card"
    stdscr.addstr(centerRow + 13, centerCol - 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 12, centerCol - 40, centerRow + 14, centerCol - 34)

    text = "space  -> Create new card"
    stdscr.addstr(centerRow + 10, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 9, centerCol + 17, centerRow + 11, centerCol + 23)

    text = "escape  -> Save and exit"
    stdscr.addstr(centerRow + 13, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 12, centerCol + 17, centerRow + 14, centerCol + 24)

# draw cards menu function
def drawCardsScreen(stdscr, action):
    global displayedCard, textList1, textList2, currentSide

    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    newTextList1 = []
    newTextList2 = []
    try:
        cardFront = str(cardSet[currentCard][0][:130])
        cardBack = str(cardSet[currentCard][1][:130])
        newTextList1 = wrap(cardFront, 27)
        newTextList2 = wrap(cardBack, 27)
    except IndexError:
        newTextList1 = ["", "Create new card", "", "+"]
        newTextList2 = ["", "Create new card", "", "+"]
    newCardSides = [newTextList1, newTextList2]
    cardSides = [textList1, textList2]

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    if action == "flip":
        if currentSide == 1:
            stdscr.clear()
            currentLine = -2
            for i in newCardSides[0]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[0]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[0]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            stdscr.addstr(centerRow - 2, centerCol - 15, "                              ", white)
            rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[0]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
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
            for i in newCardSides[0]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
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

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
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
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            stdscr.addstr(centerRow + 2, centerCol - 15, "                              ", white)
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 3, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 1, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
        else:
            stdscr.clear()
            currentLine = -2
            for i in newCardSides[1]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[1]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[1]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
                    currentLine += 1
            stdscr.addstr(centerRow - 2, centerCol - 15, "                              ", white)
            rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[1]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
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
            for i in newCardSides[1]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, yellow)
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

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
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
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            stdscr.addstr(centerRow + 2, centerCol - 15, "                              ", white)
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 3, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 1, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, cyan)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
    elif action == "move":
        if currentCard > displayedCard:
            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] - 3)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 3, "             ", white)

            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 12, boxBR[0], boxBR[1] - 12)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 9, "             ", white)

            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 4 + 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 4 + 15, boxBR[0], boxBR[1] - curses.COLS // 4 + 15)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 16, boxBR[0], boxBR[1] - curses.COLS // 2 + 16)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
        elif currentCard < displayedCard:
            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 16, boxBR[0], boxBR[1] - curses.COLS // 2 + 16)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 4 + 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 4 + 15, boxBR[0], boxBR[1] - curses.COLS // 4 + 15)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 11, "             ", white)

            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 12, boxBR[0], boxBR[1] - 12)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 3, "             ", white)

            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] - 3)

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

            currentLine = -2
            for i in cardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
        else:
            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardSides[currentSide]:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()

        displayedCard = int(currentCard)
        textList1 = list(newTextList1)
        textList2 = list(newTextList2)

# move card funciton
def moveCard(stdscr, direction):
    global currentCard

    if direction == "left" and currentCard > 0:
        currentCard -= 1
        drawCardsScreen(stdscr, "move")
    elif direction == "right" and currentCard < len(cardSet):
        currentCard += 1
        drawCardsScreen(stdscr, "move")

# flip card function
def flipCard(stdscr):
    global currentSide

    if currentSide == 0:
        currentSide = 1
    else:
        currentSide = 0
    drawCardsScreen(stdscr, "flip")

# draw new card function
def drawNewCard(stdscr, text, side):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    textList = wrap(text, 27)

    stdscr.clear()
    if side == "front":
        text = "Type card front"
    else:
        text = "Type card back"
    stdscr.addstr(centerRow - 6 , centerCol - len(text) // 2, text, white)
    text = "exit (escape)"
    stdscr.addstr(centerRow + 6 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 6 , centerCol + 14 - len(text) // 2, text, white)

    currentLine = -2
    for i in textList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, magenta)
            currentLine += 1

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 4, boxTL[1] - 8, boxBR[0] + 4, boxBR[1] + 8)
    stdscr.refresh()

# create new card function
def createNewCard(stdscr):
    global currentCard, displayedCard, cardSet, currentSide, textList1, textList2

    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    cardsLeft = len(cardSet) - currentCard

    if currentSide == 0:
        color = cyan
    else:
        color = yellow

    if cardsLeft != 0:
        if currentCard != len(cardSet) - 1:
            cardString = str(cardSet[currentCard][currentSide][:130])
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
                    stdscr.addstr(centerRow + currentLine, centerCol - 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] +- 3)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 12  - len(i) // 2, i, color)
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

            stdscr.clear()
            stdscr.refresh()
            time.sleep(sleepAmount)
            currentCard += 1
        
            while currentCard != len(cardSet):
                cardString = str(cardSet[currentCard][currentSide][:130])
                cardStringList = wrap(cardString, 27)

                stdscr.clear()
                currentLine = -2
                for i in cardStringList:
                    if currentLine <= 2:
                        stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 3 - 16 - len(i) // 2, i, color)
                        currentLine += 1
                rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 3 - 16, boxBR[0], boxBR[1] + curses.COLS // 3 - 16)
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

                stdscr.clear()
                currentLine = -2
                for i in cardStringList:
                    if currentLine <= 2:
                        stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 3 + 16 - len(i) // 2, i, color)
                        currentLine += 1
                rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 3 + 16, boxBR[0], boxBR[1] - curses.COLS // 3 + 16)
                drawHUD(stdscr)
                stdscr.refresh()
                time.sleep(sleepAmount)

                stdscr.clear()
                stdscr.refresh()

                currentCard += 1

            cardStringList = ["", "Create new card", "", "+"]
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
                    stdscr.addstr(centerRow + currentLine, centerCol + 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 3  - len(i) // 2, i, color)
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
        else:
            cardString = str(cardSet[currentCard][currentSide][:130])
            cardStringList = wrap(cardString, 27)
            newCardCard = ["", "Create new card", "", "+"]

            stdscr.clear()
            currentLine = -2
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 16 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 16, boxBR[0], boxBR[1] + curses.COLS // 2 - 16)

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
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 4 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 4 - 15, boxBR[0], boxBR[1] + curses.COLS // 4 - 15)

            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 3, boxBR[0], boxBR[1] - 3)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 6, boxBR[0], boxBR[1] - 6)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 3, "             ", white)

            currentLine = -2
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 12, boxBR[0], boxBR[1] + 12)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear() 
            currentLine = -2
            for i in cardStringList:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - 12  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - 12, boxBR[0], boxBR[1] - 12)
            for i in range(7):
                stdscr.addstr(centerRow + 3 - i, centerCol - 9, "             ", white)

            currentLine = -2
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 6  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 6, boxBR[0], boxBR[1] + 6)
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            currentLine = -2
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol + 3  - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + 3, boxBR[0], boxBR[1] + 3)

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
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

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
            for i in newCardCard:
                if currentLine <= 2:
                    stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()

    cardStringList = ["", "Create new card", "", "+"]

    time.sleep(sleepAmount * 4)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 1, boxTL[1], boxBR[0] + 1, boxBR[1])
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
    rectangle(stdscr, boxTL[0] - 2, boxTL[1], boxBR[0] + 2, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount * 2)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 2, boxTL[1] - 2, boxBR[0] + 2, boxBR[1] + 2)
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
    rectangle(stdscr, boxTL[0] - 2, boxTL[1] - 4, boxBR[0] + 2, boxBR[1] + 4)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount * 2)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    text = "Type card front"
    stdscr.addstr(centerRow - 6 , centerCol - len(text) // 2, text, white)
    text = "exit (escape)"
    stdscr.addstr(centerRow + 6 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 6 , centerCol + 14 - len(text) // 2, text, white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 3, boxTL[1] - 6, boxBR[0] + 3, boxBR[1] + 6)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    text = "Type card front"
    stdscr.addstr(centerRow - 6 , centerCol - len(text) // 2, text, white)
    text = "exit (escape)"
    stdscr.addstr(centerRow + 6 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 6 , centerCol + 14 - len(text) // 2, text, white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 4, boxTL[1] - 8, boxBR[0] + 4, boxBR[1] + 8)
    stdscr.refresh()
    time.sleep(sleepAmount)

    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", 
            "$", "%", "^", "&", "*", "-", "_", "=", "+", "<", ">", "~", ",", 
            " "]

    cardFront = ""
    cardBack = ""
    getCardBack = False
    while True:
        drawNewCard(stdscr, cardFront, "front")
        key = stdscr.getch()
        char = chr(key)
        if char in chars and len(cardFront) < 130:
            cardFront += char
        elif char == "\x7f" or char == "\b":
            cardFront = cardFront[:-1]
        elif char == "\n":
            if len(cardFront) != 0:
                getCardBack = True
                break
        elif key == 27:
            break

    if getCardBack:
        while True:
            drawNewCard(stdscr, cardBack, "back")
            key = stdscr.getch()
            char = chr(key)
            if char in chars and len(cardBack) < 130:
                cardBack += char
            elif char == "\x7f" or char == "\b":
                cardBack = cardBack[:-1]
            elif char == "\n":
                if len(cardBack) != 0:
                    cardSet.append(list([cardFront, cardBack]))
                    break
            elif key == 27:
                break

    stdscr.clear()
    if getCardBack == False:
        text = "Type card front"
    else:
        text = "Type card back"
    stdscr.addstr(centerRow - 6 , centerCol - len(text) // 2, text, white)
    text = "exit (escape)"
    stdscr.addstr(centerRow + 6 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 6 , centerCol + 14 - len(text) // 2, text, white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 4, boxTL[1] - 8, boxBR[0] + 4, boxBR[1] + 8)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    if getCardBack == False:
        text = "Type card front"
    else:
        text = "Type card back"
    stdscr.addstr(centerRow - 6 , centerCol - len(text) // 2, text, white)
    text = "exit (escape)"
    stdscr.addstr(centerRow + 6 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 6 , centerCol + 14 - len(text) // 2, text, white)
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 3, boxTL[1] - 6, boxBR[0] + 3, boxBR[1] + 6)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 2, boxTL[1] - 4, boxBR[0] + 2, boxBR[1] + 4)
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount * 2)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    rectangle(stdscr, boxTL[0] - 2, boxTL[1] - 2, boxBR[0] + 2, boxBR[1] + 2)
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
    rectangle(stdscr, boxTL[0] - 2, boxTL[1], boxBR[0] + 2, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount * 2)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] - 1, boxTL[1], boxBR[0] + 1, boxBR[1])
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

    currentCard = len(cardSet)
    displayedCard = int(currentCard)
    textList1 = ["", "Create new card", "", "+"]
    textList2 = ["", "Create new card", "", "+"]

# delete card function
def deleteCard(stdscr):
    global currentCard, cardSet
    cardSet.pop(currentCard)
    drawCardsScreen(stdscr, "move")

# draw edit card function
def drawEditCard(stdscr, oldText, text):
    global cardSet, currentCard, currentSide
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    textList = wrap(text, 27)

    stdscr.clear()

    stdscr.addstr(centerRow - 3, boxTL[1] + 2, "|                         |", white)
    stdscr.addstr(centerRow - 2, boxTL[1] + 2, "|                         |", white)
    stdscr.addstr(centerRow - 1, boxTL[1] + 2, "˅                         ˅", white)

    if currentSide == 0:
        text = "Type new card front"
        color = cyan
    else:
        text = "Type new card back"
        color = yellow
    stdscr.addstr(centerRow - 2 , centerCol - len(text) // 2, text, white)

    cardString = oldText
    cardStringList = wrap(cardString, 27)

    currentLine = -11
    for i in cardStringList:
        stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, magenta)
        currentLine += 1

    text = "exit (escape)"
    stdscr.addstr(centerRow + 11 , centerCol - 14 - len(text) // 2, text, white)
    text = "accept (enter)"
    stdscr.addstr(centerRow + 11 , centerCol + 14 - len(text) // 2, text, white)

    currentLine = 3
    for i in textList:
        stdscr.addstr(centerRow + currentLine, centerCol - len(i) // 2, i, magenta)
        currentLine += 1

    rectangle(stdscr, boxTL[0] + 5, boxTL[1], boxBR[0] + 5, boxBR[1])
    rectangle(stdscr, boxTL[0] - 9, boxTL[1], boxBR[0] - 9, boxBR[1])
    rectangle(stdscr, boxTL[0] - 12, boxTL[1] - 7, boxBR[0] + 8, boxBR[1] + 7)

# edit card function
def editCard(stdscr):
    global currentCard, displayedCard, cardSet, currentSide, textList1, textList2

    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)

    oldText = cardSet[currentCard][currentSide][:130]

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
            stdscr.addstr(centerRow + currentLine + 1, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0] + 1, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine + 2, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + 2, boxTL[1], boxBR[0] + 2, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine + 4, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + 4, boxTL[1], boxBR[0] + 4, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine + curses.LINES // 3 - 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + curses.LINES // 3 - 10, boxTL[1], boxBR[0] + curses.LINES // 3 - 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    currentLine = -2
    for i in cardStringList:
        if currentLine <= 2:
            stdscr.addstr(centerRow + currentLine + curses.LINES // 2 - 10, centerCol - len(i) // 2, i, color)
            currentLine += 1
    rectangle(stdscr, boxTL[0] + curses.LINES // 2 - 10, boxTL[1], boxBR[0] + curses.LINES // 2 - 10, boxBR[1])
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - curses.LINES // 2 + 10, boxTL[1] - 7, boxBR[0] - curses.LINES // 2 + 14, boxBR[1] + 7)
    stdscr.addstr(boxTL[0] - curses.LINES // 2 + 10, boxTL[1] - 7, "                                              ")
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 16, boxTL[1] - 7, boxBR[0] + 4, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 13, boxTL[1] - 7, boxBR[0] + 7, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 12, boxTL[1] - 7, boxBR[0] + 8, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    for i in range(27):
        if i % 3 == 1:
            drawEditCard(stdscr, oldText, "")
            j = 27 - i
            for k in range(j):
                stdscr.addstr(centerRow + 11 - k, boxTL[1] - 6, "                                           ")
            stdscr.refresh()
            time.sleep(sleepAmount)

    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", 
            "$", "%", "^", "&", "*", "-", "_", "=", "+", "<", ">", "~", ",",
            ".", " "]

    cardText = ""
    while True:
        drawEditCard(stdscr, oldText, cardText)
        stdscr.refresh()
        key = stdscr.getch()
        char = chr(key)
        if char in chars and len(cardText) < 130:
            cardText += char
        elif char == "\x7f" or char == "\b":
            cardText = cardText[:-1]
        elif char == "\n":
            if len(cardText) != 0:
                cardSet[currentCard][currentSide] = str(cardText)
                break
        elif key == 27:
            break

    for i in range(27):
        if i % 3 == 1:
            drawEditCard(stdscr, oldText, "")
            for j in range(i):
                stdscr.addstr(centerRow + 11 - j, boxTL[1] - 6, "                                           ")
            stdscr.refresh()
            time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 12, boxTL[1] - 7, boxBR[0] + 8, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 13, boxTL[1] - 7, boxBR[0] + 7, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - 16, boxTL[1] - 7, boxBR[0] + 4, boxBR[1] + 7)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    rectangle(stdscr, boxTL[0] - curses.LINES // 2 + 10, boxTL[1] - 7, boxBR[0] - curses.LINES // 2 + 14, boxBR[1] + 7)
    stdscr.addstr(boxTL[0] - curses.LINES // 2 + 10, boxTL[1] - 7, "                                              ")
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    stdscr.clear()
    drawHUD(stdscr)
    stdscr.refresh()
    time.sleep(sleepAmount)

    drawCardsScreen(stdscr, "move")

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
    drawCardsScreen(stdscr, "move")

    while True:
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            moveCard(stdscr, "left")
        elif key == curses.KEY_RIGHT:
            moveCard(stdscr, "right")
        elif key == curses.KEY_UP or key == curses.KEY_DOWN or key == ord("f"):
            flipCard(stdscr)
        elif key == ord(" "):
            createNewCard(stdscr)
        elif key == ord("d"):
            if currentCard < len(cardSet):
                deleteCard(stdscr) 
        elif chr(key) == "\n":
            if currentCard < len(cardSet):
                editCard(stdscr)
        elif key == 27:
            saveSet()
            break

    call(["python", "ChooseMode.py"])

wrapper(main)