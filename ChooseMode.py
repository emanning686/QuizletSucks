# choose mode menu
# created Aug 5, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle

# define variables
cardSet = {}
with open("CurrentSet.txt", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            homeFileName = line
        else:
            card = line.split("|")
            cardSet[card[0]] = card[1].replace("\n", "")

page = 1
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

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

    text = "Choose an option:"
    stdscr.addstr(centerRow - 11, centerCol - len(text) // 2, text, white)

    text = f"Current file: {homeFileName}"
    stdscr.addstr(centerRow + 11, centerCol - len(text) // 2, text, white)

    for i in range(3):
        if selected - 1 == i:
            color = yellow
        else:
            color = cyan
        if i == 0:
            text = "Practice"
            stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, color)
        elif i == 1:
            text = "Edit File"
            stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, color)
        elif i == 2:
            text = "Delete File"
            stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, color)

    text = "exit (esc)"
    stdscr.addstr(centerRow + 4, centerCol - 10 - len(text) // 2, text, white)
    
    stdscr.refresh()


def main(stdscr):
    while True:
        drawOptionsMenu(stdscr)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            moveCursor("up", stdscr)
        elif key == curses.KEY_DOWN:
            moveCursor("down", stdscr)
        elif key == ord(" "):
            selectItem(stdscr)
        elif key == 27:
            exit()

wrapper(main)