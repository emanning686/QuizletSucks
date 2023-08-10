# choose mode menu
# created Aug 5, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
from subprocess import call
import os

# define variables
cardSet = {}
with open("CurrentSet.txt", "r") as file:
    homeFileName = file.readline().replace("\n", "")

selected = 1

def drawOptionsMenu(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 14, centerCol - 38)
    boxBR = (centerRow + 14, centerCol + 38)

    stdscr.clear()

    text = "Choose an option:"
    stdscr.addstr(centerRow - 11, centerCol - len(text) // 2, text, white)

    text = f"Current file: {homeFileName}"
    stdscr.addstr(centerRow + 7, centerCol - len(text) // 2, text, white)

    text = "exit (esc)"
    stdscr.addstr(centerRow + 12, centerCol - 30 - len(text) // 2, text, white)

    text = "accept (enter)"
    stdscr.addstr(centerRow + 12, centerCol + 30 - len(text) // 2, text, white)

    for i in range(3):
        if i + 1 == selected:
            color = yellow
        else:
            color = cyan
        if i == 0:
            text = "Practice"
            stdscr.addstr(centerRow - 7, centerCol - len(text) // 2, text, color)
        elif i == 1:
            text = "Edit File"
            stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, color)
        elif i == 2:
            text = "Delete File"
            stdscr.addstr(centerRow + 3, centerCol - len(text) // 2, text, color)

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])
    
    stdscr.refresh()

# move cursor function
def moveCursor(dir):
    global selected, page
    if dir == "up" and selected != 1:
        selected -= 1
    elif dir == "down" and selected != 3:
        selected += 1

# select item function
def selectItem():
    if selected == 3:
        os.remove(f"Sets/{homeFileName}")
        file = open("CurrentSet.txt", "w")
        file.close()

# main function
def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    exitFile = False

    while True:
        drawOptionsMenu(stdscr)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            moveCursor("up")
        elif key == curses.KEY_DOWN:
            moveCursor("down")
        elif chr(key) == "\n":
            selectItem()
            break
        elif key == 27:
            exitFile = True
            break

    if selected == 1 and not exitFile:
        call(["python", "Practice.py"])
    elif selected == 2 and not exitFile:
        call(["python", "EditFile.py"])
    elif selected == 3 or exitFile:
        call(["python", "QuizletSucks.py"])

wrapper(main)