import re

re.findall('([a-zA-Z]+):? (\d+)', 'Sue 1: cars: 9, akitas: 3, goldfish: 0')
puzzle = open(r'D:\PyCharm projects\Advent_of_code_2015\Day16\puzzle_input', encoding='utf-8')

all_Sues = list()
compounds_dict = {'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0', 'vizslas': '0', 'goldfish': '5',
                  'trees': '3', 'cars': '2', 'perfumes': '1'}
compounds = (
'children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes')
for line in puzzle:
    can_remember = re.findall(r'([a-zA-Z]+):? (\d+)', line)
    Sue_dict = {key: value for key, value in can_remember}
    length = len(Sue_dict)
    for compound in Sue_dict:
        if compound == 'Sue':
            pass
        elif Sue_dict[compound] == compounds_dict[compound]:
            length -= 1
    all_Sues.append(length - 1)
print(all_Sues)
print(all_Sues.index(0)+1)
