from itertools import permutations

def instProcessor(input_file):
    rawData = {} 
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.split()
            person1, person2 = parts[0], parts[-1][:-1]
            happiness = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])
            if person1 not in rawData:
                rawData[person1] = {}
            rawData[person1][person2] = happiness

    return rawData

def calculateTotalHappiness(seating, data):
    totalHappiness = 0
    n = len(seating)
    for i in range(n):
        person1 = seating[i]
        person2 = seating[(i + 1) % n]  
        totalHappiness += data[person1][person2]
        totalHappiness += data[person2][person1]
    return totalHappiness

def findOptimalSeating(data):
    all_permutations = permutations(data.keys())
    max_happiness = float('-inf')
    for permutation in all_permutations:
        totalHappiness = calculateTotalHappiness(permutation, data)
        max_happiness = max(max_happiness, totalHappiness)
    return max_happiness

input_file = "/home/sunil/Desktop/repos/AoC/2015/day13/input.txt"
data = instProcessor(input_file)
max_happiness = findOptimalSeating(data)
print("Part One:", max_happiness)
