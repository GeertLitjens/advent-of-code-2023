"""
"""

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 14, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[str]]:
        """ """
        return [[x for x in line] for line in input_data.splitlines()]

    def rotate(
        self: "DaySolution", mirrors: list[list[str]], dir: int = 1
    ) -> list[list[str]]:
        if dir == 1:
            return [list(x) for x in zip(*mirrors[::-1], strict=True)]
        else:
            return [list(x) for x in zip(*mirrors, strict=True)][::-1]

    def tilt_mirrors(self: "DaySolution", mirrors: list[list[str]]) -> list[list[str]]:
        tilted_mirrors = []
        for col in mirrors:
            tilted_pieces = [
                "O" * piece.count("O") + "." * (len(piece) - piece.count("O"))
                for piece in "".join(col).split("#")
            ]
            tilted_mirrors.append([x for x in "#".join(tilted_pieces)])
        return tilted_mirrors

    def _solve_part1(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        mirrors: list[list[str]] = self.rotate(parsed_data)
        tilted_mirrors = self.tilt_mirrors(mirrors)
        tilted_mirrors = self.rotate(tilted_mirrors)
        return str(
            sum(["".join(x).count("O") * (i + 1) for i, x in enumerate(tilted_mirrors)])
        )

    def _solve_part2(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        cache: dict[str, int] = {}
        scores = []
        mirrors = self.rotate(parsed_data, -1)
        for cycle in range(1_000_000_000):
            for _ in range(4):
                mirrors = self.tilt_mirrors(mirrors)
                mirrors = self.rotate(mirrors)

            mirrors = self.rotate(mirrors)
            str_mirrors = "\n".join(["".join(line) for line in mirrors])
            scores.append(
                sum(
                    [
                        "".join(x).count("O") * (len(mirrors) - i)
                        for i, x in enumerate(mirrors)
                    ]
                )
            )
            mirrors = self.rotate(mirrors, -1)

            if str_mirrors in cache:
                prev_cycle = cache[str_mirrors]
                cycle_length = cycle - prev_cycle
                req_cycle = prev_cycle + (1_000_000_000 - prev_cycle) % cycle_length - 1
                return str(scores[req_cycle])
            else:
                cache[str_mirrors] = cycle
        return "0"
