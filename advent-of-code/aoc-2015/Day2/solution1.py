summary = 0
with open('puzzle_input', encoding='utf-8') as puzzle_file:
    for line in puzzle_file:
        lwh = line.split('x', 3)
        lwh = list(map(int, lwh))
        wrap_ribbon = lwh[0] * lwh[1] * lwh[2]
        bow_ribbon = (sorted(lwh)[0] + sorted(lwh)[1])*2
        summary += wrap_ribbon + bow_ribbon
print(summary)
