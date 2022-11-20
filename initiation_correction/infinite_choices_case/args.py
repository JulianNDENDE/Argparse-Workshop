from argparse import ArgumentParser, ArgumentTypeError
from typing import NamedTuple, List
from sys import exit


class Arguments(NamedTuple):
    function: str
    argsList: List[int]


def positive_int(value: str) -> int:
    try:
        new_value: int = int(value)
    except ValueError:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    if new_value < 0:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    return new_value


def parse_args() -> Arguments:
    parse = ArgumentParser(usage="%(prog)s\n\t./main [foo] [bar] [baz], xi...")
    parse.add_argument(
        "func", type=str, choices=["foo", "bar", "baz"], help="function to call"
    )
    parse.add_argument(
        "xi",
        type=positive_int,
        nargs="+",
        help="argument value, positive integer",
    )

    try:
        args = parse.parse_args()
    except SystemExit:
        exit(84)

    return Arguments(args.func, args.argsList)
