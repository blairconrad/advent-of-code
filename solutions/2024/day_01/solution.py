# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1
from collections.abc import Callable, Iterable
from itertools import starmap

from pipe import Pipe, select, sort

from ...base import StrSplitSolution, answer


@Pipe
def my_starmap(iterable: Iterable[tuple[int, int]], func: Callable[[tuple[int, int]], int]) -> Iterable[int]:
    return starmap(func, iterable)


def first(iterable: tuple[int]) -> int:
    return iterable[0]


def second(iterable: tuple[int]) -> int:
    return iterable[1]


def abs_diff(a: int, b: int) -> int:
    return abs(a - b)


def parse_int_pair(s: str) -> tuple[int, int]:
    return tuple(map(int, s.split()))


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2031679)
    def part_1(self) -> int:
        location_ids = list(self.input | select(parse_int_pair))
        self.debug(location_ids)
        column_1 = location_ids | select(first) | sort
        column_2 = location_ids | select(second) | sort
        self.debug(column_1)
        return zip(column_1, column_2, strict=False) | my_starmap(abs_diff) | Pipe(sum)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
