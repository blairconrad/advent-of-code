# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from functools import cache

from pipe import select, where

from ...base import StrSplitSolution, answer


class Maker:
    def __init__(self, patterns: list[str]) -> None:
        self.patterns = patterns

    @cache
    def ways_to_make(self, design: str) -> int:
        return (
            sum(
                self.patterns
                | where(design.startswith)
                | select(lambda pattern: self.ways_to_make(design[len(pattern) :]))
            )
            if len(design) > 0
            else 1
        )


class Solution(StrSplitSolution):
    _year = 2024
    _day = 19

    @answer((330, 950763269786650))
    def solve(self) -> tuple[int, int]:
        patterns = self.input[0].split(", ")
        designs = list(self.input[2:] | select(str.strip))

        maker = Maker(patterns)
        number_of_ways = list(designs | select(maker.ways_to_make) | where(lambda x: x != 0))
        return len(number_of_ways), sum(number_of_ways)
