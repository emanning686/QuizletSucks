# QuizletSucks by eric manning, a project because quizlet made the learn mode paywalled
# restarted on Aug 04, 2023

import curses
from curses import wrapper
from curses.textpad import rectangle
import time
import os
import sys
from subprocess import call

# update file list function
def updateFileList():
    global fileList
    fileList = []
    tempFileList = os.listdir("Sets/")
    for index, file in enumerate(tempFileList):
        if file[len(file) - 3:] != "txt":
            tempFileList.pop(index)
    for index, file in enumerate(tempFileList):
        tempFileList[index] = file[:-4]
    tempPage = 0
    for index, file in enumerate(tempFileList):
        if index % 6 == 0:
            if index > 1:
                tempPage += 1
            fileList.append([])
        fileList[tempPage].append(file)

page = 1
selected = 1

# draw level menu function
def drawFileMenu(stdscr):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 14, centerCol - 38)
    boxBR = (centerRow + 14, centerCol + 38)

    stdscr.clear()

    text = "Choose a file:"
    stdscr.addstr(centerRow - 11, centerCol - len(text) // 2, text, white)

    text = f"Page {page}"
    stdscr.addstr(centerRow + 7, centerCol - len(text) // 2, text, white)

    text = "exit (esc)"
    stdscr.addstr(centerRow + 12, centerCol - 30 - len(text) // 2, text, white)

    text = "accept (enter)"
    stdscr.addstr(centerRow + 12, centerCol + 30 - len(text) // 2, text, white)

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
    if selected == 7:
        color = yellow
    else:
        color = cyan

    text = "Create new file"
    stdscr.addstr(centerRow + 11, centerCol - len(text) // 2, text, color)

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

    stdscr.refresh()

# move cursor function
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
    elif dir == "down" and selected != 7:
        if selected < 3:
            selected += 1
        elif selected == 3:
            selected = 7
        else:
            selected += 1
    elif dir == "left":
        if selected == 1 and page > 1:
            page -= 1
            selected = 4
        elif selected == 2 and page > 1:
            page -= 1
            selected = 5
        elif selected == 3 and page > 1:
            page -= 1
            selected = 6
        elif selected == 4:
            selected = 1
        elif selected == 5:
            selected = 2
        elif selected == 6:
            selected = 3
        elif selected == 7 and page > 1:
            page -= 1
    elif dir == "right":
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

# draw create new file menu funciton
def drawCNFMenu(stdscr, fileName):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    yellow = curses.color_pair(3)
    white = curses.color_pair(4)

    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    boxTL = (centerRow - 7, centerCol - 19)
    boxBR = (centerRow + 7, centerCol + 19)

    textBoxTL = (centerRow - 1, centerCol - 18)
    textBoxBR = (centerRow + 1, centerCol + 18)

    stdscr.clear()

    rectangle(stdscr, textBoxTL[0], textBoxTL[1], textBoxBR[0], textBoxBR[1])

    stdscr.addstr(centerRow, centerCol - (len(fileName) + 5) // 2, f"{fileName} .txt", yellow)
    stdscr.addstr(centerRow, centerCol - (len(fileName) + 5) // 2, fileName, magenta)

    text = "Type file name"
    stdscr.addstr(centerRow - 4, centerCol - len(text) // 2, text, white)

    text = "exit (esc)"
    stdscr.addstr(centerRow + 4, centerCol - 11 - len(text) // 2, text, white)

    text = "accept (enter)"
    stdscr.addstr(centerRow + 4, centerCol + 11 - len(text) // 2, text, white)

    rectangle(stdscr, boxTL[0], boxTL[1], boxBR[0], boxBR[1])

    stdscr.refresh()

# select item function
def selectItem(stdscr):
    if selected == 7:
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", 
            "$", "%", "^", "&", "*", "-", "_", "=", "+", "<", ">", "~", " "]
        fileName = ""

        while True:
            drawCNFMenu(stdscr, fileName)
            key = stdscr.getch()
            char = chr(key)
            if char in chars and len(fileName) < 30:
                fileName += char
            elif char == "\x7f" or char == "\b":
                fileName = fileName[:-1]
            elif char == "\n":
                f = open(f"Sets/{fileName}.txt", "x")
                f.close()
                updateFileList()
                return "newFile"
            elif key == 27:
                break

    else:
        setFileLines = []
        fileName = f"{fileList[page - 1][selected - 1]}.txt"
        with open(f"Sets/{fileName}", "r") as file:
            for line in file:
                setFileLines.append(line)
        with open("CurrentSet.txt", "w") as file:
            file.write(f"{fileName}\n")
            for line in setFileLines:
                file.write(line)

# screen too small function
def screenTooSmall(stdscr):
    magenta = curses.color_pair(1)
    centerRow = curses.LINES // 2
    centerCol = curses.COLS // 2

    stdscr.clear()

    text = "Screen size too small, please resize and retry"
    stdscr.addstr(centerRow, centerCol - len(text) // 2, text,  magenta)

    stdscr.refresh()
    stdscr.getch()

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

    if curses.LINES < 59 and curses.COLS < 183:
        screenTooSmall(stdscr)
        sys.exit()

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
    time.sleep(0.5)
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
    time.sleep(0.5)

    updateFileList()

    while True:
        drawFileMenu(stdscr)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            moveCursor("up")
        elif key == curses.KEY_DOWN:
            moveCursor("down")
        elif key == curses.KEY_LEFT:
            moveCursor("left")
        elif key == curses.KEY_RIGHT:
            moveCursor("right") 
        elif chr(key) == "\n":
            createFile = selectItem(stdscr)
            if createFile != "newFile":
                break
        elif key == 27:
            sys.exit()

    call(["python", "ChooseMode.py"])

wrapper(main)