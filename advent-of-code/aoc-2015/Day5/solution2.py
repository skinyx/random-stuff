import re

puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day5\puzzle_input')
counter = 0

for line in puzzle_input:
    if re.search(r'.*(?P<first>.)(?P<second>.).*(?P=first)(?P=second)(?!P=second).*', line) \
   and re.search(r'.*(.).\1.*', line):
        counter += 1
print(counter)
