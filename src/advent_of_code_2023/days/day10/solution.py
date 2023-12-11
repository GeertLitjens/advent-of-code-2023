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
    def __init__(self: "DaySolution", day: int = 10, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(
        self: "DaySolution", input_data: str
    ) -> tuple[list[list[str]], tuple[int, int]]:
        """ """
        start_ind = input_data.index("S")
        tnls = [[x for x in line] for line in input_data.splitlines()]
        start_pos = (
            start_ind // (len(tnls[0]) + 1),
            tnls[start_ind // (len(tnls[0]) + 1)].index("S"),
        )
        return tnls, start_pos

    def parse_loop(
        self: "DaySolution", tnls: list[list[str]], start_pos: tuple[int, int]
    ) -> list[tuple[int, int]]:
        loop_seeds = [start_pos]
        dr = (1, 0)
        while True:
            start_pos = (start_pos[0] + dr[0], start_pos[1] + dr[1])
            pipe_dr = tnls[start_pos[0]][start_pos[1]]
            match pipe_dr:
                case "-" | "|":
                    dr = dr
                    loop_seeds.append(start_pos)
                case "F":
                    if dr[1] == -1:
                        dr = (1, 0)
                    else:
                        dr = (0, 1)
                    loop_seeds.append(start_pos)
                case "J":
                    if dr[1] == 1:
                        dr = (-1, 0)
                    else:
                        dr = (0, -1)
                    loop_seeds.append(start_pos)
                case "7":
                    if dr[1] == 1:
                        dr = (1, 0)
                    else:
                        dr = (0, -1)
                    loop_seeds.append(start_pos)
                case "L":
                    if dr[1] == -1:
                        dr = (-1, 0)
                    else:
                        dr = (0, 1)
                    loop_seeds.append(start_pos)
                case _:
                    loop_seeds.append(start_pos)
                    break
        return loop_seeds

    def _solve_part1(
        self: "DaySolution", parsed_data: tuple[list[list[str]], tuple[int, int]]
    ) -> str:
        """ """
        tnls, start_pos = parsed_data
        loop_seeds = self.parse_loop(tnls, start_pos)
        return str(len(loop_seeds) // 2)

    def _solve_part2(
        self: "DaySolution", parsed_data: tuple[list[list[str]], tuple[int, int]]
    ) -> str:
        """ """
        tnls, start_pos = parsed_data
        loop_seeds = self.parse_loop(tnls, start_pos)
        return str(
            int(shoelace(loop_seeds) - len(loop_seeds) // 2 + 1)
        )  # Pick's Theorem
