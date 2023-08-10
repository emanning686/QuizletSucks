# edit file menu
# created Aug 10, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call

# define variables
cardSet = []
homeFileName = ""

# flash cards function
def createCardSet(stdscr):
    global cardSet, homeFileName

    currentSet = []

    with open("CurrentCards.txt", "r") as file:
        firstLine = file.readline().replace("\n", "")

    if firstLine != "pulled":
        with open("CurrentSet.txt", "r") as file:
            for line in file:
                currentSet.append(line)
        with open("CurrentCards.txt", "w") as file:
            file.write("pulled\n")
            for line in currentSet:
                file.write(line)
    
    with open("CurrentCards.txt", "r") as file:
        pulled = file.readline().replace("\n", "")
        for line in file:
            card = line.replace("\n", "").split("|")
            cardSet.append(card)

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
        elif key == 27:
            createCardSet()
            break

    call(["python", "ChooseMode.py"])

wrapper(main)