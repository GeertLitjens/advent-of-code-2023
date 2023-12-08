import pytest

from advent_of_code_2023.days.day06.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """\
Time:      7  15   30
Distance:  9  40  200\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "288"


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == "71503"
