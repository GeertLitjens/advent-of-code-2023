"""
"""

import re

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 15, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[str]:
        """ """
        return input_data.replace("\n", "").split(",")

    def box_hash(self: "DaySolution", string: str) -> int:
        cur_code = 0
        for c in string:
            cur_code += ord(c)
            cur_code *= 17
            cur_code %= 256
        return cur_code

    def _solve_part1(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        return str(sum([self.box_hash(inst) for inst in parsed_data]))

    def _solve_part2(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        boxes: list[list[str]] = [[] for x in range(256)]
        for inst in parsed_data:
            box_code, rest = re.split("-|=", inst)
            box_nr = self.box_hash(box_code)
            if "-" in inst:
                for i, lens in enumerate(boxes[box_nr]):
                    if box_code in lens:
                        boxes[box_nr].remove(boxes[box_nr][i])
            else:
                if any(lens_loc := [box_code in lens for lens in boxes[box_nr]]):
                    boxes[box_nr][lens_loc.index(True)] = box_code + " " + rest
                else:
                    boxes[box_nr].append(box_code + " " + rest)
        focussing_power = 0
        for i, box in enumerate(boxes):
            for j, lens in enumerate(box):
                _, ls = lens.split(" ")
                focussing_power += (i + 1) * (j + 1) * (int(ls))
        return str(focussing_power)
