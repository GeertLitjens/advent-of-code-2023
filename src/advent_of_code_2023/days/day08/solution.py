"""
"""
from math import lcm

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 8, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(
        self: "DaySolution", input_data: str
    ) -> tuple[str, dict[str, list[str]]]:
        """ """
        instr, node_map = input_data.split("\n\n")
        node_dct: dict[str, list[str]] = {}
        for node in node_map.splitlines():
            base, conn = node.split(" = (")
            node_dct[base] = conn.replace(")", "").split(", ")
        return instr, node_dct

    def _solve_part1(
        self: "DaySolution", parsed_data: tuple[str, dict[str, list[str]]]
    ) -> str:
        """ """
        instr, node_dct = parsed_data
        cur_node = "AAA"
        steps = 0
        while cur_node != "ZZZ":
            for turn in instr:
                steps += 1
                if turn == "L":
                    cur_node = node_dct[cur_node][0]
                else:
                    cur_node = node_dct[cur_node][1]
        return str(steps)

    def _solve_part2(
        self: "DaySolution", parsed_data: tuple[str, dict[str, list[str]]]
    ) -> str:
        """ """
        instr, node_dct = parsed_data
        cur_nodes = [x for x in node_dct.keys() if x.endswith("A")]
        steps = [0] * len(cur_nodes)

        for i, cur_node in enumerate(cur_nodes):
            while not cur_node.endswith("Z"):
                for turn in instr:
                    steps[i] += 1
                    if turn == "L":
                        cur_node = node_dct[cur_node][0]
                    else:
                        cur_node = node_dct[cur_node][1]
        return str(lcm(*steps))
