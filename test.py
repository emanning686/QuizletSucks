from textwrap import wrap

currentCard = 0

cardSet = []
homeFilename = ""
def createCardSet():
    global cardSet, homeFileName
    with open("CurrentSet.txt", "r") as file:
        homeFileName = file.readline().replace("\n", "")
        for line in file:
            card = line.replace("\n", "").split("|")
            cardSet.append(card)

createCardSet()

newTextList1 = []
newTextList2 = []
cardFront = str(cardSet[currentCard][0][:130])
newTextList1 = wrap(cardFront, 28)

print(newTextList1)