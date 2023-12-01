import inspect
import logging
import os
import sys
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, TypeVar

import requests
from colorama import Back, Fore, init

init(autoreset=True)
logging.addLevelName(25, "SUCCESS")

ParsedAoCData = TypeVar("ParsedAoCData")


class ColorFormatter(logging.Formatter):
    # Change this dictionary to suit your coloring needs!
    COLORS = {
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED + Back.WHITE,
        "DEBUG": Fore.BLUE,
        "INFO": Fore.WHITE,
        "SUCCESS": Fore.GREEN,
        "CRITICAL": Fore.RED + Back.WHITE,
    }

    def format(self: "ColorFormatter", record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, "")
        if color:
            record.name = color + record.name
            record.levelname = color + record.levelname
            record.msg = color + record.msg
        return logging.Formatter.format(self, record)


class ColorLogger(logging.Logger):
    def __init__(self: "ColorLogger", name: str) -> None:
        logging.Logger.__init__(self, name)
        color_formatter = ColorFormatter("%(message)s")
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)
        self.addHandler(console)


class Solution(ABC, Generic[ParsedAoCData]):
    def __init__(self: "Solution", day: int = 1, year: int = 2023) -> None:
        init()
        self._data_dir = Path.home() / ".aoc" / str(year)
        if not self._data_dir.exists():
            os.makedirs(self._data_dir)
        self._input_data_path = self._data_dir / f"{day}_input.txt"
        self._answers1_path = self._data_dir / f"{day}_answers1.txt"
        self._answers2_path = self._data_dir / f"{day}_answers2.txt"
        self._day = day
        self._year = year
        self._solution_part1: str = ""
        self._solution_part2: str = ""
        self._user_agent = {"User-Agent": "advent-of-code-data v1.1.0"}
        self._session_token = {"session": os.environ["AOC_TOKEN"]}
        self._logger = logging.getLogger("aoclogger")

    def _get_input_data(self: "Solution") -> str:
        if not self._input_data_path.exists():
            input_url = f"https://adventofcode.com/{self._year}/day/{self._day}/input"
            response = requests.get(
                url=input_url,
                cookies=self._session_token,
                headers=self._user_agent,
                timeout=10,
            )
            if response.ok:
                with open(self._input_data_path, "w") as f:
                    f.writelines(response.text)
            else:
                raise requests.ConnectionError()
        return self._input_data_path.read_text()

    @abstractmethod
    def _parse_data(self: "Solution", input_data: str) -> ParsedAoCData:
        pass

    @abstractmethod
    def _solve_part1(self: "Solution", parsed_data: ParsedAoCData) -> str:
        return ""

    @abstractmethod
    def _solve_part2(self: "Solution", parsed_data: ParsedAoCData) -> str:
        return ""

    def solve(
        self: "Solution", part1: bool = True, part2: bool = True
    ) -> tuple[str, str]:
        self._logger.info(f"Solving for day {self._day}")
        parse_start = time.time()
        parsed_data = self._parse_data(self._get_input_data())
        parse_end = time.time()
        self._logger.info(f"\tTime needed for parsing data: {parse_end - parse_start}s")
        if part1:
            part1_start = time.time()
            self._solution_part1 = self._solve_part1(parsed_data)
            part1_end = time.time()
            self._logger.info(f"\tSolution for part 1: {self._solution_part1}")
            self._logger.info(f"\tTime needed for part 1: {part1_end - part1_start}s")
            self._solution_part2 = ""
        if part2:
            part2_start = time.time()
            self._solution_part2 = self._solve_part2(parsed_data)
            part2_end = time.time()
            self._logger.info(f"\tSolution for part 2: {self._solution_part2}")
            self._logger.info(f"\tTime needed for part 2: {part2_end - part2_start}s")
        return self._solution_part1, self._solution_part2

    def submit(self: "Solution") -> None:
        answer_url = f"https://adventofcode.com/{self._year}/day/{self._day}/answer"
        if self._solution_part1:
            if self._answers1_path.exists():
                prev_answers1 = self._answers1_path.read_text().splitlines()
            else:
                prev_answers1 = []
            if not str(self._solution_part1) in prev_answers1:
                response = requests.post(
                    url=answer_url,
                    cookies=self._session_token,
                    headers=self._user_agent,
                    data={"level": 1, "answer": str(self._solution_part1)},
                    timeout=10,
                )
                if response.ok:
                    self._logger.debug("Response OK!")
                    self._check_answer(response.text)
                else:
                    self._logger.error("Failed ")
                prev_answers1.append(str(self._solution_part1))
                self._answers1_path.write_text("\n".join(prev_answers1))
            else:
                self._logger.warning(
                    "Answer for part 1 already given, not submitting again!"
                )
        if self._solution_part2:
            if self._answers2_path.exists():
                prev_answers2 = self._answers2_path.read_text().splitlines()
            else:
                prev_answers2 = []
            if not str(self._solution_part2) in prev_answers2:
                response = requests.post(
                    url=answer_url,
                    cookies=self._session_token,
                    headers=self._user_agent,
                    data={"level": 2, "answer": str(self._solution_part2)},
                    timeout=10,
                )
                if response.ok:
                    self._logger.debug("Response OK!")
                    self._check_answer(response.text)
                else:
                    self._logger.error("Failed ")
                prev_answers2.append(str(self._solution_part2))
                self._answers2_path.write_text("\n".join(prev_answers2))
            else:
                self._logger.warning(
                    "Answer for part 2 already given, not submitting again!"
                )

    def _check_answer(self: "Solution", response_text: str) -> None:
        if "That's the right answer" in response_text:
            self._logger.log(25, "\tYou answered correctly!")
        elif "Did you already complete it" in response_text:
            self._logger.warning("\tYou completed this part already!")
        else:
            self._logger.warning("\tYou gave the wrong answer!")

    def generate_day_md(self: "Solution") -> None:
        template_path = Path(__file__).parent / "template.md"
        with open(template_path, "r") as file:
            template = file.read()
        day_readme_path = (
            Path(__file__).parent / f"../days/day{str(self._day).zfill(2)}/README.md"
        )
        with open(day_readme_path, "r") as file:
            day_text = file.readlines()
        page_description = day_text[0].replace("## ", "")
        day_text_string = "".join(["> " + line for line in day_text[2:]])
        page_title = f"Day {self._day}"
        if self._parse_data.__doc__:
            aoc_parse_solution = " ".join(
                [x.lstrip() for x in self._parse_data.__doc__.split("\n")]
            )
        if self._solve_part1.__doc__:
            aoc_part1_solution = " ".join(
                [x.lstrip() for x in self._solve_part1.__doc__.split("\n")]
            )
        if self._solve_part2.__doc__:
            aoc_part2_solution = " ".join(
                [x.lstrip() for x in self._solve_part2.__doc__.split("\n")]
            )
        day_experience = sys.modules[self.__module__].__doc__
        aoc_part1_text, aoc_part2_text = day_text_string.split("> ### Part 2")
        aoc_parse_code = self._clean_code_for_md(
            inspect.getsourcelines(self._parse_data)[0]
        )
        aoc_part1_code = self._clean_code_for_md(
            inspect.getsourcelines(self._solve_part1)[0]
        )
        aoc_part2_code = self._clean_code_for_md(
            inspect.getsourcelines(self._solve_part2)[0]
        )
        replace_dict = {
            "<page_title>": page_title,
            "<page_description>": page_description,
            "<aoc_part1_solution>": aoc_part1_solution,
            "<aoc_parse_solution>": aoc_parse_solution,
            "<aoc_part2_solution>": aoc_part2_solution,
            "<day_experience>": day_experience,
            "<aoc_part1_text>": aoc_part1_text,
            "<aoc_part2_text>": aoc_part2_text,
            "<aoc_parse_code>": aoc_parse_code,
            "<aoc_part1_code>": aoc_part1_code,
            "<aoc_part2_code>": aoc_part2_code,
        }
        for key, value in replace_dict.items():
            if isinstance(value, str):
                template = template.replace(key, value)
        out_path = Path(__file__).parent / f"../../../docs/days/day{self._day}.md"
        with open(out_path, "w") as file:
            file.write(template)

        # Then adept the ToC
        toc_path = Path(__file__).parent / "../../../docs/index.md"
        toc_text, *rest = toc_path.read_text().split("## Solutions")
        toc_text += (
            "## Solutions\nHere you can find my solutions "
            "(on [GitHub](https://github.com/GeertLitjens/advent-of-code-2023) as well) "
            "for the different days:\n\n"
        )
        for day_md in range(
            len(os.listdir(Path(__file__).parent / "../../../docs/days"))
        ):
            toc_text += f"* [Day {day_md + 1}](./days/day{day_md + 1}.md)\n"
        toc_path.write_text(toc_text)

    @staticmethod
    def _clean_code_for_md(snippet: list[str]) -> str:
        leading_whitespace = len(snippet[0]) - len(snippet[0].lstrip(" "))
        snippet = [line[leading_whitespace:] for line in snippet]
        first_line_comment = 0
        last_line_comment = 0
        for i, line in enumerate(snippet):
            if line.lstrip().startswith('"""') and first_line_comment == 0:
                first_line_comment = i
            elif line.lstrip().startswith('"""') and first_line_comment > 0:
                last_line_comment = i
                break
        del snippet[first_line_comment : last_line_comment + 1]
        return "".join(snippet).rstrip()
