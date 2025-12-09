# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from functools import Placeholder, partial

from pipe import select, where

from solutions.utils.iterables import how_many

from ...base import TextSolution, answer


def parse_input(text: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges_block, ingredients_block = text.split("\n\n")
    ranges = list(
        ranges_block.splitlines()
        | select(partial(str.split, Placeholder, "-"))
        | select(lambda parts: tuple(parts | select(int)))
    )
    ingredients = list(ingredients_block.splitlines() | select(int))
    return ranges, ingredients


def is_fresh(fresh_ranges: list[tuple[int, int]], ingredient: int) -> bool:
    return any(lower <= ingredient <= upper for lower, upper in fresh_ranges)


class Solution(TextSolution):
    _year = 2025
    _day = 5

    @answer(690)
    def part_1(self) -> int:
        fresh_ranges, ingredients = parse_input(self.input)
        return how_many(ingredients | where(partial(is_fresh, fresh_ranges)))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
