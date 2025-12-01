# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from typing import TYPE_CHECKING

from pipe import select, traverse, where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Generator


class Safe:
    def __init__(self, size: int, start: int) -> None:
        self.size = size
        self.position = start

    def spin(self, rotation: str) -> int:
        list(self.spin_slowly(rotation))
        return self.position

    def spin_slowly(self, rotation: str) -> Generator[int]:
        magnitude = int(rotation[1:])
        step = 1 if rotation[0] == "R" else -1
        for _ in range(magnitude):
            self.position = (self.position + step) % self.size
            yield self.position


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(999)
    def part_1(self) -> int:
        safe = Safe(100, 50)
        return how_many(self.input | select(safe.spin) | where(lambda x: x == 0))

    @answer(6099)
    def part_2(self) -> int:
        safe = Safe(100, 50)
        return how_many(self.input | select(safe.spin_slowly) | traverse | where(lambda x: x == 0))
