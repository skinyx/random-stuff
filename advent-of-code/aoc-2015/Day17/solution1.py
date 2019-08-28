import itertools
puzzle = []
combs = []
combinations_counter = 0
for line in open(r'D:\PyCharm projects\Advent_of_code_2015\Day17\puzzle_input', encoding='utf-8'):
    puzzle.append(int(line.rstrip()))
puzzle = sorted(puzzle)
for i in range(len(puzzle)):
    if sum(puzzle[:i]) >= 150:
        max_length = i
        break
for j in range(len(puzzle)):
    if sum(puzzle[::-1][:j]) >= 150:
        min_length = j
        break
print(max_length,min_length,puzzle)
for k in range(min_length, max_length + 1):
    combs.append(itertools.combinations(puzzle, k))
for comb in combs:
    for combination in comb:
        if sum(combination) == 150:
            combinations_counter += 1
print(combinations_counter)
