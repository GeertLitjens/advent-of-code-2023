"""
"""
import re

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 4, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[set[int]]]:
        """ """
        game_strings = input_data.splitlines()
        games = [
            [
                set(int(x[0]) for x in re.finditer(r"\d+", nrs))
                for nrs in line.split(":")[1].split("|")
            ]
            for line in game_strings
        ]
        return games

    def _solve_part1(self: "DaySolution", parsed_data: list[list[set[int]]]) -> str:
        """ """
        return str(
            sum(
                [
                    1 * 2 ** (matched_nrs - 1)
                    for game in parsed_data
                    if (matched_nrs := len(game[0].intersection(game[1]))) > 0
                ]
            )
        )

    def _solve_part2(self: "DaySolution", parsed_data: list[list[set[int]]]) -> str:
        """ """
        card_copies = [1] * len(parsed_data)
        for i, card in enumerate(parsed_data):
            matched_nrs = len(card[0].intersection(card[1]))
            for j in range(i + 1, min(i + matched_nrs + 1, len(card_copies))):
                card_copies[j] += card_copies[i]
        return str(sum(card_copies))
