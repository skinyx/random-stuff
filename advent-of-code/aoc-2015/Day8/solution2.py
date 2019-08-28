import re

new_code = 0
old_code = 0

puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day8\puzzle_input', encoding='utf-8')
for line in puzzle_input:
    line = line.rstrip()
    old_code += len(line)
    line = re.sub(r'\\', r'\\\\', line)
    line = re.sub(r'"', r'\"', line)
    line = line.center(len(line)+2, '"')
    r = len(line)
    new_code += len(line)
print(new_code - old_code)
