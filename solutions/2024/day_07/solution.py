# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from collections.abc import Callable, Iterable
from functools import partial
from operator import add, mul

from pipe import select, where

from ...base import StrSplitSolution, answer


class Calibration:
    def __init__(self, line: str) -> None:
        parts = line.split(" ")
        self.value = int(parts[0][:-1])
        self.terms = tuple(map(int, parts[1:]))

    def __repr__(self) -> str:
        return f"<Calibration value={self.value} terms={self.terms}>"


def parse_line(line: str) -> Calibration:
    return line.splitlines()


def possible_values(terms: tuple[int, ...], operations: Iterable[Callable[[int, int], int]]) -> Iterable[int]:
    if len(terms) == 1:
        yield terms[0]
        return
    for operation in operations:
        yield from possible_values((operation(terms[0], terms[1]), *terms[2:]), operations)


def can_resolve(calibration: Calibration, operations: Iterable[Callable[[int, int], int]]) -> bool:
    p = tuple(possible_values(calibration.terms, operations))
    return calibration.value in p


def get_value(calibration: Calibration) -> int:
    return calibration.value


def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))


class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    @answer(2437272016585)
    def part_1(self) -> int:
        check = partial(can_resolve, operations=(add, mul))
        return sum(self.input | select(Calibration) | where(check) | select(get_value))

    @answer(162987117690649)
    def part_2(self) -> int:
        check = partial(can_resolve, operations=(add, mul, concatenate))
        return sum(self.input | select(Calibration) | where(check) | select(get_value))
