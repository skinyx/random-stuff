import itertools
import functools


def total_score(*args):
    properties = [0, 0, 0, 0, 0]
    properties[0] = 5 * args[0] - args[1] - args[3]
    properties[1] = - args[0] + 3 * args[1] - args[2]
    properties[2] = 4 * args[2]
    properties[3] = 2 * args[3]
    properties[4] = 5 * args[0] + args[1] + 6 * args[2] + 8 * args[3]
    for i in properties[:-1]:
        if i <= 0:
            return 0
    return functools.reduce(lambda x, y: x * y, properties[:-1])


all_possible_situtations = itertools.product(range(101), repeat=4)
all_possible_situtations = itertools.filterfalse(lambda i: sum(i) - 100, all_possible_situtations)
max_ = -1
for i in all_possible_situtations:
    max_ = max(total_score(*i), max_)
print(max_)
