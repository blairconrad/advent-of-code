# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1
from itertools import islice
from typing import TYPE_CHECKING

from pipe import Pipe, select, sort

from ...base import StrSplitSolution, answer
from ...utils.iterables import starmap
from ...utils.parsing import split_ints

if TYPE_CHECKING:
    from collections.abc import Iterable


def count(target: int, iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable if i == target)


def nth(n: int) -> int:
    return lambda it: next(islice(it, n, None), None)


def abs_diff(a: int, b: int) -> int:
    return abs(a - b)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2031679)
    def part_1(self) -> int:
        location_ids = list(self.input | split_ints)
        self.debug(f"{location_ids=}")
        left_column = location_ids | select(nth(0)) | sort
        right_column = location_ids | select(nth(1)) | sort
        self.debug(left_column)
        return zip(left_column, right_column, strict=False) | starmap(abs_diff) | Pipe(sum)

    @answer(19678534)
    def part_2(self) -> int:
        location_ids = list(self.input | split_ints)
        left_column = location_ids | select(nth(0))
        right_column = list(location_ids | select(nth(1)))
        return left_column | select(lambda n: n * count(n, right_column)) | Pipe(sum)
