"""
"""

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 16, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[str]]:
        """ """
        return [[x for x in line] for line in input_data.splitlines()]

    def solve_maze(
        self: "DaySolution",
        maze: list[list[str]],
        start_beam: tuple[tuple[int, int], tuple[int, int]] = ((0, 0), (0, 1)),
    ) -> int:
        shape = (len(maze), len(maze[0]))
        beams = [start_beam]
        activated_tiles = [[0] * shape[1] for _ in range(shape[0])]
        visited_mirrors = []
        while beams:
            cur_beam = beams.pop()
            beam_pos, beam_dir = cur_beam
            while -1 < beam_pos[0] < shape[0] and -1 < beam_pos[1] < shape[1]:
                activated_tiles[beam_pos[0]][beam_pos[1]] = 1
                match maze[beam_pos[0]][beam_pos[1]]:
                    case "\\":
                        if [beam_pos, beam_dir] not in visited_mirrors:
                            visited_mirrors.append([beam_pos, beam_dir])
                            match beam_dir:
                                case (0, 1):
                                    beam_dir = (1, 0)
                                case (1, 0):
                                    beam_dir = (0, 1)
                                case (-1, 0):
                                    beam_dir = (0, -1)
                                case (0, -1):
                                    beam_dir = (-1, 0)
                        else:
                            break
                    case "/":
                        if [beam_pos, beam_dir] not in visited_mirrors:
                            visited_mirrors.append([beam_pos, beam_dir])
                            match beam_dir:
                                case (0, 1):
                                    beam_dir = (-1, 0)
                                case (1, 0):
                                    beam_dir = (0, -1)
                                case (-1, 0):
                                    beam_dir = (0, 1)
                                case (0, -1):
                                    beam_dir = (1, 0)
                        else:
                            break
                    case "|":
                        match beam_dir:
                            case (0, _):
                                beam_dir = (-1, 0)
                                beams.append((beam_pos, (1, 0)))
                    case "-":
                        match beam_dir:
                            case (_, 0):
                                beam_dir = (0, -1)
                                beams.append((beam_pos, (0, 1)))
                beam_pos = (beam_pos[0] + beam_dir[0], beam_pos[1] + beam_dir[1])
        return sum([sum(_) for _ in activated_tiles])

    def _solve_part1(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        return str(self.solve_maze(parsed_data))

    def _solve_part2(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        max_act_tiles = []
        for i in range(len(parsed_data[0])):
            max_act_tiles.append(self.solve_maze(parsed_data, ((0, i), (1, 0))))
            max_act_tiles.append(
                self.solve_maze(parsed_data, ((len(parsed_data) - 1, i), (-1, 0)))
            )
        for i in range(len(parsed_data)):
            max_act_tiles.append(self.solve_maze(parsed_data, ((i, 0), (0, 1))))
            max_act_tiles.append(
                self.solve_maze(parsed_data, ((i, len(parsed_data[0]) - 1), (0, -1)))
            )
        return str(max(max_act_tiles))
