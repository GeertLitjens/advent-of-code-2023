import pytest

from advent_of_code_2023.days.day09.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "114"


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == "2"
