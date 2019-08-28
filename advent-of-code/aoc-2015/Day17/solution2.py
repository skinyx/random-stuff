import itertools

puzzle = []
combs = []
combinations_counter = 0
for line in open(r'D:\PyCharm projects\Advent_of_code_2015\Day17\puzzle_input', encoding='utf-8'):
    puzzle.append(int(line.rstrip()))
puzzle = sorted(puzzle)
for j in range(len(puzzle)):
    if sum(puzzle[::-1][:j]) >= 150:
        min_length = j
        break
for comb in itertools.combinations(puzzle, min_length):
    if sum(comb) == 150:
        combinations_counter += 1
print(combinations_counter)
