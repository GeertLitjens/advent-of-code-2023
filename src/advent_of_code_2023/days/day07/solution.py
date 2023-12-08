"""
"""

from collections import Counter

from advent_of_code_2023.utils import Solution

CARD_TO_VALUE = {
    "A": 0xE,
    "K": 0xD,
    "Q": 0xC,
    "J": 0xB,
    "T": 0xA,
    "9": 0x9,
    "8": 0x8,
    "7": 0x7,
    "6": 0x6,
    "5": 0x5,
    "4": 0x4,
    "3": 0x3,
    "2": 0x2,
}


def cmp(hand1: str) -> int:
    cntr: Counter[int] = Counter(Counter(hand1).values())
    hand_value: int = 0x0
    if 5 in cntr:
        hand_value += 0x600000
    elif 4 in cntr:
        hand_value += 0x500000
    elif 3 in cntr and 2 in cntr:
        hand_value += 0x400000
    elif 3 in cntr:
        hand_value += 0x300000
    elif 2 in cntr and cntr[2] == 2:
        hand_value += 0x200000
    elif 2 in cntr:
        hand_value += 0x100000
    multiplier = 0x10000
    for card in hand1:
        hand_value += CARD_TO_VALUE[card] * multiplier
        multiplier //= 0x10
    return hand_value


def cmp_2(hand1: str) -> int:
    CARD_TO_VALUE["J"] = 0x1
    card_amounts = Counter(hand1)
    if "J" in card_amounts.keys():
        jokers = card_amounts["J"]
        card_amounts["J"] = 0
        card_amounts[card_amounts.most_common(1)[0][0]] += jokers
    cntr: Counter[int] = Counter(card_amounts.values())
    hand_value: int = 0x0
    if 5 in cntr:
        hand_value += 0x600000
    elif 4 in cntr:
        hand_value += 0x500000
    elif 3 in cntr and 2 in cntr:
        hand_value += 0x400000
    elif 3 in cntr:
        hand_value += 0x300000
    elif 2 in cntr and cntr[2] == 2:
        hand_value += 0x200000
    elif 2 in cntr:
        hand_value += 0x100000
    multiplier = 0x10000
    for card in hand1:
        hand_value += CARD_TO_VALUE[card] * multiplier
        multiplier //= 0x10
    return hand_value


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 7, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[str]]:
        """ """
        hands = [x.split(" ") for x in input_data.splitlines()]
        return hands

    def _solve_part1(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        hands = parsed_data
        hands.sort(key=lambda x: cmp(x[0]))
        total_score = 0
        for i, hand in enumerate(hands):
            total_score += (i + 1) * int(hand[1])
        return str(total_score)

    def _solve_part2(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        hands = parsed_data
        hands.sort(key=lambda x: cmp_2(x[0]))
        total_score = 0
        for i, hand in enumerate(hands):
            total_score += (i + 1) * int(hand[1])
        return str(total_score)
