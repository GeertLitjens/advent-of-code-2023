import importlib
import logging
import os
import shutil
import sys
import typing
from pathlib import Path

import click

from . import __version__
from .utils import ColorLogger


@click.group()
@click.option("--debug/--no-debug", help="Provide more debug logging", default=False)
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx: click.Context, debug: bool) -> None:
    """
    Solution of the Advent of Code 2023 as implemented by Geert Litjens in Python
    """
    logging.setLoggerClass(ColorLogger)
    logger = logging.getLogger("aoclogger")
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    ctx.obj = logger


@cli.command()
@click.argument(
    "days",
    nargs=-1,
    required=False,
    type=click.STRING,
)
@click.option(
    "-t",
    "--token",
    required=False,
    type=click.STRING,
    default="",
    help="The AoC token to access inputs and submit results. Can also be specified as an \
          an enviromental variable AOC_TOKEN",
)
@click.option(
    "-s",
    "--submit/--no-submit",
    required=False,
    type=click.BOOL,
    default=False,
    help="Submit results for specified days to AoC.",
)
@click.option(
    "-b",
    "--blog/--no-blog",
    required=False,
    type=click.BOOL,
    default=False,
    help="Generate the blog page for the specified days.",
)
@click.pass_obj
def run(
    logger: logging.Logger,
    days: list[str],
    token: str,
    submit: bool,
    blog: bool,
) -> None:
    """
    Run a specific set of days, default is all days. If you want to run
    a specific part of a day, specify an a or a b after the day number
    (e.g. 11a, 12b)
    """
    if token:
        os.environ["AOC_TOKEN"] = token
    elif os.path.exists(".aoc_token"):
        os.environ["AOC_TOKEN"] = Path(".aoc_token").read_text()

    day_fldrs = [
        x for x in os.listdir(Path(__file__).parent / "days") if "temp" not in x
    ]
    if not days:
        days = sorted([x.replace("day", "") for x in day_fldrs])

    logger.info("Started calculating solutions for days: " + str(days))
    for day_nr in days:
        part = ""
        if not str(day_nr)[-1].isdigit():
            part = day_nr[-1]
            day_nr = day_nr[:-1]
        day_module = importlib.import_module(
            "advent_of_code_2023.days.day" + str(day_nr).zfill(2)[:2] + ".solution"
        )
        solution = day_module.DaySolution()
        if part:
            if part == "a":
                solution.solve(True, False)
            else:
                solution.solve(False, True)
        else:
            solution.solve()
        if submit:
            solution.submit()
        if blog:
            solution.generate_day_md()


@cli.command()
@click.argument(
    "days",
    nargs=-1,
    required=True,
    type=click.INT,
)
@click.option(
    "--overwrite/--no-overwrite",
    help="Overwrite the old day codes, carefull!",
    default=False,
)
@click.pass_obj
def create(logger: logging.Logger, days: typing.List[int], overwrite: bool) -> None:
    """Create template folder for different days."""
    for day in days:
        logger.info(f"Creating structure for day {day}")
        in_path = Path(__file__).parent / "days" / "day_template"
        out_path = Path(__file__).parent / "days" / f"day{int(day):02d}"
        out_solution_path = (
            Path(__file__).parent / "days" / f"day{day:02d}" / "solution.py"
        )
        out_test_path = (
            Path(__file__).parent / "days" / f"day{day:02d}/test_day_template.py"
        )
        test_path = Path(__file__).parent.parent.parent / f"tests/test_day{day:02d}.py"
        logger.debug(f"Input path {in_path}")
        logger.debug(f"Output path {out_path}")
        logger.debug(f"Original test path {out_test_path}")
        logger.debug(f"Move test path {test_path}")

        if overwrite and out_path.exists() and test_path.exists():
            shutil.rmtree(out_path)
            os.remove(test_path)
        try:
            shutil.copytree(in_path, out_path)
            out_solution_path.write_text(
                out_solution_path.read_text().replace("<DAY_NUMBER>", str(day))
            )
            test_path.write_text(
                out_test_path.read_text().replace("<DAY_NUMBER>", str(day).zfill(2))
            )
            os.remove(out_test_path)
            logger.log(25, "Successfully created folder and tests.")
        except OSError:
            logger.error(f"Failed to create the folder for day {day}.")


if __name__ == "__main__":
    cli(sys.argv[1:])
