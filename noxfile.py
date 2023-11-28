# type: ignore
import tempfile

import nox  # pyright: ignore
from nox_poetry import Session, session  # pyright: ignore

nox.options.sessions = "lint", "mypy", "safety", "tests"
locations = "src", "tests"
package = "advent_of_code_2023"


@session(python=["3.11", "3.8"])
def tests(session: Session) -> None:
    session.install("pytest", "coverage[toml]", "pytest-cov", ".")
    session.run("pytest", "--cov")


@session(python=["3.10", "3.8"])
def lint(session: Session) -> None:
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-isort",
    )
    session.run("flake8", *args)


@session(python="3.11")
def black(session: Session) -> None:
    args = session.posargs or locations
    args += ("--extend-exclude", "day_template")
    session.install("black")
    session.run("black", *args)


@session(python=["3.11", "3.8"])
def mypy(session: Session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@session(python="3.8")
def safety(session: Session) -> None:
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@session(python=["3.11", "3.8"])
def typeguard(session: Session) -> None:
    args = session.posargs or ["-m", "not e2e"]
    session.install("pytest", "pytest-mock", "typeguard", ".")
    session.run("pytest", f"--typeguard-packages={package}", *args)
