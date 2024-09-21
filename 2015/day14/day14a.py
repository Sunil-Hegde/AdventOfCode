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
    while i < time :
        if runTime < deer[2]:
            totalDistance += deer[1] 
            runTime += 1
            i+=1
        elif runTime == deer[2]:
            i+= deer[3]
            runTime = 0
        
    return totalDistance



input_file = "/home/sunil/Desktop/repos/AoC/2015/day14/input.txt"
deer = instProcessor(input_file)
deers = []
time = 2503
for i in deer:
    deers.append(computeDistance(i, time))

print("Part One: " + str(max(deers)))




                