import pytest

from advent_of_code_2023.days.day15.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "1320"


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == "145"
