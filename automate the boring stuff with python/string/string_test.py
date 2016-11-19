
def printTable(tableData):
    colWidths = []
    result = []
    for index in range(len(tableData)):
        maxLen = 0
        item = tableData[index]
        for string in item:
            if maxLen < len(string):
                maxLen = len(string)
        colWidths.append(maxLen)

    for space in colWidths:
        print(str(space) + " ", end='')

    print(len(tableData[0]))
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            justlen = colWidths[j] - len(tableData[j][i])
            print(tableData[j][i] + " ", end='')
        print("\t")

    # if len(tableData) > 0:
    #     for i in range(len(tableData[0])):
    #         for j in range(len(tableData)):
    #             print(tableData[i][j] + " ", end='')
    #         print
                # print(tableData[i][j].rjust(colWidths[i] - len(tableData[i][j])), end='')

if __name__ == '__main__':
    tableData = [['apple', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
