filename = "data_5a_sample.txt"
# filename = "data_5_full.txt"


with open(filename) as f:
    ls = f.read().split("\n\n")



# Part 1

# seeds = ls[0].split(":")[1].strip().split()
seeds = list(map(int, ls[0].split(":")[1].strip().split()))
print(f"seeds: {seeds}")

# seed_range = [{int(seeds[i]): int(seeds[i + 1])} for i in range(0, len(seeds), 2)]

location_lookups = [line.split(":")[1].strip().split("\n") for line in ls[1:]]
print(f"mapper: {location_lookups}")

lowest_seed_soil = None
for seed in seeds:
    next_position = seed
    for location_lookup in location_lookups:
        for inner_map in location_lookup:
            source = int(inner_map.split()[1])
            range_of_seeds = int(inner_map.split()[2])
            if next_position in range(source, source + range_of_seeds):
                next_position = int(inner_map.split()[0]) + (next_position - source)
                break
    if lowest_seed_soil is None or next_position < lowest_seed_soil:
        lowest_seed_soil = next_position

print(f"lowest_seed_soil: {lowest_seed_soil}")
