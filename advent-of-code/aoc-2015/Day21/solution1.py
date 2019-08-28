import itertools
from math import ceil
import sys


def fight(me):
    cost = 0
    my_hp = 100
    my_armor = 0
    my_damage = 0
    boss_hp = 109
    boss_armor = 2
    boss_damage = 8
    for equip in me:
        if isinstance(equip, tuple):
            cost += int(equip[0][-3]) + int(equip[1][-3])
            my_damage += int(equip[0][-2]) + int(equip[1][-2])
            my_armor += int(equip[0][-1]) + int(equip[1][-1])
        else:
            cost += int(equip[-3])
            my_damage += int(equip[-2])
            my_armor += int(equip[-1])
    my_damage_on_boss = my_damage - boss_armor
    if my_damage_on_boss < 1:
        my_damage_on_boss = 1
    boss_damage_on_me = boss_damage - my_armor
    if boss_damage_on_me < 1:
        boss_damage_on_me = 1
    me_dead = ceil(my_hp / boss_damage_on_me)
    boss_dead = ceil(boss_hp / my_damage_on_boss)
    if boss_dead <= me_dead:
        return cost
    else:
        return sys.maxsize


equipment = []
for line in open(r'puzzle_input', encoding='utf-8'):
    if ':' in line:
        equipment.append([])
        continue
    if not line == '\n':
        equipment[-1].append(line.split())
equipment[1].append(['No_armor', 0, 0, 0])
equipment[2].append(['No_ring', 0, 0, 0])
rings = itertools.combinations(equipment[2])
all_variations = itertools.product(equipment[0], equipment[1], rings)
low_cost = sys.maxsize
for battle in all_variations:
    low_cost = min(fight(battle), low_cost)
print(low_cost)
