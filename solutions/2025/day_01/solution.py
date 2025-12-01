# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from functools import Placeholder, partial
from itertools import accumulate

from pipe import select, where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer


def parse_rotation(rotation_str: str) -> int:
    magnitude = int(rotation_str[1:])
    return magnitude if rotation_str[0] == "R" else -magnitude


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(999)
    def part_1(self) -> int:
        return how_many(spin(self.input | select(parse_rotation)) | where(lambda x: x == 0))

    # @answer(3)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
