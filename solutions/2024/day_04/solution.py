# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from collections.abc import Iterable
from dataclasses import dataclass
from itertools import product
from typing import Self

from pipe import Pipe, where

from ...base import StrSplitSolution, answer


@dataclass
class Stride:
    over: int
    down: int


all_strides = [
    Stride(-1, -1),
    Stride(0, -1),
    Stride(1, -1),
    Stride(-1, 0),
    Stride(1, 0),
    Stride(-1, 1),
    Stride(0, 1),
    Stride(1, 1),
]


@dataclass
class Position:
    row: int
    column: int

    def move(self, stride: Stride) -> Self:
        return Position(self.row + stride.down, self.column + stride.over)


def is_valid_position(puzzle: list[str], position: Position) -> bool:
    return 0 <= position.row < len(puzzle) and 0 <= position.column < len(puzzle[position.row])


def find(puzzle: list[str], target: str, starting_position: Position, stride: Stride) -> bool:
    if not target:
        return True

    if (
        is_valid_position(puzzle, starting_position)
        and puzzle[starting_position.row][starting_position.column] == target[0]
    ):
        return find(puzzle, target[1:], starting_position.move(stride), stride)
    return False


@Pipe
def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2397)
    def part_1(self) -> int:
        return (
            product(product(range(len(self.input)), range(len(self.input[0]))), all_strides)
            | where(lambda position_stride: find(self.input, "XMAS", Position(*position_stride[0]), position_stride[1]))
            | how_many
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
