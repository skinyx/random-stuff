x = open(r'D:\PyCharm projects\Advent_of_code_2015\day3\puzzle_input', encoding='UTF-8')
location = [0, 0]
visited_places = [[0, 0]]

for z in x.read():
    if z == '>':
        location[0] += 1
    elif z == '<':
        location[0] -= 1
    elif z == '^':
        location[1] += 1
    elif z == 'v':
        location[1] -= 1
    if location not in visited_places:
        visited_places.append(location[:])
print(len(visited_places))

