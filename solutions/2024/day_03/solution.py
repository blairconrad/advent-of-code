# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re
from collections.abc import Iterable
from itertools import chain
from operator import mul

from pipe import Pipe, select

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 3

    def find_active_areas(self, program: str) -> Iterable[str]:
        return re.split(r"don't\(\).*?(?:do\(\)|$)", program, flags=re.DOTALL)

    def find_muls(self, program: str) -> Iterable[tuple[int, int]]:
        return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)

    @answer(179834255)
    def part_1(self) -> int:
        return self.find_muls(self.input) | select(lambda x: x | select(int)) | select(lambda x: mul(*x)) | Pipe(sum)

    @answer(80570939)
    def part_2(self) -> int:
        return (
            self.find_active_areas(self.input)
            | select(self.find_muls)
            | Pipe(chain.from_iterable)
            | select(lambda x: x | select(int))
            | select(lambda x: mul(*x))
            | Pipe(sum)
        )
