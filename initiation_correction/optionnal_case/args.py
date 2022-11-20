from argparse import ArgumentParser, ArgumentTypeError
from typing import NamedTuple, Union
from sys import exit, argv


class Vector2int(NamedTuple):
    x: int
    y: int


class Arguments(NamedTuple):
    a: int
    option: Union[int, Vector2int]


def positive_int(value: str) -> int:
    try:
        new_value: int = int(value)
    except ValueError:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    if new_value < 0:
        raise ArgumentTypeError(f"{new_value} is not a positive integer")
    return new_value


def parse_args() -> Arguments:
    parse = ArgumentParser(usage="%(prog)s\n\t./main a [n | x y]")
    parse.add_argument("a", type=positive_int, help="argument value, positive integer")
    parse.add_argument(
        "--size",
        metavar=("n"),
        type=positive_int,
        help="size of the square",
    )
    parse.add_argument(
        "--pos",
        nargs=2,
        metavar=("x", "y"),
        type=positive_int,
        help="position of the square",
    )

    args = argv[1:]
    if len(args) == 2:
        args.insert(1, "--size")
    elif len(args) == 3:
        args.insert(1, "--pos")

    try:
        parsed_args = parse.parse_args(args)
    except SystemExit:
        exit(84)

    if parsed_args.size is not None:
        return Arguments(parsed_args.a, parsed_args.size)
    if parsed_args.pos is not None:
        return Arguments(parsed_args.a, Vector2int(*parsed_args.pos))

    print("Error: No action passed")
    exit(84)
