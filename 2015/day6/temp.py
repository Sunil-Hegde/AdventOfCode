# Initialize a 1000x1000 grid with all lights off and brightness zero
grid = [[0] * 1000 for _ in range(1000)]

# Function to process instructions and update grid
def process_instruction(instruction):
    parts = instruction.split()
    if parts[0] == 'toggle':
        start_x, start_y = map(int, parts[1].split(','))
        end_x, end_y = map(int, parts[3].split(','))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                grid[x][y] += 2
    else:
        action = parts[1]
        start_x, start_y = map(int, parts[2].split(','))
        end_x, end_y = map(int, parts[4].split(','))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == 'on':
                    grid[x][y] += 1
                elif action == 'off':
                    grid[x][y] = max(0, grid[x][y] - 1)

# Process instructions
with open('/home/sunil/Desktop/repos/AoC/2015/day6/instructions.txt') as file:
    for line in file:
        process_instruction(line.strip())

# Calculate total brightness
total_brightness = sum(sum(row) for row in grid)

print("Total brightness of all lights combined:", total_brightness)
