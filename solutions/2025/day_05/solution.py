# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from functools import Placeholder, partial, reduce

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


def add_range(ranges: list[tuple[int, int]], new_range: tuple[int, int]) -> list[tuple[int, int]]:
    new_ranges = []
    for a_range in ranges:
        if a_range[1] < new_range[0] or a_range[0] > new_range[1]:
            new_ranges.append(a_range)
        else:
            new_range = (min(a_range[0], new_range[0]), max(a_range[1], new_range[1]))
    new_ranges.append(new_range)
    return new_ranges


def count_range(a_range: tuple[int, int]) -> int:
    return a_range[1] - a_range[0] + 1


class Solution(TextSolution):
    _year = 2025
    _day = 5

    @answer(690)
    def part_1(self) -> int:
        fresh_ranges, ingredients = parse_input(self.input)
        consolidated_ranges: list[tuple[int, int]] = reduce(add_range, fresh_ranges, [])
        return how_many(ingredients | where(partial(is_fresh, consolidated_ranges)))

    @answer(344323629240733)
    def part_2(self) -> int:
        fresh_ranges, _ = parse_input(self.input)
        consolidated_ranges: list[tuple[int, int]] = reduce(add_range, fresh_ranges, [])
        return sum(consolidated_ranges | select(count_range))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
