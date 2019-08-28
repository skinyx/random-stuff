import re, numpy

puzzle = open(r'D:\PyCharm projects\Advent_of_code_2015\Day6\puzzle_input', encoding='utf-8')
grid = numpy.zeros((1000, 1000), int)


def toggle(x):
    if x == 0:
        return 1
    elif x == 1:
        return 0


for line in puzzle:
    grid[grid < 0] = 0
    coord1, coord2, coord3, coord4 = map(int, re.findall(r'\d+', line))
    command = re.search(r'(^.*?)(?=\d+)', line).group(1).rstrip()
    if command == 'turn on':
        grid[coord1:coord3+1, coord2:coord4+1] = grid[coord1:coord3+1, coord2:coord4+1] + 1
    elif command == 'turn off':
        grid[coord1:coord3+1, coord2:coord4+1] = grid[coord1:coord3+1, coord2:coord4+1] - 1
    elif command == 'toggle':
        grid[coord1:coord3+1, coord2:coord4+1] = grid[coord1:coord3+1, coord2:coord4+1] + 2

print(numpy.sum(grid))
