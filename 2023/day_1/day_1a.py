

filename = "data-1a-full.txt"

with open(filename) as f:
    content = f.readlines()

print(content)
sum = 0
for line in content:
    for i, char in enumerate(line):
        if char.isdigit():
            first_digit = int(char) * 10
            break
    for i, char in reversed(list(enumerate(line))):
        if char.isdigit():
            last_digit = int(char)
            break
    sum += first_digit + last_digit

print(sum)