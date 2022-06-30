def indexExists(myList,index):
    listLength = len(myList)
    if(index < listLength):
        return True
    else:
        return False

def printPascal(rowToPrint):
    index = 0
    lastNumberIndex = len(rowToPrint) - 1
    for currentNumber in rowToPrint:
        if index == lastNumberIndex:
            print(currentNumber)
        else:
            print(currentNumber,end=" ")
        index += 1

def main():
    currentRow = [1]
    nextRow = list()
    numberOfRows = 10
    initialSpaces = numberOfRows - 1
    y = 0

    while y < numberOfRows:
        print(" "*initialSpaces,end="")
        printPascal(currentRow)
        nextRow.append(1)
        i = 0

        while i < len(currentRow):
            if indexExists(currentRow,i+1):
                nextRow.append(currentRow[i] + currentRow[i+1])

            i += 1

        nextRow.append(1)
        currentRow.clear()
        
        for i in nextRow:
            currentRow.append(i) 

        nextRow.clear()
        y += 1
        initialSpaces -= 1

if __name__ == '__main__':
    main()