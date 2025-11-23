# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2


from itertools import count, islice, pairwise
from typing import TYPE_CHECKING

from pipe import select, take

from solutions.base import StrSplitSolution, answer

from ...utils.iterables import how_many

if TYPE_CHECKING:
    from collections.abc import Callable


def parse_ints(s: str) -> tuple[int, int, int, int, int]:
    return tuple(map(int, s.split()))


def is_safe_ascending(first: int, second: int) -> bool:
    return second - 3 <= first < second <= first + 3


def is_safe_descending(first: int, second: int) -> bool:
    return is_safe_ascending(second, first)


def nth(n: int) -> int:
    return lambda it: next(islice(it, n, None), None)


def is_safe(level: tuple[int, ...]) -> bool:
    return all(is_safe_ascending(a, b) for a, b in pairwise(level)) or all(
        is_safe_descending(a, b) for a, b in pairwise(level)
    )


def drop_from(level: tuple[int, ...]) -> Callable[[int], tuple[int, ...]]:
    def drop(i: int) -> tuple[int, ...]:
        return level[:i] + level[i + 1 :]

    return drop


def is_safe_dampened(level: tuple[int, ...]) -> bool:
    n = len(level)
    return any(count(0) | take(n) | select(drop_from(level)) | select(is_safe))


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(639)
    def part_1(self) -> int:
        return how_many(filter(is_safe, self.input | select(parse_ints)))

    @answer(674)
    def part_2(self) -> int:
        return how_many(filter(is_safe_dampened, self.input | select(parse_ints)))
