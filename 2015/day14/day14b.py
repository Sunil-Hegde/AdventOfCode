def instProcessor(input_file):
    rawData = []  
    with open(input_file, 'r') as file:
        for line in file:
            x = line.split()
            rawData.append([x[0], int(x[3]), int(x[6]), int(x[-2])])

    return rawData

def computeDistance(deer, time):
    totalDistance = 0
    runTime = 0
    i = 0
    distance = []
    while i < time:
        if runTime < deer[2]:
            totalDistance += deer[1] 
            distance.append(totalDistance)
            runTime += 1
            i += 1
        elif runTime == deer[2]:
            i += deer[3]
            runTime = 0
            for x in range(deer[3]):
                distance.append(totalDistance)  # Keep track of the distance even during rest
    return distance

def computeRaceResult(deers, time):
    points = [0] * len(deers)
    for i in range(time):
        distances = [deer[i] for deer in deers]
        max_distance = max(distances)
        for j, distance in enumerate(distances):
            if distance == max_distance:
                points[j] += 1
    return points

input_file = "/home/sunil/Desktop/repos/AoC/2015/day14/input.txt"
deer = instProcessor(input_file)
deers = []
time = 2503
for i in deer:
    deers.append(computeDistance(i, time))

result = computeRaceResult(deers, time)
print("Part two: " + str(max(result)))
