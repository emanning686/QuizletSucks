import curses
from curses import wrapper
from curses.textpad import rectangle

def main(stdscr):
    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 4, centerCol - 15)
    boxBR = (centerRow + 4, centerCol + 15)
    
    stdscr.clear()

    rectangle(stdscr, boxTL[0] + 7, boxTL[1], boxBR[0], boxBR[1])

    stdscr.refresh()
    stdscr.getch()

wrapper(main)