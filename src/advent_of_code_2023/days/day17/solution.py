"""
"""

import heapq

import numpy as np

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 17, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> np.ndarray:
        """ """
        return np.array([[int(x) for x in line] for line in input_data.splitlines()])

    def min_heat_loss(
        self: "DaySolution", edges: np.ndarray, least: int = 1, most: int = 3
    ) -> int:
        queue = [(0, 0, 0, 0, 0)]
        seen = set()
        while queue:
            heat, x, y, px, py = heapq.heappop(queue)
            if (x, y) == (edges.shape[0] - 1, edges.shape[1] - 1):
                return heat
            if (x, y, px, py) in seen:
                continue
            seen.add((x, y, px, py))
            # calculate turns only
            for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(px, py), (-px, -py)}:
                a, b, h = x, y, heat
                # enter 4-10 moves in the chosen direction
                for i in range(1, most + 1):
                    a, b = a + dx, b + dy
                    if 0 <= a < edges.shape[0] and 0 <= b < edges.shape[1]:
                        h += edges[a, b]
                        if i >= least:
                            heapq.heappush(queue, (h, a, b, dx, dy))
        return 0

    def _solve_part1(self: "DaySolution", parsed_data: np.ndarray) -> str:
        """ """
        return str(self.min_heat_loss(parsed_data))

    def _solve_part2(self: "DaySolution", parsed_data: np.ndarray) -> str:
        """ """
        return str(self.min_heat_loss(parsed_data, 4, 10))
