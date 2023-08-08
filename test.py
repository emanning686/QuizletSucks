import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    white = curses.color_pair(1)   

    lines = curses.LINES
    cols = curses.COLS

    stdscr.clear()
    
    stdscr.addstr(1, 1, str(lines), white)
    stdscr.addstr(2, 1, str(cols), white)

    stdscr.refresh()
    stdscr.getch()

wrapper(main)