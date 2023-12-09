"""
"""
import numpy as np

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 9, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[int]]:
        """ """
        return [[int(x) for x in line.split(" ")] for line in input_data.splitlines()]

    def _solve_part1(self: "DaySolution", parsed_data: list[list[int]]) -> str:
        """ """
        total = 0
        for history in parsed_data:
            diff_sum: int = 1
            cur_seq = np.array(history)
            seqs = [cur_seq]
            while diff_sum != 0:
                cur_seq = np.diff(cur_seq)
                diff_sum = np.sum(cur_seq)
                seqs.append(cur_seq)
            exp_coef = 0
            for i in range(len(seqs) - 2, -1, -1):
                exp_coef = exp_coef + seqs[i][-1]
            total += exp_coef
        return str(total)

    def _solve_part2(self: "DaySolution", parsed_data: list[list[int]]) -> str:
        """ """
        total = 0
        for history in parsed_data:
            diff_sum: int = 1
            cur_seq = np.array(history)
            seqs = [cur_seq]
            while diff_sum != 0:
                cur_seq = np.diff(cur_seq)
                diff_sum = np.sum(cur_seq)
                seqs.append(cur_seq)
            exp_coef = 0
            for i in range(len(seqs) - 2, -1, -1):
                exp_coef = seqs[i][0] - exp_coef
            total += exp_coef
        return str(total)
