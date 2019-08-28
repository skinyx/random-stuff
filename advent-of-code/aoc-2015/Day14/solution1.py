class Reindeer:

    def __init__(self, name1, speed1, fly1, rest1):
        self.name = name1
        self.speed = speed1
        self.fly = fly1
        self.rest = rest1
        self.cycle = rest1 + fly1

    def distance(self, sec):  # функция по определению пройденного расстояния за определённое время
        dist = 0  # пройденное расстояние
        cycle_counter = 0  # счётчик цикла (полёт + отдых)
        for travel_time in range(sec):
            if not travel_time % self.cycle:  # прошли один цикл - обнуляем его счётчик
                cycle_counter = 0
            if cycle_counter < self.fly:
                dist += self.speed
                cycle_counter += 1
            elif cycle_counter < self.cycle:
                cycle_counter += 1
        return dist


reindeers = []
time = 2503
puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day14\puzzle_input', encoding='utf-8')

for line in puzzle_input:
    name, _, _, speed, _, _, fly, _, _, _, _, _, _, rest, _ = line.split(' ')
    speed, fly, rest = int(speed), int(fly), int(rest)
    reindeers.append(Reindeer(name, speed, fly, rest).distance(time))
print(max(reindeers))
print(reindeers)