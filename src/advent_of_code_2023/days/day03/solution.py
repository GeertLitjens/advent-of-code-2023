"""
"""
import re
from collections import defaultdict
from math import prod

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 3, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[str]:
        """ """
        return input_data.splitlines()

    def get_engine_parts(
        self: "DaySolution", parsed_data: list[str]
    ) -> defaultdict[tuple[int, int], list[int]]:
        rows, cols = len(parsed_data), len(parsed_data[0])
        engine_parts = defaultdict(list)
        symbol_locations = {
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if parsed_data[r][c] not in "0123456789."
        }
        for r, row in enumerate(parsed_data):
            for digit in re.finditer(r"\d+", row):
                neighbors = {
                    (r + s, c + d)
                    for s in (-1, 0, 1)
                    for d in (-1, 0, 1)
                    for c in range(*digit.span())
                }
                for correct_position in neighbors & symbol_locations:
                    engine_parts[correct_position].append(int(digit[0]))
        return engine_parts

    def _solve_part1(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        engine_parts = self.get_engine_parts(parsed_data)
        return str(sum(sum(part) for part in engine_parts.values()))

    def _solve_part2(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        engine_parts = self.get_engine_parts(parsed_data)
        return str(sum([prod(x) for x in engine_parts.values() if len(x) == 2]))
