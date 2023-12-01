import pytest

from advent_of_code_2023.days.day01.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> dict:
    return {
        "part1": """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet\
""",
        "part2": """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen\
""",
    }


def test_part1(day_testdata: dict[str, str]) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata["part1"])
    result = sol._solve_part1(parsed_data)
    assert result == "142"


def test_part2(day_testdata: dict[str, str]) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata["part2"])
    result = sol._solve_part2(parsed_data)
    assert result == "281"
