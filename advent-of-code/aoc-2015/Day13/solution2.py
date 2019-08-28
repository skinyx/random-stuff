from itertools import permutations
puzzle_input = open('puzzle_input', encoding='utf-8')

names = set()  # список уникальных имён для дальнейших перестановок
names.add('Ivan')  # добавляю себя в список сидящих за столом
happiness_dict = dict()  # словарь, в котором по принципу словарь[имя1][имя2] будет выдаваться уровень счасться имя1, если он рядом с имя2
happiness_dict['Ivan'] = {'Alice': 0, 'Bob': 0, 'Carol': 0, 'David': 0,  # добавляю себя в список сидящих за столом
                          'Eric': 0, 'Frank': 0, 'George': 0, 'Mallory': 0}
total_happiness = 0
max_happiness = - 10000000000000000
for line in puzzle_input:
    name1, _, sign, value, *_, name2 = line.split(' ')
    names.add(name1)
    if sign == 'gain':
        happiness_dict.setdefault(name1, dict())[name2.rstrip('.\n')] = int(value)
    if sign == 'lose':
        happiness_dict.setdefault(name1, dict())[name2.rstrip('.\n')] = - int(value)
    happiness_dict.setdefault(name1, dict())['Ivan'] = 0

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
