# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from functools import reduce
from operator import add, mul

from pipe import select

from ...base import TextSolution, answer

to_op = {"+": add, "*": mul}


def transpose(matrix: list) -> zip:
    "Swap the rows and columns of a 2-D matrix."
    # transpose([(1, 2, 3), (11, 22, 33)]) → (1, 11) (2, 22) (3, 33)
    return zip(*matrix, strict=True)


def calculate_row(row: list) -> int:
    op = to_op[row[-1]]
    return reduce(op, row[:-1] | select(int))


class Solution(TextSolution):
    _year = 2025
    _day = 6

    @answer(7326876294741)
    def part_1(self) -> int:
        lines = self.input.split("\n")
        return sum(transpose(lines | select(str.split)) | select(calculate_row))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
