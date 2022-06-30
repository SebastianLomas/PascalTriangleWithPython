def indexExists(myList,index):
    listLength = len(myList)
    if(index < listLength):
        return True
    else:
        return False

def main():
    currentRow = [1]
    nextRow = list()
    numberOfRows = 10
    initialSpaces = numberOfRows - 1
    y = 0

    while y < numberOfRows:
        print(" "*initialSpaces,*currentRow)
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