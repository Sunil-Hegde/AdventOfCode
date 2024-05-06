def dataProcessor(inputFile):
    finalData = []
    with open(inputFile, 'r') as file:
        for line in file:
            finalData.append(int(line))
    return finalData

def find_combinations(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            backtrack(i + 1, target - nums[i], path + [nums[i]])

    result = []
    nums.sort()
    backtrack(0, target, [])
    return result

def findMinimum(combinations):
    sizeList = []
    for i in combinations:
        sizeList.append(len(i))
    minSize = min(sizeList)
    minList = []
    for x in combinations:
        if len(x) == minSize:
            minList.append(x)
    
    return minList

inputFile = "/home/sunil/Desktop/repos/AoC/2015/day17/input.txt"
nums = dataProcessor(inputFile)
target = 150
combinations = find_combinations(nums, target)
print("Part One: Number of combinations that add up to 150 are: " + str(len(combinations)))
print("Part Two: Minimum of containers and number of ways: " + str(len(findMinimum(combinations))))
