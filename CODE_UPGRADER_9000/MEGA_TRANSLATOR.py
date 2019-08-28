'''

Данный скрипт предназначен для быстрой адаптации программистов из языка 1С. Рекомендуется прогонять через него все учебные примеры.

'''
import re


def ord_char(name_):
    if isinstance(name_, str):
        name_ = tuple(name_.strip())
        name_ = map(ord, name_)
        return tuple(name_)
    if isinstance(name_, tuple):
        name_ = map(lambda x: chr(x + 975), name_)
        name_ = ''.join(name_)
        return name_


func_pattern = re.compile(r'def +(\w+?)\((.*?)\)')  # паттерн для поиска имени функции
class_pattern = re.compile(r'class +(\w+)')  # паттерн для поиска имени класса
var_pattern = re.compile(r'^ *?(\w+?) *?.=')  # паттерн для поиска имени переменной
names = dict()  # словарь со всеми заменами имён: names['старое_имя'] = 'новое_имя'
cache_file = ''
original_file = input('Укажите путь до файла (.py), который вы хотите прокачать.\n')
with open(original_file, encoding='utf-8') as file:
    for line in file:
        if re.search(r' *?def +?', line):  # проверяем, является ли строка заданием функции
            func_name, func_args = func_pattern.findall(line)[0]
            if func_name not in names.keys() and not re.search(r'__\w+__', line):
                names[func_name] = ord_char(func_name)
            func_args = func_args.split(',')
            for arg in func_args:
                if '=' in arg:
                    arg = arg.split('=')[0]  # если у функци аттрибут со значением - значение и знак '=' отбрасываем
                arg = arg.strip()
                if arg not in names.keys() and arg != '*' and arg != '':
                    names[arg] = ord_char(arg)
        elif re.search(r' *?class +?', line):
            class_name = class_pattern.findall(line)[0]
            if class_name not in names.keys():
                names[class_name] = ord_char(class_name)
        elif var_pattern.findall(line):
            var_name = var_pattern.findall(line)[0]
            if var_name not in names.keys():
                names[var_name] = ord_char(var_name)
'''        print(line)
        for name in names.keys():
            if name in line:
                line = re.sub(r'(?<!\w)' + name + r'(?!\w)', names[name], line)   #эту часть кода можно доработать
        print(line)                                                               #чтобы лишний раз не открывать файл
        cache_file += line'''                                                     #и не проходить по нему

with open(original_file, encoding='utf-8') as file:
    for line in file:
        for name in names.keys():
            if name in line:
                line = re.sub(r'(?<!\w)' + name + r'(?!\w)', ord_char(names[name]), line)
        cache_file += line


with open('BRAND_NEW_SCRIPT_9000.py', mode='w', encoding='utf-8') as new_file:
    new_file.write(cache_file)
    print('тВоЙ нОвЫй ФаЙлИк гОтОв :***')
