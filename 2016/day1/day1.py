inputFile = '/home/sunil/Desktop/repos/AoC/2016/day1/instructions.txt'

def processData(inputFile):
    with open(inputFile) as file:
        rawData = [line.strip().split(", ") for line in file][0]
        return rawData

def countTotalAndFirstRevisit(rawData):
    directions = ['N', 'E', 'S', 'W']
    currentDirectionIndex = 0
    currentPosition = (0, 0)
    visitedLocations = set()
    visitedLocations.add(currentPosition)
    firstRevisitedLocation = None
    
    n, s, e, w = 0, 0, 0, 0
    
    for instruction in rawData:
        turn = instruction[0]
        steps = int(instruction[1:])
        
        if turn == 'R':
            currentDirectionIndex = (currentDirectionIndex + 1) % 4
        elif turn == 'L':
            currentDirectionIndex = (currentDirectionIndex - 1) % 4
        
        for _ in range(steps):
            if directions[currentDirectionIndex] == 'N':
                currentPosition = (currentPosition[0], currentPosition[1] + 1)
                n += 1
            elif directions[currentDirectionIndex] == 'E':
                currentPosition = (currentPosition[0] + 1, currentPosition[1])
                e += 1
            elif directions[currentDirectionIndex] == 'S':
                currentPosition = (currentPosition[0], currentPosition[1] - 1)
                s += 1
            elif directions[currentDirectionIndex] == 'W':
                currentPosition = (currentPosition[0] - 1, currentPosition[1])
                w += 1
            
            if currentPosition in visitedLocations and firstRevisitedLocation is None:
                firstRevisitedLocation = currentPosition
            
            visitedLocations.add(currentPosition)

    totalDistance = abs(n - s) + abs(e - w)
    firstRevisitDistance = abs(firstRevisitedLocation[0]) + abs(firstRevisitedLocation[1]) if firstRevisitedLocation else None
    
    return totalDistance, firstRevisitDistance

processedData = processData(inputFile)
totalDistance, firstRevisitDistance = countTotalAndFirstRevisit(processedData)

print("Shorted distance:", totalDistance, "blocks")
print("First location visited twice is", firstRevisitDistance, "blocks away.")
