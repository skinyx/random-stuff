import re

representation = 0
in_memory = 0

puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day8\puzzle_input', encoding='utf-8')
for line in puzzle_input:
    line = line.rstrip()
    print(line)
    z = re.findall(r'\\x[0-9a-f]{2}', line)
    d = re.findall(r'"', line)
    t = re.findall(r'\\\\(?![x[0-9a-f]{2}])', line)
    representation += len(line)
    in_memory = in_memory + len(line) - 3 * len(re.findall(r'\\x[0-9a-f]{2}', line)) - 1 * len(re.findall(r'"', line)) - 1 * len(re.findall(r'\\\\(?![x[0-9a-f]{2}])', line))
    print(len(line), len(line) - 3 * len(re.findall(r'\\x[0-9a-f]{2}', line)) - 1 * len(re.findall(r'"', line)) - 1 * len(re.findall(r'\\\\(?![x[0-9a-f]{2}])', line)))
print(representation - in_memory)
