# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2


from collections.abc import Iterable
from itertools import pairwise

from pipe import select

from solutions.base import StrSplitSolution, answer


def count(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


def parse_ints(s: str) -> tuple[int, int, int, int, int]:
    return tuple(map(int, s.split()))


def is_safe_ascending(first: int, second: int) -> bool:
    return second - 3 <= first < second <= first + 3


def is_safe_descending(first: int, second: int) -> bool:
    return is_safe_ascending(second, first)


def is_safe(level: tuple[int, int, int, int, int]) -> bool:
    return all(is_safe_ascending(a, b) for a, b in pairwise(level)) or all(
        is_safe_descending(a, b) for a, b in pairwise(level)
    )


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(639)
    def part_1(self) -> int:
        return count(filter(is_safe, self.input | select(parse_ints)))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
