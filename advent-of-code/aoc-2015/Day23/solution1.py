list_of_instructions = tuple(instruction.rstrip() for instruction in open(r'puzzle_input', encoding='utf-8'))
print(list_of_instructions)

out_of_range = False
i = 0
a = 1
b = 0
i_changer = 1
while not out_of_range:
    print('i:', i)
    instruction = list_of_instructions[i]
    i_changer = 1
    if list_of_instructions[i] == 'hlf a':
        a //= 2
    elif list_of_instructions[i] == 'hlf b':
        b //= 2
    elif list_of_instructions[i] == 'tpl a':
        a *= 3
    elif list_of_instructions[i] == 'tpl b':
        b *= 3
    elif list_of_instructions[i] == 'inc a':
        a += 1
    elif list_of_instructions[i] == 'inc b':
        b += 1
    elif instruction.split()[0] == 'jmp':
        i_changer = int(instruction.split()[-1])
    elif instruction.split()[0] == 'jie':
        if (instruction.split()[1] == 'a,' and a % 2 == 0
        or  instruction.split()[1] == 'b,' and b % 2 == 0):
            i_changer = int(instruction.split()[-1])
    elif instruction.split()[0] == 'jio':
        if (instruction.split()[1] == 'a,' and a == 1
        or  instruction.split()[1] == 'b,' and b == 1):
            i_changer = int(instruction.split()[-1])
    i += i_changer
    print('a=', a, 'b=', b)
    if i not in range(len(list_of_instructions)):
        out_of_range = True
print(a)
