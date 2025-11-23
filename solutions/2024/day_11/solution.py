# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from functools import cache
from typing import TYPE_CHECKING

from pipe import Pipe

from ...base import IntSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable


def split_int(n: int) -> list[int] | None:
    digits = str(n)
    if len(digits) % 2 == 1:
        return None
    first_half = digits[: len(digits) // 2]
    second_half = digits[len(digits) // 2 :].lstrip("0")
    if second_half == "":
        second_half = "0"
    return [int(first_half), int(second_half)]


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    if (parts := split_int(stone)) is not None:
        return parts
    return [stone * 2024]


@Pipe
def count_blinks(stones: Iterable[int], num_blinks: int) -> Iterable[int]:
    for stone in stones:
        yield count_blinks_output(stone, num_blinks)


@cache
def count_blinks_output(stone: int, num_blinks: int) -> int:
    if num_blinks == 0:
        return 1
    stones = blink(stone)
    return sum(stones | count_blinks(num_blinks - 1))


class Solution(IntSplitSolution):
    _year = 2024
    _day = 11

    separator = " "

    @answer(216996)
    def part_1(self) -> int:
        stones = self.input
        return sum(stones | count_blinks(25))

    @answer(257335372288947)
    def part_2(self) -> int:
        stones = self.input
        return sum(stones | count_blinks(75))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
