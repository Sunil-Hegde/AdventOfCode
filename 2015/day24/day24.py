inputFile = '/home/sunil/Desktop/repos/AoC/2015/day24/input.txt'

def processData(inputFile):
    processedData = []
    with open(inputFile) as file:
        total_sum = 0
        for line in file:
            x = int(line.strip())
            total_sum += x
            processedData.append(x)
    return processedData, total_sum

def unique_combination(A, target, local=[], start=0):
    result = []
    if target == 0:
        result.append(local)
        return result

    for i in range(start, len(A)):
        if A[i] > target:
            continue
        if i > start and A[i] == A[i - 1]:
            continue
        result += unique_combination(A, target - A[i], local + [A[i]], i + 1)
    return result

def find_combinations(A, target):
    A.sort()
    return unique_combination(A, target)

def findSmallList(combinations):
    minLength = min(map(len, combinations))
    smallList = []
    quantumEntanglement = []
    for i in combinations:
        if len(i) == minLength:
            smallList.append(i)
    
    for j in smallList:
        entanglement = 1
        for k in j:
            entanglement*=k
        quantumEntanglement.append(entanglement)
    return min(quantumEntanglement)

numberList, total_sum = processData(inputFile)
target = total_sum // 3
combinations = find_combinations(numberList, target)
print("Part One: " + str(findSmallList(combinations)))
newTarget = total_sum // 4
newCombinations = find_combinations(numberList, newTarget)
print("Part Two: " + str(findSmallList(newCombinations)))


