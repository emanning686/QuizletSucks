import os
tempFileList = os.listdir()
fileList = []
tempPage = 0
for index, file in enumerate(tempFileList):
    if file[len(file) - 3:] != "txt":
        tempFileList.pop(index)
for index, file in enumerate(tempFileList):
    tempFileList[index] = file[:-4]
print(tempFileList)