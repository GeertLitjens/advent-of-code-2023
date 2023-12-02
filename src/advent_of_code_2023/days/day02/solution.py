"""
"""

import re

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 2, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[str]:
        """ """
        return input_data.splitlines()

    def _solve_part1(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        valid_game_ids = []
        (reds, greens, blues) = (12, 13, 14)
        for game in parsed_data:
            game_id = int(re.findall(r"Game (\d+)", game)[0])
            grabs = game.split(":")[1].split(";")
            valid = True
            for grab in grabs:
                red_blocks = re.findall(r"(\d+) red", grab)
                green_blocks = re.findall(r"(\d+) green", grab)
                blue_blocks = re.findall(r"(\d+) blue", grab)
                if (
                    (red_blocks and int(red_blocks[0]) > reds)
                    or (green_blocks and int(green_blocks[0]) > greens)
                    or (blue_blocks and int(blue_blocks[0]) > blues)
                ):
                    valid = False
                    break
            if valid:
                valid_game_ids.append(game_id)
        return str(sum(valid_game_ids))

    def _solve_part2(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        total_power = 0
        for game in parsed_data:
            grabs = game.split(":")[1].split(";")
            max_red, max_blue, max_green = (0, 0, 0)
            for grab in grabs:
                red_blocks = re.findall(r"(\d+) red", grab)
                green_blocks = re.findall(r"(\d+) green", grab)
                blue_blocks = re.findall(r"(\d+) blue", grab)
                if red_blocks and int(red_blocks[0]) > max_red:
                    max_red = int(red_blocks[0])
                if green_blocks and int(green_blocks[0]) > max_green:
                    max_green = int(green_blocks[0])
                if blue_blocks and int(blue_blocks[0]) > max_blue:
                    max_blue = int(blue_blocks[0])
            total_power += max_red * max_green * max_blue
        return str(total_power)
