instructions = '/home/sunil/Desktop/repos/AoC/2016/day8/instructions.txt'

def processData(input):
    with open(input) as file:
        rawData = []
        for line in file:
            x = line.split()
            instr = []
            if x[0] == 'rect':
                instr.append(x[0])
                y = x[1].split('x')
                instr.append(int(y[0]))
                instr.append(int(y[1]))
            elif x[0] == 'rotate':
                instr.append(x[0])
                instr.append(x[1])
                y = x[2].split('=')
                instr.append(int(y[-1]))
                instr.append(int(x[-1]))
            rawData.append(instr)
    return rawData

def rotateRow(display, row, times):
    for _ in range(times):
        display[row].insert(0, display[row].pop())  # Pop the last element and insert it at the beginning
    return display

def rotateColumn(display, column, times):
    numberOfRows = len(display)
    columnArray = [display[i][column] for i in range(numberOfRows)]
    for _ in range(times):
        columnArray.insert(0, columnArray.pop())  # Pop the last element and insert it at the beginning
    for i in range(numberOfRows):
        display[i][column] = columnArray[i]
    return display

def turnPixelsOn(row, column, display):
    for i in range(row):
        for j in range(column):
            display[i][j] = 1
    return display

def createDisplay():
    rows = 6
    cols = 50
    display = [[0 for _ in range(cols)] for _ in range(rows)]
    return display

def executeInstructions(instructions):
    display = createDisplay()
    for i in instructions:
        if i[0] == 'rect':
            display = turnPixelsOn(i[2], i[1], display)
        elif i[0] == 'rotate':
            if i[1] == 'row':
                display = rotateRow(display, i[2], i[-1])
            elif i[1] == 'column':
                display = rotateColumn(display, i[2], i[-1])
    return display

instructionData = processData(instructions)
displayAfterInstructions = executeInstructions(instructionData)
count = sum(row.count(1) for row in displayAfterInstructions)
print(count)
for i in displayAfterInstructions:
    print(i)
