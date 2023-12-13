"""
"""

import functools
import re

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 12, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(
        self: "DaySolution", input_data: str
    ) -> tuple[list[str], list[list[int]]]:
        """ """
        ht_spr = [x.split()[0] for x in input_data.splitlines()]
        brkn = [
            [int(x) for x in re.findall(r"(\d+)", line)]
            for line in input_data.splitlines()
        ]
        return ht_spr, brkn

    def solve_row(self: "DaySolution", hot_spr: str, brk: list[int]) -> int:
        @functools.cache
        def check_part(spr_i: int, grp_j: int, pos: int = 0) -> int:
            if spr_i == len(hot_spr):
                return grp_j == len(brk)

            if hot_spr[spr_i] in ".?":
                pos += check_part(spr_i + 1, grp_j)

            if grp_j < len(brk) and (spr_j := spr_i + brk[grp_j]) < len(hot_spr):
                if (
                    hot_spr[spr_i] in "#?"
                    and "." not in hot_spr[spr_i:spr_j]
                    and "#" not in hot_spr[spr_j]
                ):
                    pos += check_part(spr_j + 1, grp_j + 1)

            return pos

        return check_part(0, 0)

    def _solve_part1(
        self: "DaySolution", parsed_data: tuple[list[str], list[list[int]]]
    ) -> str:
        """ """
        ht_sprs, brkn = parsed_data

        return str(
            sum(
                [
                    self.solve_row(hot_spr + ".", brk)
                    for hot_spr, brk in zip(ht_sprs, brkn, strict=True)
                ]
            )
        )

    def _solve_part2(
        self: "DaySolution", parsed_data: tuple[list[str], list[list[int]]]
    ) -> str:
        """ """
        ht_sprs, brkn = parsed_data

        return str(
            sum(
                [
                    self.solve_row((hot_spr + "?") * 5, brk * 5)
                    for hot_spr, brk in zip(ht_sprs, brkn, strict=True)
                ]
            )
        )
