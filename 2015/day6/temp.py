def processData(input_file):
    rawData = []    
    with open(input_file, 'r') as file:
        for line in file:
            x = line.split()
            if x[0] == "turn":
                x.pop(3)
                x[0] = x[0] + x[1]  
                x.pop(1) 
            else:
                x.pop(2)
            rawData.append(x)
                  
    return rawData

def lightsFunctionPartOne(lights, instructions):
    for i in instructions:
        x = i[1].split(',')
        y = i[-1].split(',')
        if i[0] == "turnon":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    lights[m][n] = 1
        elif i[0] == "turnoff":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    lights[m][n] = 0
        elif i[0] == "toggle":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    if lights[m][n] == 0:
                        lights[m][n] = 1
                    elif lights[m][n] == 1:
                        lights[m][n] = 0
    count = 0
    for i in lights:
        for j in i:
            if j == 1:
                count+=1
    return count

def lightsFunctionPartTwo(lights, instructions):
    for i, instr in enumerate(instructions):
        x = instr[1].split(',')
        y = instr[-1].split(',')
        if instr[0] == "turnon":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    lights[m][n] += 1
        elif instr[0] == "turnoff":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    lights[m][n] = max(0, lights[m][n] - 1)
        elif instr[0] == "toggle":
            for m in range(int(x[0]), int(y[0])+1):
                for n in range(int(x[1]), int(y[1])+1):
                    lights[m][n] += 2
    total_brightness = sum(sum(row) for row in lights)
    return total_brightness

input_file = "/home/sunil/Desktop/repos/AoC/2015/day6/instructions.txt"
lights = [[0] * 1000 for i in range(1000)]
instructions = processData(input_file)
partOne = lightsFunctionPartOne(lights, instructions)
print("Part One: " + str(partOne))
partTwo = lightsFunctionPartTwo(lights, instructions)
print("Part Two: " + str(partTwo))
