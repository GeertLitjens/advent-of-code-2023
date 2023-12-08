import pytest

from advent_of_code_2023.days.day08.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)\
"""


@pytest.fixture
def day_testdata_2() -> str:
    return """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "6"


def test_part2(day_testdata_2: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata_2)
    result = sol._solve_part2(parsed_data)
    assert result == "6"
