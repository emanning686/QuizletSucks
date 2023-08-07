# edit file menu
# created aug 7, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call
import time
from textwrap import wrap

# define variables

sleepAmount = 0.083
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
    stdscr.addstr(centerRow + 13, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 12, centerCol + 17, centerRow + 14, centerCol + 23)

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
        newTextList1 = wrap(cardFront, 28)
        newTextList2 = wrap(cardBack, 28)
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
            rectangle(stdscr, boxTL[0] + 7, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 6, boxTL[1], boxBR[0] - 1, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 5, boxTL[1], boxBR[0] - 2, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0] - 4, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0] - 6, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 7, boxBR[1])
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
            rectangle(stdscr, boxTL[0] + 7, boxTL[1], boxBR[0], boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 6, boxTL[1], boxBR[0] - 1, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 5, boxTL[1], boxBR[0] - 2, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 3, boxTL[1], boxBR[0] - 4, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0] + 1, boxTL[1], boxBR[0] - 6, boxBR[1])
            drawHUD(stdscr)
            stdscr.refresh()
            time.sleep(sleepAmount)

            stdscr.clear()
            rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0] - 7, boxBR[1])
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
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 15, boxBR[0], boxBR[1] + curses.COLS // 2 - 15)

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
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 15, boxBR[0], boxBR[1] - curses.COLS // 2 + 15)
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
                    stdscr.addstr(centerRow + currentLine, centerCol - curses.COLS // 2 + 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] - curses.COLS // 2 + 15, boxBR[0], boxBR[1] - curses.COLS // 2 + 15)

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
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 15, boxBR[0], boxBR[1] + curses.COLS // 2 - 15)
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
                    stdscr.addstr(centerRow + currentLine, centerCol + curses.COLS // 2 - 15 - len(i) // 2, i, color)
                    currentLine += 1
            rectangle(stdscr, boxTL[0], boxTL[1] + curses.COLS // 2 - 15, boxBR[0], boxBR[1] + curses.COLS // 2 - 15)
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
def moveCard(stdscr, dir):
    global currentCard
    if dir == "left" and currentCard > 0:
        currentCard -= 1
        drawCardsScreen(stdscr, "move")
    elif dir == "right" and currentCard < len(cardSet):
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

# create new card function
def createNewCard(stdscr):
    cardsLeft = len(cardSet) - 1 - currentCard

    if cardsLeft != 0:
    

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
        elif key == curses.KEY_UP or key == ord("f"):
            flipCard(stdscr)
        elif chr(key) == "\n":
            createNewCard(stdscr)
        elif key == 27:
            exit()

wrapper(main)