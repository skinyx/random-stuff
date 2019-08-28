import re

puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day5\puzzle_input')
counter = 0

for line in puzzle_input:
    if (not re.search(r'ab|cd|pq|xy', line))\
        and re.search(r'(?P<double>.)(?P=double)', line)\
        and re.search(r'.*[aeiou].*[aeiou].*[aeiou].*', line):
        counter += 1
print(counter)
