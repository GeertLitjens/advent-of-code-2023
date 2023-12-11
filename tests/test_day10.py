import pytest

from advent_of_code_2023.days.day10.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...\
"""


@pytest.fixture
def day_testdata2() -> str:
    return """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "8"


def test_part2(day_testdata2: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata2)
    result = sol._solve_part2(parsed_data)
    assert result == "10"
