#!/usr/bin/env python

import argparse

TEMPLATE = """def solve(data: str) -> None:
    pass


if __name__ == "__main__":
    import example
    solve(example.get({}))
"""


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2025 Solver")
    sub = parser.add_subparsers()

    cmd_prepare = sub.add_parser("prepare", help="prepare input data files")
    cmd_prepare.set_defaults(func=prepare)

    cmd_solve = sub.add_parser("solve", help="solve the puzzle for a given day")
    cmd_solve.set_defaults(func=solve)
    grp_example = cmd_solve.add_mutually_exclusive_group()
    grp_example.add_argument(
        "-r",
        "--real",
        action="store_true",
        dest="real",
        default=True,
        help="use real input data (default)",
    )
    grp_example.add_argument(
        "-e",
        "--example",
        action="store_false",
        dest="real",
        help="use example input data",
    )

    parser.add_argument(
        "day",
        type=int,
        choices=range(1, 13),
        metavar="day",
        help="day of the Advent of Code (1-12)",
    )

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(e)


def prepare(arg: argparse.Namespace):
    import requests
    import os

    day: int = arg.day
    with open(f"{os.getenv("HOME", "")}/.adventofcode.session") as f:
        session = f.read().strip()

    with requests.get(
        f"https://adventofcode.com/2025/day/{day}/input",
        cookies={"session": session},
    ) as resp:
        if resp.status_code != 200:
            raise ConnectionError(
                f"Failed to fetch input data for day {day}: {resp.status_code} {resp.text}"
            )
        with open(f"input/{day:02d}.txt", "w") as f:
            f.write(resp.text)

    with open(f"day{day:02d}.py", "w") as f:
        f.write(TEMPLATE.format(day))


def solve(args: argparse.Namespace):
    import importlib
    import time

    day: int = args.day
    if args.real:
        from input import get
    else:
        from example import get

    data = get(day)
    solver = importlib.import_module(f"day{day:02d}")

    if hasattr(solver, "solve") and callable(getattr(solver, "solve")):
        start = time.perf_counter_ns()
        solver.solve(data)
        end = time.perf_counter_ns()
        print(f"Solved in {(end - start) / 1e6:.6f} ms.")
    else:
        raise NotImplementedError(f"No solve function found in module day{day:02d}.")


if __name__ == "__main__":
    main()
