import re


def transform(operation):
    operation = operation.replace('AND', '&')
    operation = operation.replace('OR', '|')
    operation = operation.replace('LSHIFT', '<<')
    operation = operation.replace('RSHIFT', '>>')
    operation = operation.replace('NOT', '~')
    operation = operation.replace('RSHIFT', '>>')
    name = re.search(r'\w+$', line).group(0)
    operation = re.sub(r' ->.*', r'', operation).rstrip()
    operation = re.sub(r' ->.*', r'', operation)
    operation = re.sub(r'([a-z]+)', r"var['\1']", operation)
    return name, operation


var= {re.search(r'\w+$', line).group(0): 0 for line in open(r'D:\PyCharm projects\Advent_of_code_2015\Day7\puzzle_input', encoding='utf-8')}
cache = {}

while cache != var:
    cache = var.copy()
    for line in open(r'D:\PyCharm projects\Advent_of_code_2015\Day7\puzzle_input', encoding='utf-8'):
        name, operation = transform(line)
        var[name] = eval(operation)

print(var['a'])
