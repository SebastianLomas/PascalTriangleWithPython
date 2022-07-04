from Include import pascalLib as pl

def main():
    numberOfRows = pl.getNumberOfRows("Give Me A Limit(Integer): ")
    currentRow = [1]
    nextRow = list()
    initialSpaces = numberOfRows - 1
    currentRowPosition = 0

    while currentRowPosition < numberOfRows:
        print(currentRow)
        currentRow = pl.createCurrentRow(currentRow)

        currentRowPosition += 1



if __name__ == '__main__':
    main()