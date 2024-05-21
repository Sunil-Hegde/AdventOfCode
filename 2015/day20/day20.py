def find_min_house_with_presents(target_presents):
    limit = target_presents // 10
    house_presents = [0] * (limit + 1)

    for elf in range(1, limit + 1):
        for house in range(elf, limit + 1, elf):
            house_presents[house] += elf * 10

    for house, presents in enumerate(house_presents):
        if presents >= target_presents:
            return house

def find_min_house_with_presents_v2(target_presents):
    limit = target_presents // 11
    house_presents = [0] * (limit + 1)

    for elf in range(1, limit + 1):
        for house in range(elf, min(elf * 50 + 1, limit + 1), elf):
            house_presents[house] += elf * 11

    for house, presents in enumerate(house_presents):
        if presents >= target_presents:
            return house

target_presents = 36000000
min_house_part_one = find_min_house_with_presents(target_presents)
print("Part One: " + str(min_house_part_one))
min_house_part_two = find_min_house_with_presents_v2(target_presents)
print("Part Two: " + str(min_house_part_two))
