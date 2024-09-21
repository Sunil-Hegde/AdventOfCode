from itertools import combinations
from functools import reduce

def find_combinations(numbers, target):
    def backtrack(start, path, target):
        if target == 0:
            combinations.add(tuple(sorted(path)))
            return
        for i in range(start, len(numbers)):
            if numbers[i] <= target:
                backtrack(i + 1, path + [numbers[i]], target - numbers[i])
                
    combinations = set()
    backtrack(0, [], target)
    return combinations

def findSmallList(combinations):
    min_entanglement = float('inf')
    for combo in combinations:
        entanglement = reduce(lambda x, y: x * y, combo)
        min_entanglement = min(min_entanglement, entanglement)
    return min_entanglement

def processData(inputFile):
    processedData = []
    with open(inputFile) as file:
        total_sum = 0
        for line in file:
            x = int(line.strip())
            total_sum += x
            processedData.append(x)
    return processedData, total_sum

inputFile = '/home/sunil/Desktop/repos/AoC/2015/day24/input.txt'
numberList, total_sum = processData(inputFile)

target = total_sum // 3
combinations = find_combinations(numberList, target)
print("Part One:", findSmallList(combinations))

newTarget = total_sum // 4
newCombinations = find_combinations(numberList, newTarget)
print("Part Two:", findSmallList(newCombinations))
