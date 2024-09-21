input_file = "/home/sunil/Desktop/repos/AoC/2015/day18/input.txt"
lights = [[0] * 100 for i in range(100)]

def processData(input_file, lights):
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char == '#':
                    lights[i][j] = 1
                elif char == '.':
                    lights[i][j] = 0
    return lights



def animatePartOne(lights):
    next_state = [[0] * 100 for _ in range(100)] 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(100):
        for j in range(100):
            lightsOn = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < 100 and 0 <= nj < 100 and lights[ni][nj] == 1:
                    lightsOn += 1
            if (lights[i][j] == 1 and (lightsOn == 2 or lightsOn == 3)) or (lights[i][j] == 0 and lightsOn == 3):
                next_state[i][j] = 1
            else:
                next_state[i][j] = 0
    return next_state

def animatePartTwo(lights):
    next_state = [[0] * 100 for _ in range(100)] 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    lights[0][0] = 1
    lights[0][99] = 1
    lights[99][0] = 1
    lights[99][99] = 1
    for i in range(100):
        for j in range(100):
            lightsOn = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < 100 and 0 <= nj < 100 and lights[ni][nj] == 1:
                    lightsOn += 1
            
            if (lights[i][j] == 1 and (lightsOn == 2 or lightsOn == 3)) or (lights[i][j] == 0 and lightsOn == 3):
                next_state[i][j] = 1
            else:
                next_state[i][j] = 0
    next_state[0][0] = 1
    next_state[0][99] = 1
    next_state[99][0] = 1
    next_state[99][99] = 1
    return next_state

def countLights(lights):
    count = 0
    for i in range(100):
        for j in range(100):
            if lights[i][j] == 1:
                count += 1
    return count

processedData = processData(input_file, lights)
animationPartOne = animatePartOne(processedData)
for i in range(99):
    animationPartOne = animatePartOne(animationPartOne)

countPartOne = countLights(animationPartOne)
print("Part One: " + str(countPartOne))

animationPartTwo = animatePartTwo(processedData)
for i in range(99):
    animationPartTwo = animatePartTwo(animationPartTwo)

countPartTwo = countLights(animationPartTwo)
print("Part Two: " + str(countPartTwo))

