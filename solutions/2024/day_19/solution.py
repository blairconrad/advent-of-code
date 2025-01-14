# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from functools import cache

from pipe import select, where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer


class Maker:
    def __init__(self, patterns: list[str]) -> None:
        self.patterns = patterns

    @cache
    def can_make(self, design: str) -> bool:
        return len(design) == 0 or any(
            design.startswith(pattern) and self.can_make(design[len(pattern) :]) for pattern in self.patterns
        )


class Solution(StrSplitSolution):
    _year = 2024
    _day = 19

    @answer(330)
    def part_1(self) -> int:
        patterns = self.input[0].split(", ")
        designs = list(self.input[2:] | select(str.strip))

        maker = Maker(patterns)
        return how_many(designs | where(maker.can_make))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
