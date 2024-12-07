import re

filename = "data_3a_full.txt"

with open(filename) as f:
    content = f.read()


mul = r"mul\((\d{1,3}),(\d{1,3})\)"
do = r"do\(\)"
dont = r"don't\(\)"

# Part 1
sum = 0
res = re.finditer(mul, content)
for i in res:
    sum += int(i.group(1)) * int(i.group(2))

print(f'Part 1 sum: {sum}')

# Part 2
sum = 0
enable = True
for i in re.finditer(f'{do}|{dont}|{mul}', content):
    if re.fullmatch(do, i.group()):
        enable = True
    elif re.fullmatch(dont, i.group()):
        enable = False
    elif enable:
        sum += int(i.group(1)) * int(i.group(2))

print(f'Part 2 sum: {sum}')

