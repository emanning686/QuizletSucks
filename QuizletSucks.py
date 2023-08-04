# QuizletSucks by eric manning, a project because quizlet made the learn mode paywalled
# restarted on Aug 04, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
import time
import os

# define variables

tempFileList = os.listdir()
fileList = []
tempPage = 0
for index, file in enumerate(tempFileList):
    if file[len(file) - 3:] != "txt":
        tempFileList.pop(index)
for index, file in enumerate(tempFileList):
    tempFileList[index] = file[:-4]
for index, file in enumerate(tempFileList):
    if index % 6 == 0:
        if index > 1:
            tempPage += 1
        fileList.append([])
    fileList[tempPage].append(file)

page = 1
selected = 1

# draw level menu function
def drawLevelMenu(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 14, centerCol - 39)
    boxBR = (centerRow + 14, centerCol + 39)

    stdscr.clear()

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

    text = "Chose a file:"
    stdscr.addstr(centerRow - 11, centerCol - len(text) // 2, text, white)
    text = f"Page {page}"
    stdscr.addstr(centerRow + 7, centerCol - len(text) // 2, text, white)

    for index, file in enumerate(fileList[page - 1]):
        if index + 1 == selected:
            color = yellow
        else:
            color = cyan
        text = file[:30]
        if index == 0:
            stdscr.addstr(centerRow - 7, centerCol - 21 - len(text) // 2, text, color)
        elif index == 1:
            stdscr.addstr(centerRow - 2, centerCol - 21 - len(text) // 2, text, color)
        elif index == 2:
            stdscr.addstr(centerRow + 3, centerCol - 21 - len(text) // 2, text, color)
        elif index == 3:
            stdscr.addstr(centerRow - 7, centerCol + 21 - len(text) // 2, text, color)
        elif index == 4:
            stdscr.addstr(centerRow - 2, centerCol + 21 - len(text) // 2, text, color)
        elif index == 5:
            stdscr.addstr(centerRow + 3, centerCol + 21 - len(text) // 2, text, color)
    stdscr.refresh()
    if selected == 7:
        color = yellow
    else:
        color = cyan
    text = "Create new file"
    stdscr.addstr(centerRow + 11, centerCol - len(text) // 2, text, color)

def moveCursor(dir):
    global selected, page
    if dir == "up" and selected != 1 and selected != 4:
        if selected == 7:
            selected = 3
            if selected > len(fileList[page - 1]):
                selected = 2
            if selected > len(fileList[page - 1]):
                selected = 1   
        else:
            selected -= 1
    if dir == "down" and selected != 7:
        if selected < 3:
            selected += 1
        elif selected == 3:
            selected = 7
        else:
            selected += 1
    if dir == "left":
        if selected == 1 and page > 1:
            page -= 1
            selected = 4
            if len(fileList[page - 1]) < 4:
                selected = 1
        elif selected == 2 and page > 1:
            page -= 1
            selected = 5
            if len(fileList[page - 1]) < 5:
                selected = 4
            elif len(fileList[page - 1]) < 4:
                selected = 2
            elif len(fileList[page - 1]) < 2:
                selected = 1
        elif selected == 3 and page > 1:
            page -= 1
            selected = 6
            if len(fileList[page - 1]) < 6:
                selected = 5
            elif len(fileList[page - 1]) < 5:
                selected = 4
            elif len(fileList[page - 1]) < 4:
                selected = 3
            elif len(fileList[page - 1]) < 3:
                selected = 2
            elif len(fileList[page - 1]) < 2:
                selected = 1
        elif selected == 4:
            selected = 1
        elif selected == 5:
            selected = 2
        elif selected == 6:
            selected = 3
        elif selected == 7 and page > 1:
            page -= 1
    if dir == "right":
        if selected == 1:
            selected = 4
        elif selected == 2:
            selected = 5
        elif selected == 3:
            selected = 6
        elif selected == 4 and page < len(fileList):
            page += 1
            selected = 1
        elif selected == 5 and page < len(fileList):
            page += 1
            selected = 2
            if len(fileList[page - 1]) < 2:
                selected = 1
        elif selected == 6 and page < len(fileList):
            page += 1
            selected = 3
            if len(fileList[page - 1]) < 3:
                selected = 2
            if len(fileList[page - 1]) < 2:
                selected = 1
        elif selected == 7 and page < len(fileList):
            page += 1
    if selected > len(fileList[page - 1]):
            selected = 7

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

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    stdscr.clear()
    text = "    _,.---._                  .=-.-.                       ,----.  ,--.--------.  "
    stdscr.addstr(centerRow - 4, centerCol - len(text) // 2, text, magenta)
    text = "  ,-.' - ,  `.   .--.-. .-.-./==/_ /,--,----.  _.-.     ,-.--` , \/==/,  -   , -\ "
    stdscr.addstr(centerRow - 3, centerCol - len(text) // 2, text, magenta)
    text = " /==/ ,    -  \ /==/ -|/=/  |==|, |/==/` - ./.-,.'|    |==|-  _.-`\==\.-.  - ,-./ "
    stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, magenta)
    text = "|==| - .=.  ,  ||==| ,||=| -|==|  |`--`=/. /|==|, |    |==|   `.-. `--`\==\- \    "
    stdscr.addstr(centerRow - 1, centerCol - len(text) // 2, text, magenta)
    text = "|==|  : ;=:  - ||==|- | =/  |==|- | /==/- / |==|- |   /==/_ ,    /      \==\_ \   "
    stdscr.addstr(centerRow, centerCol - len(text) // 2, text, magenta)
    text = "|==|,  '='  ,  ||==|,  \/ - |==| ,|/==/- /-.|==|, |   |==|    .-'       |==|- |   "
    stdscr.addstr(centerRow + 1, centerCol - len(text) // 2, text, magenta)
    text = " \==\ _   -    ;|==|-   ,   /==|- /==/, `--`\==|- `-._|==|_  ,`-._      |==|, |   "
    stdscr.addstr(centerRow + 2, centerCol - len(text) // 2, text, magenta)
    text = "  '.='.  ,  ; -\/==/ , _  .'/==/. |==\-  -, /==/ - , ,/==/ ,     /      /==/ -/   "
    stdscr.addstr(centerRow + 3, centerCol - len(text) // 2, text, magenta)
    text = "    `--`--'' `--`--`..---'  `--`-` `--`.-.--`--`-----'`--`-----``       `--`--`   "
    stdscr.addstr(centerRow + 4, centerCol - len(text) // 2, text, magenta)
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()
    text = "   ,-,--.                _,.----.  ,--.-.,-.    ,-,--.  "
    stdscr.addstr(centerRow - 4, centerCol - len(text) // 2, text, magenta)
    text = " ,-.'-  _\ .--.-. .-.-..' .' -   \/==/- |\  \ ,-.'-  _\ "
    stdscr.addstr(centerRow - 3, centerCol - len(text) // 2, text, magenta)
    text = "/==/_ ,_.'/==/ -|/=/  /==/  ,  ,-'|==|_ `/_ //==/_ ,_.' "
    stdscr.addstr(centerRow - 2, centerCol - len(text) // 2, text, magenta)
    text = "\==\  \   |==| ,||=| -|==|-   |  .|==| ,   / \==\  \    "
    stdscr.addstr(centerRow - 1, centerCol - len(text) // 2, text, magenta)
    text = " \==\ -\  |==|- | =/  |==|_   `-' \==|-  .|   \==\ -\   "
    stdscr.addstr(centerRow, centerCol - len(text) // 2, text, magenta)
    text = " _\==\ ,\ |==|,  \/ - |==|   _  , |==| _ , \  _\==\ ,\  "
    stdscr.addstr(centerRow + 1, centerCol - len(text) // 2, text, magenta)
    text = "/==/\/ _ ||==|-   ,   |==\.       /==/  '\  |/==/\/ _ | "
    stdscr.addstr(centerRow + 2, centerCol - len(text) // 2, text, magenta)
    text = "\==\ - , //==/ , _  .' `-.`.___.-'\==\ /\=\.'\==\ - , / "
    stdscr.addstr(centerRow + 3, centerCol - len(text) // 2, text, magenta)
    text = " `--`---' `--`..---'               `--`       `--`---'  "
    stdscr.addstr(centerRow + 4, centerCol - len(text) // 2, text, magenta)
    stdscr.refresh()
    time.sleep(1)

    while True:
        drawLevelMenu(stdscr)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            moveCursor("up")
        elif key == curses.KEY_DOWN:
            moveCursor("down")
        elif key == curses.KEY_LEFT:
            moveCursor("left")
        elif key == curses.KEY_RIGHT:
            moveCursor("right")

wrapper(main)