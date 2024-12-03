# filename = "data_3_sample.txt"
filename = "data_3_full.txt"


with open(filename) as f:
    ls = f.read().strip().split("\n")


part_location = {}
parts = []
gears_ratio = []

def find_adjacent(row, column):
    print(f"row: {row}, column: {column}")
    offset = 0
    part = ""
    # print(part_location[row][column - offset])
    # print(part_location[row][column - offset].isnumeric())
    while part_location[row][column - offset].isnumeric() and column - offset >= 0:
        offset += 1
    print(f"    offset: {offset}")
    print(part_location[row][column - offset])
    while column - offset + 1 < len(part_location) and part_location[row][column - offset + 1].isnumeric():
        part += part_location[row][column - offset + 1]
        offset -= 1
    print(f"    part {part}")
    if part == "":
        return 0
    return int(part)

# Part 1
for row, line in enumerate(ls):
    # print(row)
    # print(line.isalnum())
    part_location[row] = []
    for i in line:
        part_location[row].append(i)


# look for symbols
for row in part_location:
    # print(row)
    for column, symbol in enumerate(part_location[row]):
        # print(column, symbol)
        if symbol.isalnum() is not True and symbol != ".":
            print(f"symbol: {part_location[row][column]}")
            # Look for adjacent numbers
            # Left?
            if part_location[row][column - 1].isalnum():
                print("  left")
                parts.append(find_adjacent(row, column - 1))

            # Right?
            if part_location[row][column + 1].isalnum():
                print("  right")
                parts.append(find_adjacent(row, column + 1))

            # # Top, left, center, right
            print("  top")
            top_set = set()
            if part_location[row - 1][column - 1].isalnum():
                top_set.add(find_adjacent(row - 1, column - 1))
            if part_location[row - 1][column].isalnum():
                top_set.add(find_adjacent(row - 1, column))
            if part_location[row - 1][column + 1].isalnum():
                top_set.add(find_adjacent(row - 1, column + 1))
            if len(top_set) > 0:
                for i in top_set:
                    parts.append(i)

            # # Bottom, left, center, right
            print("  bottom")
            bottom_set = set()
            # if row + 1 < len(part_location):
            if part_location[row + 1][column - 1].isalnum():
                bottom_set.add(find_adjacent(row + 1, column - 1))
            if part_location[row + 1][column].isalnum():
                bottom_set.add(find_adjacent(row + 1, column))
            if part_location[row + 1][column + 1].isalnum():
                bottom_set.add(find_adjacent(row + 1, column + 1))
            if len(bottom_set) > 0:
                for i in bottom_set:
                    parts.append(i)

        # Find the gear ratio
        if symbol == "*":
            # Left?
            gear_ratio_pair = []
            if part_location[row][column - 1].isalnum():
                print("  left")
                gear_ratio_pair.append(find_adjacent(row, column - 1))

            # Right?
            if part_location[row][column + 1].isalnum():
                print("  right")
                gear_ratio_pair.append(find_adjacent(row, column + 1))

            # # Top, left, center, right
            print("  top")
            top_set = set()
            if part_location[row - 1][column - 1].isalnum():
                top_set.add(find_adjacent(row - 1, column - 1))
            if part_location[row - 1][column].isalnum():
                top_set.add(find_adjacent(row - 1, column))
            if part_location[row - 1][column + 1].isalnum():
                top_set.add(find_adjacent(row - 1, column + 1))
            if len(top_set) > 0:
                for i in top_set:
                    gear_ratio_pair.append(i)

            # # Bottom, left, center, right
            print("  bottom")
            bottom_set = set()
            # if row + 1 < len(part_location):
            if part_location[row + 1][column - 1].isalnum():
                bottom_set.add(find_adjacent(row + 1, column - 1))
            if part_location[row + 1][column].isalnum():
                bottom_set.add(find_adjacent(row + 1, column))
            if part_location[row + 1][column + 1].isalnum():
                bottom_set.add(find_adjacent(row + 1, column + 1))
            if len(bottom_set) > 0:
                for i in bottom_set:
                    gear_ratio_pair.append(i)

            if len(gear_ratio_pair) == 2:
                gears_ratio.append(gear_ratio_pair[0] * gear_ratio_pair[1])






print(f"Part Sum: {parts}")
print(f"Part Sum: {sum(parts)}")

print(f"Gear Ratios: {gears_ratio}")
print(f"Gear Ratios: {sum(gears_ratio)}")