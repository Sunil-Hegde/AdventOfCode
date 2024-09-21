def dataProcessor(inputFile):
    finalData = []
    with open(inputFile, 'r') as file:
        for line in file:
            temp_dict = {
                'children': -1,
                'cats': -1,
                'samoyeds': -1,
                'pomeranians': -1,
                'akitas': -1,
                'vizslas': -1,
                'goldfish': -1,
                'trees': -1,
                'cars': -1,
                'perfumes': -1
            }
            x = line.strip().split(', ')
            for item in x:
                key, value = item.split(': ')
                temp_dict[key] = int(value)
            finalData.append(temp_dict)

    return finalData

def comparePartOne(processedData):
    referenceDict = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    compList = []
    for i in processedData:
        tempList = []
        for x in i:
            if i.get(x) == referenceDict.get(x):
                tempList.append(1)
        count = 0
        for z in tempList:
            if z == 1:
                count+=1
        compList.append(count)

    return compList

def comparePartTwo(processedData):
    referenceDict = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    compList = []
    for aunt in processedData:
        count = 0
        for key, value in aunt.items():
            if key in ['cats', 'trees']:
                if value >= referenceDict[key]:
                    count += 1
            elif key in ['pomeranians', 'goldfish']:
                if value <= referenceDict[key]:
                    count += 1
            elif value == referenceDict[key]:
                count += 1
        compList.append(count)
    return compList


inputFile = "/home/sunil/Desktop/repos/AoC/2015/day16/input.txt"
processedData = dataProcessor(inputFile)
comparedDataPartOne = comparePartOne(processedData)
comparedDataPartTwo = comparePartTwo(processedData)
print("Part One: " + str(comparedDataPartOne.index(max(comparedDataPartOne)) + 1))
print("Part Two: " + str(comparedDataPartTwo.index(max(comparedDataPartTwo)) + 1))
