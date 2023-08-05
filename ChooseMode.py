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
    text = f"Page"
    stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, white)
    text = f"Page"
    stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, white)
    
    stdscr.refresh()


def main(stdscr):
    drawOptionsMenu(stdscr)
    stdscr.getch()

wrapper(main)