import hashlib, re

puzzle_input = 'yzbqklnj'
hash_puzzle = ''
counter = 0

while not re.search(r'^000000', hash_puzzle):
    counter += 1
    new_string = puzzle_input + str(counter)
    hash_puzzle = hashlib.md5(bytes(new_string, 'UTF-8')).hexdigest()
print(counter)