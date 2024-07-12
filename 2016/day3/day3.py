inputFile = '/home/sunil/Desktop/repos/AoC/2016/day3/instructions.txt'

def processData(inputFile):
    rawData = []
    with open(inputFile) as file:
        for line in file:
            x = line.split()
            rawData.append(x)
    return rawData

def processDataPartTwo(inputFile):
    rawData = []
    with open(inputFile) as file:
        for line in file:
            x = list(map(int, line.split()))
            rawData.append(x)
    
    column_data = [[], [], []]  # To store columns separately
    for row in rawData:
        for i in range(3):
            column_data[i].append(row[i])
    
    result = []
    for col in column_data:
        for i in range(0, len(col), 3):
            result.append(col[i:i+3])
    
    return result

def checkTriangles(rawData):
    possibleTriangles = 0
    for x in rawData:
        sides = [int(x[0]), int(x[1]), int(x[2])]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            possibleTriangles+=1
    return possibleTriangles

data = processData(inputFile)
data1 = processDataPartTwo(inputFile)
print(f"Number of possible triangles: {checkTriangles(data)}")
print(f"Number of possible triangles according to columns: {checkTriangles(data1)}")
