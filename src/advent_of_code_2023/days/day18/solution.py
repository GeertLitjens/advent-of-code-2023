"""
"""

import numpy as np

from advent_of_code_2023.utils import Solution


def shoelace(x_y: list[tuple[int, int]]) -> float:
    x_y_arr = np.array(x_y)
    x_y_arr = x_y_arr.reshape(-1, 2)

    x = x_y_arr[:, 0]
    y = x_y_arr[:, 1]

    S1 = np.sum(x * np.roll(y, -1))
    S2 = np.sum(y * np.roll(x, -1))

    area = 0.5 * np.absolute(S1 - S2)

    return area


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 18, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[str]]:
        """ """
        return [
            line.replace("(", "").replace(")", "").split(" ", 3)
            for line in input_data.splitlines()
        ]

    def _solve_part1(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        polygon = [(0, 0)]
        bound_length = 0
        for line in reversed(parsed_data):
            dr, lngth, _ = line
            bound_length += int(lngth)
            match dr:
                case "R":
                    polygon.append((polygon[-1][0], polygon[-1][1] + int(lngth)))
                case "U":
                    polygon.append((polygon[-1][0] - int(lngth), polygon[-1][1]))
                case "D":
                    polygon.append((polygon[-1][0] + int(lngth), polygon[-1][1]))
                case "L":
                    polygon.append((polygon[-1][0], polygon[-1][1] - int(lngth)))
        return str(int(shoelace(polygon) + bound_length // 2 + 1))

    def _solve_part2(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        polygon = [(0, 0)]
        bound_length = 0
        nr_to_dr = {"0": "R", "1": "D", "2": "L", "3": "U"}
        for line in reversed(parsed_data):
            _, _, code = line
            lngth = int(code[1:-1], 16)
            bound_length += int(lngth)
            match nr_to_dr[code[-1]]:
                case "R":
                    polygon.append((polygon[-1][0], polygon[-1][1] + int(lngth)))
                case "U":
                    polygon.append((polygon[-1][0] - int(lngth), polygon[-1][1]))
                case "D":
                    polygon.append((polygon[-1][0] + int(lngth), polygon[-1][1]))
                case "L":
                    polygon.append((polygon[-1][0], polygon[-1][1] - int(lngth)))
        return str(int(shoelace(polygon) + bound_length // 2 + 1))
