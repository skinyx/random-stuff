"""
Два игрока играют в игру:
Есть две чаши, в каждую из которых помещается любое количество монет.
Первый игрок кладет в первую чашу любое натуральное количество монет на свой выбор.
После этого второй игрок, зная сколько монет положил первый, кладет во вторую чашу любое натуральное количество монет на свой выбор.
После этого, начиная с первого игрока, каждый игрок совершает один из трех возможных ходов:
1. Взять любое количество монет из первой чаши
2. Взять любое количество монет из второй чаши
3. Взять одинаковое количество монет из обоих чаш
Оба игрока знают, сколько монет лежит в чашах в каждый момент времени. Побеждает тот игрок, после хода которого в обоих чашах не останется монет.
Вопросы:
• Существует ли стратегия, гарантирующая победу, если да, то у какого игрока? Опишите эту стратегию.
• Вопрос повышенной сложности: опишите формулами, какое количество монет должен взять на i-ом шаге побеждающий игрок из каждой чаши в зависимости от количества находящихся в них монет к этому шагу.
"""

unique_cases = {1: 2,
                2: 1,
                3: 5,
                5: 3,
                9: 16,
                16: 9}


def bot_turn(f, s):
    if f == s or not (f and s):
        f = 0
        s = 0
    elif s in unique_cases and f >= unique_cases[s]:
        f = unique_cases[s]
    elif f in unique_cases and s >= unique_cases[f]:
        s = unique_cases[f]
    elif f > s:
        dif = f - s
        if dif == 1:
            f = 2
            s = 1
        elif dif + 1 < s:
            s = dif + 1
            f = s + dif
        elif not (s % 2) and f > s * 2 - 1:  # 12-25 -> 12-23
            f = s * 2 - 1
        elif s > 4 and s % 2 and f > (s - 1) * 2:  # 13-25 -> 13 - 24
            f = (s - 1) * 2
        elif f % 2 and s > (f + 1) // 2:  # 8-11 -> 6-11
            s = (f + 1) // 2
        else:
            print('SYKA BUG')
    elif f < s:
        dif = s - f
        if dif == 1:
            s = 2
            f = 1
        elif dif + 1 < f:
            f = dif + 1
            s = f + dif
        elif not (f % 2) and s > f * 2 - 1:  # 12-25 -> 12-23
            s = f * 2 - 1
        elif f > 4 and f % 2 and s > (f - 1) * 2:  # 13-25 -> 13 - 24
            s = (f - 1) * 2
        elif s % 2 and f > (s + 1) // 2:  # 8-11 -> 6-11
            f = (s + 1) // 2
        else:
            print('SYKA BUG')
    print('bot turn:')
    print(f, s)
    return f, s


def player_turn(target, n, first, second):
    if n < 1:
        msg = 'Число монет не может быть отрицательным'
        raise ValueError(msg)
    elif target not in ('f', 's', 'b'):
        raise ValueError
    elif target == 'f' and first < n or target == 's' and second < n or target == 'b' and min(first, second) < n:
        msg = 'Нельзя взять больше монет, чем их есть'
        raise ValueError(msg)
    if target == 'f':
        first -= n
    elif target == 's':
        second -= n
    else:
        first -= n
        second -= n
    print(first, second)
    return first, second


first = int(input('Положите монеты в первую чашу\n'))
if first in unique_cases:
    second = unique_cases[first]
elif first % 2:
    if not ((first + 1 // 2) % 2):
        second = (first + 1) // 2
    else:
        second = (first - 1) * 2
else:
    second = first * 2 - 1

print(first, second)
print('Выбирайте:\n1) Чтобы вытащить из первой чаши, напишите: "f n" без кавычек, где n - количество монет\n2)'
      ' Для второй чаши: "s n"\n3) Из обеих: "b n"')
while first or second:
    inp = input('Player turn:\n')
    target, n = inp[0], int(inp[2:])
    first, second = player_turn(target, n, first, second)
    first, second = bot_turn(first, second)

print('You Lose')
print(first, second)
