class Reindeer:
    def __init__(self, name1, speed1, fly1, rest1):
        self.name = name1
        self.speed = speed1
        self.fly = fly1
        self.rest = rest1
        self.cycle = rest1 + fly1
        self.distance = 0
        self.time = 0
        self.points = 0

    def one_step(self):
        if self.time == self.cycle:  # прошли один цикл - обнуляем его счётчик
            self.time = 0
        if self.time < self.fly:
            self.distance += self.speed
            self.time += 1
        elif self.time < self.cycle:
            self.time += 1
        return self.distance, self

    def leader(self):
        self.points += 1


reindeers = []
time = 2503
puzzle_input = open(r'D:\PyCharm projects\Advent_of_code_2015\Day14\puzzle_input', encoding='utf-8')
max_dist = -1
leaders = set()
for line in puzzle_input:
    name, _, _, speed, _, _, fly, _, _, _, _, _, _, rest, _ = line.split(' ')
    speed, fly, rest = int(speed), int(fly), int(rest)
    reindeers.append(Reindeer(name, speed, fly, rest))
for _ in range(time):
    for reindeer in reindeers:
        dist, deer = reindeer.one_step()
        if dist > max_dist:
            leaders = set()
            max_dist = dist
            leaders.add(deer)
        elif dist == max_dist:
            leaders.add(deer)
    for i in leaders:
        i.leader()
        print(i.name, 'have %s points' % i.points,'at %s second' % _, 'with %s distance' %i.distance)

print([i.points for i in reindeers])
print([i.distance for i in reindeers])
