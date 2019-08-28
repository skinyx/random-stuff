import re

puzzle = open('D:\PyCharm projects\Advent_of_code_2015\Day12\puzzle_input', encoding='utf-8').read()
negative_numbers_str = re.findall(r'(?<=-)\d+', puzzle)
negative_numbers = map(int, negative_numbers_str)
all_numbers_str = re.findall(r'\d+', puzzle)
all_numbers = map(int, all_numbers_str)
summary = sum(all_numbers) - 2 * sum(negative_numbers)
print(summary)
