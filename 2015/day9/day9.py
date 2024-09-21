from itertools import permutations

def instProcessor(input_file):
    rawData = []  
    with open(input_file, 'r') as file:
        for line in file:
            x = line.split()
            rawData.append([x[0], x[2], int(x[-1])])

    return rawData

def calculate_total_distance(routes, permutation):
    total_distance = 0
    for i in range(len(permutation) - 1):
        from_place = permutation[i]
        to_place = permutation[i + 1]
        route = next((r for r in routes if (r[0] == from_place and r[1] == to_place) or (r[0] == to_place and r[1] == from_place)), None)
        if route:
            total_distance += route[2]  

    return total_distance

def finalAnswer(all_permutations):
    distance = []
    for permutation in all_permutations:
        total_distance = calculate_total_distance(routes, permutation)
        distance.append(total_distance)
    print("Part one: " + str(min(distance)))
    print("Part two: " + str(max(distance)))

input_file = "input.txt"
routes = instProcessor(input_file)
unique_places = set()
for route in routes:
    unique_places.add(route[0])
    unique_places.add(route[1])
all_permutations = permutations(unique_places)

finalAnswer(all_permutations)




                