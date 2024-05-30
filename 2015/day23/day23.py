instructionsFile = '/home/sunil/Desktop/repos/AoC/2015/day23/instructions.txt'

def processInstructions(instructionsFile):
    processedData = []
    with open(instructionsFile) as file:
        for line in file:
            processedData.append(line.split())
    return processedData

def executeInstructions(instructions, a=0, b=0):
    currentIndex = 0
    while 0 <= currentIndex < len(instructions):
        inst = instructions[currentIndex]
        op = inst[0]
        
        if op == "hlf":
            if inst[1] == 'a':
                a //= 2
            else:
                b //= 2
            currentIndex += 1
        
        elif op == "tpl":
            if inst[1] == 'a':
                a *= 3
            else:
                b *= 3
            currentIndex += 1
        
        elif op == "inc":
            if inst[1] == 'a':
                a += 1
            else:
                b += 1
            currentIndex += 1
        
        elif op == "jmp":
            currentIndex += int(inst[1])
        
        elif op == "jie":
            if (inst[1] == 'a' and a % 2 == 0) or (inst[1] == 'b' and b % 2 == 0):
                currentIndex += int(inst[2])
            else:
                currentIndex += 1
        
        elif op == "jio":
            if (inst[1] == 'a' and a == 1) or (inst[1] == 'b' and b == 1):
                currentIndex += int(inst[2])
            else:
                currentIndex += 1

    return b

instructions = processInstructions(instructionsFile)
print("Part One: " + str(executeInstructions(instructions)))
print("Part Two: " + str(executeInstructions(instructions,1,0)))
