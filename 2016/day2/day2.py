inputFile = '/home/sunil/Desktop/repos/AoC/2016/day2/instructions.txt'

def processData(inputFile):
    rawData = []
    with open(inputFile) as file:
        for line in file:
            rawData.append(line.strip()) 
    return rawData

def generateKeyPartOne(rawData):
    directions = {'U' : [0, 1], 'R' : [1, 0], 'D' : [0, -1], 'L' : [-1, 0]}
    numberGrid = {(-1, 1) : 1, (0, 1) : 2, (1, 1) : 3,
                  (-1, 0) : 4, (0, 0) : 5, (1, 0) : 6,
                  (-1, -1) : 7, (0, -1) : 8, (1, -1) : 9}
    currentLocation = [0, 0]
    key = []
    for line in rawData:
        for x in line:
            newLocation = [currentLocation[0] + directions[x][0], currentLocation[1] + directions[x][1]]
            if tuple(newLocation) in numberGrid:
                currentLocation = newLocation
        key.append(numberGrid[tuple(currentLocation)])
    return key

def generateKeyPartTwo(rawData):
    directions = {'U' : [0, 1], 'R' : [1, 0], 'D' : [0, -1], 'L' : [-1, 0]}
    numberGrid = {(0,0) : 5,
                  (1,0) : 6,
                  (2,0) : 7,
                  (3,0) : 8,
                  (4,0) : 9,
                  (1,1) : 2,
                  (2,1) : 3,
                  (3,1) : 4,
                  (2,2) : 1,
                  (1,-1) : 'A',
                  (2,-1) : 'B',
                  (3,-1) : 'C',
                  (2,-2) : 'D'}
    currentLocation = [0, 0]
    key = []
    for line in rawData:
        for x in line:
            newLocation = [currentLocation[0] + directions[x][0], currentLocation[1] + directions[x][1]]
            if tuple(newLocation) in numberGrid:
                currentLocation = newLocation
        key.append(numberGrid[tuple(currentLocation)])
    return key

data = processData(inputFile)
keyPartOne = generateKeyPartOne(data)
keyPartTwo = generateKeyPartTwo(data)
print(f"Part One: {keyPartOne}")
print(f"Part Two: {keyPartTwo}")