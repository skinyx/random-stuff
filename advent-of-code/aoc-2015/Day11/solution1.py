import re


def incrementing(password):   # функция, которая перебирает пароли
    password = list(password)  # превращаем строку в список, чтобы можно было изменять элементы
    last_letter_index = len(password) - 1
    while password[last_letter_index] == 'z':
        password[last_letter_index] = 'a'
        last_letter_index -= 1
    password[last_letter_index] = chr(ord(password[last_letter_index]) + 1)
    return ''.join(password)  # превращаем результат обратно в сроку


switcher = True
puzzle = 'vzbxxzaa'

while switcher:
    if 'i' in puzzle or 'o' in puzzle or 'l' in puzzle:  # условие 1: в пароле нет 'i', 'o', 'l'
        pass
    elif len(set(re.findall(r'(.)\1', puzzle))) < 2:  # условие 2: есть две пары разных букв
        pass
    elif True:
        for n in range(len(puzzle) - 2):  # условие 3: чтобы было три идущие друг за другом буквы
            if ord(puzzle[n]) == (ord(puzzle[n + 1]) - 1) and ord(puzzle[n + 1]) == (ord(puzzle[n + 2]) - 1):
                switcher = False  # если все три условия выполнены - прекращаем цикл
    if switcher:
        puzzle = incrementing(puzzle)
    if puzzle == 'zzzzzzzz':  # когда перебрали все варианты - прекращаем цикл
        switcher = False
        print('Решение не найдено')
print(puzzle)