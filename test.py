
import curses
from curses import wrapper
from curses.textpad import rectangle
import time
import os
from subprocess import call

# define variables
fileList = []

# update file list function
def updateFileList():
    global fileList
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

updateFileList()
print(len(fileList))