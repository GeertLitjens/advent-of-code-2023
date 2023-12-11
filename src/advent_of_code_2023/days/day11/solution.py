"""
"""

import numpy as np

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 11, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> np.ndarray[str]:
        """ """
        glx_mp = np.array([[x for x in line] for line in input_data.splitlines()])
        return glx_mp

    def calculate_shortest_paths(
        self: "DaySolution", glx_mp: np.ndarray[str], multiplier: int = 2
    ) -> int:
        empty_rows, empty_cols = set(), set()
        for i in range(glx_mp.shape[0]):
            if "#" not in glx_mp[i]:
                empty_rows.add(i)
        for i in range(glx_mp.shape[1]):
            if "#" not in glx_mp[:, i]:
                empty_cols.add(i)
        glx_rows, glx_cols = np.where(glx_mp == "#")
        dist_mat = np.zeros((len(glx_rows), len(glx_rows)))
        for i, (row_i, col_i) in enumerate(zip(glx_rows, glx_cols, strict=True)):
            for j, (row_j, col_j) in enumerate(zip(glx_rows, glx_cols, strict=True)):
                if i >= j:
                    continue
                intersecting_rows = len(
                    set(range(min(row_i, row_j), max(row_i, row_j))).intersection(
                        empty_rows
                    )
                )
                intersecting_cols = len(
                    set(range(min(col_i, col_j), max(col_i, col_j))).intersection(
                        empty_cols
                    )
                )
                dist_mat[i, j] = (
                    np.abs(row_i - row_j)
                    + np.abs(col_i - col_j)
                    - intersecting_rows
                    - intersecting_cols
                    + multiplier * intersecting_rows
                    + multiplier * intersecting_cols
                )
        return int(np.sum(dist_mat))

    def _solve_part1(self: "DaySolution", parsed_data: np.ndarray[str]) -> str:
        """ """
        return str(self.calculate_shortest_paths(parsed_data))

    def _solve_part2(self: "DaySolution", parsed_data: np.ndarray[str]) -> str:
        """ """
        return str(self.calculate_shortest_paths(parsed_data, 1_000_000))
