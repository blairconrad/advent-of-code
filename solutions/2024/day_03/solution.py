# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re
from collections.abc import Iterable
from functools import reduce
from operator import mul

from pipe import Pipe, chain, select

from ...base import TextSolution, answer


def to_ints(strs: Iterable[str]) -> Iterable[int]:
    return map(int, strs)


def product(nums: Iterable[int]) -> int:
    return reduce(mul, nums, 1)


class Solution(TextSolution):
    _year = 2024
    _day = 3

    def find_active_areas(self, program: str) -> Iterable[str]:
        return re.split(r"don't\(\).*?(?:do\(\)|$)", program, flags=re.DOTALL)

    def find_multiplicands(self, program: str) -> Iterable[tuple[int, int]]:
        return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)

    @answer(179834255)
    def part_1(self) -> int:
        return self.find_multiplicands(self.input) | select(to_ints) | select(product) | Pipe(sum)

    @answer(80570939)
    def part_2(self) -> int:
        return (
            self.find_active_areas(self.input)
            | select(self.find_multiplicands)
            | chain
            | select(to_ints)
            | select(product)
            | Pipe(sum)
        )
