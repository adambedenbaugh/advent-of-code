

filename = "data_2a_full.txt"
with open(filename) as f:
    content = f.readlines()


def is_saft(arr):
    increase = arr[1] > arr[0]
    if increase:
        for i in range(1, len(arr)):
            inner_diff = arr[i] - arr[i-1]
            if not 1 <= inner_diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(arr)):
            inner_diff = arr[i] - arr[i-1]
            if not -3 <= inner_diff <= -1:
                return False
        return True


def is_saft_with_dampener(arr):
    if is_saft(arr):
        return True
    for i in range(len(arr)):
        if is_saft(arr[:i] + arr[i+1:]):
            return True
    return False


# Part 1
saft = 0
for line in content:
    report = [int(x) for x in line.split()]
    saft += is_saft(report)

print(f'First Half safe:  {saft}')

# Part 2
saft = 0
for line_number, line in enumerate(content):
    report = [int(x) for x in line.split()]
    saft += is_saft_with_dampener(report)

print(f'Second Half saft: {saft}')