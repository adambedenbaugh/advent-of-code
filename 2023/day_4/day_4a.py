import re

# filename = "data_4a_sample.txt"
filename = "data_4_full.txt"

with open(filename) as f:
    ls = f.read().split("\n")


def count_condition(_count):
    if _count == 0:
        return 0
    if _count == 1:
        return 1
    if _count > 1:
        return 2 ** (_count - 1)


def add_cards(_card, _card_to_add):
    number_of_cards[_card + _card_to_add] += number_of_cards[_card]


# Part 1

all_card_total = 0
number_of_cards = {x + 1: 1 for x in range(len(ls))}
print(f"number_of_cards: {number_of_cards}")

for line in ls:
    card = line.split(":")
    card_number = int(card[0].split()[1])
    winning_card = card[1].split("|")[0].strip().split()
    your_card = card[1].split("|")[1].strip().split()

    card_total = [x for x in your_card if x in winning_card]
    card_total_count = count_condition(len(card_total))
    all_card_total += card_total_count

    [add_cards(card_number, card_to_add + 1) for card_to_add in range(len(card_total))]


print(f"All Card Points Total: {all_card_total}")
print(f"All Card Copies Total: {sum(number_of_cards.values())}")