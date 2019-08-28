import re

puzzle = '1113222113'


def look_n_say(string, i):
    for j in range(i):
        string = ''.join([str(len(match.group(1))) + match.group(2) for match in re.finditer(r'((.)\2*)', string)])
    return len(string)


print(look_n_say(puzzle, 50))
