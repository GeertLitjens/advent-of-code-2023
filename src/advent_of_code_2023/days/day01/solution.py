"""
"""
import numpy as np

from advent_of_code_2023.utils import Solution


class DaySolution(Solution, list[str]):
    def __init__(self: "DaySolution", day: int = 1, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[str]:
        """ """
        return input_data.splitlines()

    def _solve_part1(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        artsy_calibration_values = parsed_data
        total = 0
        for c_v in artsy_calibration_values:
            real_calibration_value = ""
            for ch in c_v:
                if ch.isdigit():
                    real_calibration_value += ch
                    break
            for ch in reversed(c_v):
                if ch.isdigit():
                    real_calibration_value += ch
                    break
            total += int(real_calibration_value)
        return str(total)

    def _solve_part2(self: "DaySolution", parsed_data: list[str]) -> str:
        """ """
        search_terms = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]
        artsy_calibration_values = parsed_data
        total = 0
        for c_v in artsy_calibration_values:
            real_calibration_value = ""
            matches_min = np.array([c_v.find(term) for term in search_terms])
            matches_max = np.array([c_v.rfind(term) for term in search_terms])
            loc_min = np.where(matches_min >= 0, matches_min, np.inf).argmin()
            loc_max = matches_max.argmax()
            if loc_min > 9:
                real_calibration_value += search_terms[loc_min]
            else:
                real_calibration_value += search_terms[loc_min + 10]
            if loc_max > 9:
                real_calibration_value += search_terms[loc_max]
            else:
                real_calibration_value += search_terms[loc_max + 10]
            total += int(real_calibration_value)
        return str(total)
