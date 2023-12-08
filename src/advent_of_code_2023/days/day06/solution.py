"""
"""

import re
from math import ceil, floor

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 6, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[str]:
        """ """
        time_line, distance_line = input_data.splitlines()
        return [time_line, distance_line]

    def _solve_part1(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        times = [int(x) for x in re.findall(r"\d+", parsed_data[0])]
        distances = [int(x) for x in re.findall(r"\d+", parsed_data[1])]
        races = list(zip(times, distances, strict=True))
        total_options = 1
        for race in races:
            time, dist = race
            D = time**2 - 4 * (dist + 1)
            min_thresh = ceil((time - D ** (1 / 2)) / 2)
            max_thresh = floor((time + D ** (1 / 2)) / 2)
            total_options *= max_thresh - min_thresh + 1
        return str(total_options)

    def _solve_part2(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        time = int(re.findall(r"\d+", parsed_data[0].replace(" ", ""))[0])
        dist = int(re.findall(r"\d+", parsed_data[1].replace(" ", ""))[0])
        D = time**2 - 4 * (dist + 1)
        min_thresh = ceil((time - D ** (1 / 2)) / 2)
        max_thresh = floor((time + D ** (1 / 2)) / 2)
        return str(max_thresh - min_thresh + 1)
