# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re
from collections.abc import Iterable

from pipe import Pipe, select

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 3

    def find_muls(self, program: str) -> Iterable[tuple[int, int]]:
        return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)

    @answer(179834255)
    def part_1(self) -> int:
        return sum(self.find_muls(self.input) | select(lambda x: int(x[0]) * int(x[1])))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
