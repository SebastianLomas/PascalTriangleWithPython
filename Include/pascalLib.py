def indexExists(myList,index):
    listLength = len(myList)
    if(index < listLength):
        return True
    else:
        return False

def getNumberOfRows(message):
    while True:
        try:
            numberOfRows = int(input(message))
            return numberOfRows
        except:
            print("Error: The Value Most Be An Integer...")

def createCurrentRow(currentRow):
    nextRow = list()
    nextRow.append(1)
    currentRowLen = len(currentRow)
    index = 0

    while index < currentRowLen:
        if indexExists(currentRow,index+1):
            nextValue = currentRow[index] + currentRow[index+1]
            nextRow.append(nextValue)
            index += 1
        else:
            break

    nextRow.append(1)
    return nextRow



#You may ask why did i added this function instead of using spread operator
#Well, when the pascal triangle is printend, numbers with more than two digits
#ruin the format of the triangle, that's why i created it, I'll fix that.
"""def printPascal(rowToPrint):
    index = 0
    lastNumberIndex = len(rowToPrint) - 1
    for currentNumber in rowToPrint:
        if index == lastNumberIndex:
            print(currentNumber)
        else:
            print(currentNumber,end=" ")
        index += 1"""