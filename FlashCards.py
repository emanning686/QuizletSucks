# edit file menu
# created Aug 10, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call
import os
import time
from textwrap import wrap

# define variables
sleepAmount = 0.083 / 2
sleepAmount = 1

currentCard = 0
currentSide = 0

knowPile = 0
dontKnowPile = 0

defaultCardSet = []
cardSet = []
homeFileName = ""

# create card set function
def createCardSet():
    global defaultCardSet, cardSet, homeFileName

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

    text = "space  -> Flip card"
    stdscr.addstr(centerRow + 13, centerCol + 30 - len(text) // 2, text, white)
    rectangle(stdscr, centerRow + 12, centerCol + 19, centerRow + 14, centerCol + 27)

# draw cards screen function
def drawCardsScreen(stdscr):
    global currentCard, currentSide, cardSet

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

# draw card left function
def drawCardLeft(stdscr):

# move card function
def moveCard(stdscr, direction):
    if direction == "left":
        drawCardLeft(stdscr)

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

    while True:
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            moveCard(stdscr, "left")
        elif key == curses.KEY_RIGHT:
            moveCard(stdscr, "right")
        elif key == curses.KEY_UP or key == curses.KEY_DOWN or key == ord("f"):
            flipCard(stdscr)
        elif key == 27:
            createCardSet()
            break

    call(["python", "Practice.py"])

wrapper(main)