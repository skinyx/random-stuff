lights_matrix = [list(puzzle.rstrip()) for puzzle in open(r'puzzle_input', encoding='utf-8')]


def on_or_off(grid, i, j):
    indicator = 0
    if (i == 0 and j == 0) or (i == 0 and j == len(grid[i]) - 1) or (i == len(grid) - 1 and j == 0) or (i == len(grid) - 1 and j == len(grid[i]) - 1):
        return True
    if j > 0 and grid[i][j - 1] == '#':
        indicator += 1
    if j < len(grid) - 1 and grid[i][j + 1] == '#':
        indicator += 1
    if i > 0:
        if grid[i - 1][j] == '#':
            indicator += 1
        if j > 0 and grid[i - 1][j - 1] == '#':
            indicator += 1
        if j < len(grid) - 1 and grid[i - 1][j + 1] == '#':
            indicator += 1
    if i < len(grid) - 1:
        if grid[i + 1][j] == '#':
            indicator += 1
        if j > 0 and grid[i + 1][j - 1] == '#':
            indicator += 1
        if j < len(grid) - 1 and grid[i + 1][j + 1] == '#':
            indicator += 1
    if indicator == 3:
        return True
    elif grid[i][j] == '#' and indicator == 2:
        return True
    else:
        return False


def bool_to_lights(bool_mat):
    lights_mat = []
    for list_ in bool_mat:
        cache = []
        for item in list_:
            if item:
                cache.append('#')
            else:
                cache.append('.')
        lights_mat.append(cache)
    return lights_mat


for _ in range(100):
    bool_matrix = [[on_or_off(lights_matrix, i, j) for j in range(len(lights_matrix[1]))] for i in range(len(lights_matrix))]
    lights_matrix = bool_to_lights(bool_matrix)

total = 0
for i in bool_matrix:
    total += sum(i)
print(total)
'''
animation = []
for _ in range(99):
    bool_matrix = [[on_or_off(lights_matrix, i, j) for j in range(len(lights_matrix[1]))] for i in range(len(lights_matrix))]
    lights_matrix = bool_to_lights(bool_matrix)
    good_looking_matrix = '\n'.join([''.join(line1) for line1 in lights_matrix])
    animation.append(good_looking_matrix)
for i in animation:
    print(i)
    print(''.join(['_' for _ in range(20)]))
'''