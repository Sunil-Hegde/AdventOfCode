from itertools import combinations

weapons_file = '/home/sunil/Desktop/repos/AoC/2015/day21/weapons.txt'
armor_file = '/home/sunil/Desktop/repos/AoC/2015/day21/armor.txt'
rings_file = '/home/sunil/Desktop/repos/AoC/2015/day21/rings.txt'

def dataProcessor(weapons, armor, rings):
    data = []
    def read_file(filepath, item_type, keys):
        with open(filepath) as file:
            for line in file:
                values = line.split()
                item = dict(zip(keys, values))
                item['type'] = item_type
                data.append(item)
    read_file(weapons, "weapon", ['name', 'cost', 'damage', 'armor'])
    read_file(armor, "armor", ['name', 'cost', 'damage', 'armor'])
    read_file(rings, "rings", ['name', 'ranking', 'cost', 'damage', 'armor'])
    return data

def generate_combinations(items):
    weapons = [item for item in items if item['type'] == 'weapon']
    armor = [item for item in items if item['type'] == 'armor']
    rings = [item for item in items if item['type'] == 'rings']
    all_combinations = []
    for weapon in weapons:
        all_combinations.append([weapon])
        for arm in armor:
            all_combinations.append([weapon, arm])
        for num_rings in range(1, 3):
            for ring_comb in combinations(rings, num_rings):
                all_combinations.append([weapon] + list(ring_comb))
        for arm in armor:
            for num_rings in range(1, 3):
                for ring_comb in combinations(rings, num_rings):
                    all_combinations.append([weapon, arm] + list(ring_comb))
    return all_combinations

def gameSimulator(playerHitpoints, playerDamage, playerArmor):
    opponentHitPoints = 109
    damageToOpponent = max(playerDamage - 2, 1)  
    damageToPlayer = max(8 - playerArmor, 1)  
    while playerHitpoints > 0 and opponentHitPoints > 0:
        opponentHitPoints -= damageToOpponent
        if opponentHitPoints <= 0:
            break
        playerHitpoints -= damageToPlayer
    return playerHitpoints > 0

def games(combinations):
    statusWin = []
    statusLose = []
    for combination in combinations:
        totalCost = sum(int(item['cost']) for item in combination)
        totalDamage = sum(int(item['damage']) for item in combination)
        totalArmor = sum(int(item['armor']) for item in combination)
        gameStatus = gameSimulator(100, totalDamage, totalArmor)
        if gameStatus:
            statusWin.append(totalCost)
        else:
            statusLose.append(totalCost)
    return [min(statusWin), max(statusLose)]

items = dataProcessor(weapons_file, armor_file, rings_file)
combinations = generate_combinations(items)
part_one, part_two = games(combinations)
print("Part One(Player would win with least amount spent): " + str(part_one))
print("Part Two(Player would lose with max amound spent): " + str(part_two))
