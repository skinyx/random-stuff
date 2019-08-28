x = open(r'D:\PyCharm projects\Advent_of_code_2015\day3\puzzle_input', encoding='UTF-8')
location = [0, 0, 0, 0]
visited_places = [[0, 0]]
counter = 0
for z in x.read():
    if counter % 2:
        if z == '>':
            location[0] += 1
        elif z == '<':
            location[0] -= 1
        elif z == '^':
            location[1] += 1
        elif z == 'v':
            location[1] -= 1
        if location[:2] not in visited_places:
            visited_places.append(location[:2])
    else:
        if z == '>':
            location[2] += 1
        elif z == '<':
            location[2] -= 1
        elif z == '^':
            location[3] += 1
        elif z == 'v':
            location[3] -= 1
        if location[2:] not in visited_places:
            visited_places.append(location[2:])
    counter += 1
print(len(visited_places))