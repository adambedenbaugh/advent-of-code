filename = "data_1a_full.txt"

with open(filename) as f:
    content = f.readlines()

left_list = []
right_list = []

for line in content:
    numbers = line.split()
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))

sum = 0
for i in range(len(left_list)):
    distance = right_list[i] - left_list[i]
    sum += abs(distance)

print(f'part 1a: {sum}')

sum = 0
for i in range(len(left_list)):
    sum += left_list[i] * right_list.count(left_list[i])

print(f'part 1b: {sum}')