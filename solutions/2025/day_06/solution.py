# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from functools import partial, reduce
from itertools import groupby, zip_longest
from operator import add, itemgetter, mul

from pipe import select, where

from ...base import TextSolution, answer

to_op = {"+": add, "*": mul}


def transpose(matrix: list[str]) -> zip_longest[tuple[str, ...]]:
    "Swap the rows and columns of a 2-D matrix."
    # transpose([(1, 2, 3), (11, 22, 33)]) → (1, 11) (2, 22) (3, 33)
    return zip_longest(*matrix, fillvalue=" ")


def calculate_row_part1(row: list) -> int:
    op = to_op[row[-1]]
    return reduce(op, row[:-1] | select(int))


def calculate_row_part2(row: list) -> int:
    op = to_op[row[0][-1]]
    return reduce(op, [row[0][:-1], *row[1:]] | select(int))


class Solution(TextSolution):
    _year = 2025
    _day = 6

    @answer(7326876294741)
    def part_1(self) -> int:
        lines = self.input.split("\n")
        return sum(transpose(lines | select(str.split)) | select(calculate_row_part1))

    @answer(10756006415204)
    def part_2(self) -> int:
        lines = self.input.split("\n")
        return sum(
            groupby(transpose(lines) | select(partial(str.join, "")) | select(str.strip), bool)
            | where(itemgetter(0))
            | select(itemgetter(1))
            | select(list)
            | select(calculate_row_part2)
        )
