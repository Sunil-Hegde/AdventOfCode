def parse_input(input_file):
    rawData = []  
    with open(input_file, 'r') as file:
        for line in file:
            x = line.split()
            rawData.append({'name': x[0][:-1], 
                            'capacity': int(x[2][:-1]), 
                            'durability': int(x[4][:-1]), 
                            'flavor': int(x[6][:-1]), 
                            'texture': int(x[8][:-1]), 
                            'calories': int(x[10])})
    return rawData

def calculate_cookie_properties(combo, ingredients):
    properties = {'capacity': 0, 'durability': 0, 'flavor': 0, 'texture': 0, 'calories': 0}
    for i, ingredient in enumerate(ingredients):
        for prop in properties:
            properties[prop] += combo[i] * ingredient[prop]
    for prop in properties:
        if prop != 'calories' and properties[prop] < 0:
            properties[prop] = 0
    return properties

def calculate_total_score(properties):
    total_score = 1
    for prop in properties:
        if prop != 'calories':
            total_score *= max(0, properties[prop])
    return total_score

def find_highest_score(ingredients, calorie_limit=None):
    highest_score = 0
    for combo in combinations_summing_to(100, len(ingredients)):
        properties = calculate_cookie_properties(combo, ingredients)
        if calorie_limit is not None and properties['calories'] != calorie_limit:
            continue
        score = calculate_total_score(properties)
        highest_score = max(highest_score, score)
    return highest_score

def combinations_summing_to(total, length):
    if length == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for combo in combinations_summing_to(total - i, length - 1):
                yield (i,) + combo

def main(input_file):
    ingredients = parse_input(input_file)
    highest_score = find_highest_score(ingredients)
    print("Total score of the highest-scoring cookie (Part One):", highest_score)
    highest_score_500_calories = find_highest_score(ingredients, calorie_limit=500)
    print("Total score of the highest-scoring cookie with 500 calories (Part Two):", highest_score_500_calories)

input_file = "/home/sunil/Desktop/repos/AoC/2015/day15/input.txt"  
main(input_file)
