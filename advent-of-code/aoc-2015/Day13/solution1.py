from itertools import permutations
puzzle_input = open('D:\PyCharm projects\Advent_of_code_2015\Day13\puzzle_input', encoding='utf-8')

names = set()  # список уникальных имён для дальнейших перестановок
happiness_dict = dict()  # словарь, в котором по принципу словарь[имя1][имя2] будет выдаваться уровень счасться имя1, если он рядом с имя2
total_happiness = 0
max_happiness = - 10000000000000000
for line in puzzle_input:
    name1, _, sign, value, _, _, _, _, _, _, name2 = line.split(' ')
    names.add(name1)
    if sign == 'gain':
        happiness_dict.setdefault(name1, dict())[name2.rstrip('.\n')] = int(value)
    if sign == 'lose':
        happiness_dict.setdefault(name1, dict())[name2.rstrip('.\n')] = - int(value)
perms = permutations(list(names))  # все возможные размещения за столом

for item in perms:
    item = item + (item[0],)  # сидящие за столом по часовой стрелке
    item += item[-2::-1]  # добавим направление против часовой
    for i in range(len(item) - 1):
        total_happiness += happiness_dict[item[i]][item[i + 1]]  # уровень счастья по часовой стрелке и против
    max_happiness = max(max_happiness, total_happiness)
    if total_happiness == 618:
        print(item)
    total_happiness = 0
print(max_happiness)
