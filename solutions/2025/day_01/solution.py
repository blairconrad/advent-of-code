# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from functools import Placeholder, partial
from itertools import accumulate

from pipe import select, where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer


class Safe:
    def __init__(self, size: int, start: int) -> None:
        self.size = size
        self.position = start

    def spin(self, rotation: str) -> int:
        magnitude = int(rotation[1:])
        move = magnitude if rotation[0] == "R" else -magnitude
        self.position = (self.position + move) % self.size
        return self.position


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(999)
    def part_1(self) -> int:
        safe = Safe(100, 50)

        return how_many(self.input | select(safe.spin) | where(lambda x: x == 0))

    # @answer(3)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
