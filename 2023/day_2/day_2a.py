from collections import defaultdict
# filename = "data-2a-sample.txt"
filename = "data-2-full.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")



# Part 1

max_game = {
    "red": 12,
    "green": 13,
    "blue": 14
}

valid_game_sum = 0
power_game_sum = 0

for line in ls:
    color_count = {}
    game = line.split(":")
    game_number = game[0].split(" ")[1]
    # print(game_number)
    game_data = game[1].split(";")
    color_count = defaultdict(int)
    valid_game = []
    for individual_game in game_data:
        game_blocks = individual_game.split(",")
        # print(game_blocks)
        for block in game_blocks:
            color = block.strip().split(" ")[1]
            count = int(block.strip().split(" ")[0])
            if count > color_count[color]:
                color_count[color] = count
        # print(color_count)
        if (color_count["red"] <= max_game["red"]
                and color_count["green"] <= max_game["green"]
                and color_count["blue"] <= max_game["blue"]):
            valid_game.append(True)
        else:
            valid_game.append(False)

    # print(valid_game)
    # print(color_count)
    if all(valid_game):
        # print(f"Valid game: {game_number}")
        valid_game_sum += int(game_number)
    power = (color_count["red"] * color_count["green"] * color_count["blue"])
    # print(f"Power: {power}")
    power_game_sum += power


print(f"Valid game sum: {valid_game_sum}") #2505
print(f"Power game sum: {power_game_sum}") #70265
