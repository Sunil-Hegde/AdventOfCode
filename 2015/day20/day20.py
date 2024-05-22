import math

def giftsCalculatorPartOne(number):
    sum = 0
    sqrt_num = int(math.sqrt(number))
    for i in range(1, sqrt_num + 1):
        if number % i == 0:
            sum += i * 10
            if i != number // i:  
                sum += (number // i) * 10
    return sum

def giftsCalculatorPartTwo(number, elves):
    sum = 0
    sqrt_num = int(math.sqrt(number))
    for i in range(1, sqrt_num + 1):
        if number % i == 0:
            if elves[i] < 50:
                sum += i * 11
                elves[i] += 1
            if i != number // i and elves[number // i] < 50:
                sum += (number // i) * 11
                elves[number // i] += 1
    return sum

def findHousePartOne(target_gifts):
    houseNumber = 1
    while True:
        giftsPerHouse = giftsCalculatorPartOne(houseNumber)
        #print(f"Gifts for house {houseNumber} is {giftsPerHouse}")
        if giftsPerHouse >= target_gifts:
            break
        houseNumber += 1
    return houseNumber

def findHousePartTwo(target_gifts):
    houseNumber = 1
    elves = [0] * (target_gifts + 1) 
    while True:
        giftsPerHouse = giftsCalculatorPartTwo(houseNumber, elves)
        #print(f"Gifts for house {houseNumber} is {giftsPerHouse}")
        if giftsPerHouse >= target_gifts:
            break
        houseNumber += 1
    return houseNumber

number = 36000000
print(f"Part One: {findHousePartOne(number)}")
print(f"Part Two: {findHousePartTwo(number)}")
