def parser(iterable):  # функция для парсинга итерируемых объектов
    sum = 0
    for item in iterable:
        if isinstance(item, dict):
            sum += dict_parser(item)
        elif isinstance(item, list):
            sum += parser(item)
        elif isinstance(item, int):
            sum += item
    return sum


def dict_parser(object):  # отдельная функция для парсинга словарей, чтобы не делать первую функцию слишком большой
    sum = 0
    if 'red' in object.keys() or 'red' in object.values():  # убираем словари, в которых есть 'red'
        return 0
    for value in object.values():
        if isinstance(value, dict):
            sum += dict_parser(value)
        elif isinstance(value, list):
            sum += parser(value)
        elif isinstance(value, int):
            sum += value
    return sum


puzzle = open('D:\PyCharm projects\Advent_of_code_2015\Day12\puzzle_input', encoding='utf-8')
puzzle_list = eval(puzzle.read())
print(parser(puzzle_list))