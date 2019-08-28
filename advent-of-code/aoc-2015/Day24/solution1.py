import itertools, functools
puzzle = open(r'puzzle_input', encoding='utf-8')
list_ = []
for i in puzzle:
    list_.append(int(i))
total_weight = sum(list_)
group_weight = total_weight // 3
sorted_list = sorted(list_, reverse=True)
for j in range(len(list_) + 1):
    if sum(sorted_list[:j + 1]) >= group_weight:
        min_packages = j + 1
        break

min_prod = 99999999999999999999
breaker = False
for comb_len in range(min_packages, len(list_) - 1):
    combs = itertools.combinations(list_, comb_len)
    for comb in combs:
        if sum(comb) == group_weight:
            min_prod = min(min_prod, functools.reduce(lambda x, y: x * y, comb))
            breaker = True
            break
    if breaker:
        break
print(min_prod)
