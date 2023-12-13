"""
"""

import numpy as np

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 13, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[np.ndarray]:
        """ """
        return [
            np.array(
                [[0 if x == "." else 1 for x in row] for row in block.splitlines()]
            )
            for block in input_data.split("\n\n")
        ]

    def _solve_part1(self: "DaySolution", parsed_data: list[np.ndarray]) -> str:
        """ """
        score = 0
        for block in parsed_data:
            # Check vertical symmetry
            for i in range(1, block.shape[1]):
                left = block[:, :i]
                flipped_left = np.flip(left, axis=1)
                concat = np.concatenate([left, flipped_left], axis=1)
                if concat.shape[1] < block.shape[1]:
                    if np.all(concat == block[:, : concat.shape[1]]):
                        score += i
                        break
                else:
                    if np.all(concat[:, : block.shape[1]] == block):
                        score += i
                        break
            for i in range(1, block.shape[0]):
                top = block[:i]
                flipped_top = np.flip(top, axis=0)
                concat = np.concatenate([top, flipped_top], axis=0)
                if concat.shape[0] < block.shape[0]:
                    if np.all(concat == block[: concat.shape[0]]):
                        score += i * 100
                        break
                else:
                    if np.all(concat[: block.shape[0]] == block):
                        score += i * 100
                        break
        return str(score)

    def _solve_part2(self: "DaySolution", parsed_data: list[np.ndarray]) -> str:
        """ """
        score = 0
        for block in parsed_data:
            # Check vertical symmetry
            for i in range(1, block.shape[1]):
                left = block[:, :i]
                flipped_left = np.flip(left, axis=1)
                concat = np.concatenate([left, flipped_left], axis=1)
                if concat.shape[1] < block.shape[1]:
                    if np.sum(concat != block[:, : concat.shape[1]]) == 1:
                        score += i
                        break
                else:
                    if np.sum(concat[:, : block.shape[1]] != block) == 1:
                        score += i
                        break
            for i in range(1, block.shape[0]):
                top = block[:i]
                flipped_top = np.flip(top, axis=0)
                concat = np.concatenate([top, flipped_top], axis=0)
                if concat.shape[0] < block.shape[0]:
                    if np.sum(concat != block[: concat.shape[0]]) == 1:
                        score += i * 100
                        break
                else:
                    if np.sum(concat[: block.shape[0]] != block) == 1:
                        score += i * 100
                        break
        return str(score)
