'''
To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083.
'''

row = 1
column = 1
code = 20151125
while row != 2978 or column != 3083:
    code = (code * 252533) % 33554393
    if row == 1:
        row = column + 1
        column = 1
    else:
        row -= 1
        column += 1
   # print('row:', row, 'column:', column)
   # print('code:', code)
   # input()
print(code)
