from argparse import ArgumentParser, ArgumentTypeError
from typing import NamedTuple
from sys import exit


class Arguments(NamedTuple):
    a: int
    b: int
    c: int


def positive_int(value: str) -> int:
    try:
        new_value: int = int(value)
    except ValueError:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    if new_value < 0:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    return new_value


def parse_args() -> Arguments:
    parse = ArgumentParser(usage="%(prog)s\n\t./main a b c")
    parse.add_argument("a", type=positive_int, help="argument value, positive integer")
    parse.add_argument("b", type=positive_int, help="argument value, positive integer")
    parse.add_argument("c", type=positive_int, help="argument value, positive integer")

    try:
        args = parse.parse_args()
    except SystemExit:
        exit(84)

    return Arguments(args.a, args.b, args.c)
