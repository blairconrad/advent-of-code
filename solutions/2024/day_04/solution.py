# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Self

from pipe import Pipe, chain, select, where

from ...base import StrSplitSolution, answer


@dataclass
class Position:
    row: int
    column: int

    def __add__(self, other: Self) -> Self:
        return Position(self.row + other.row, self.column + other.column)


def positions_in(block: list[str]) -> Iterable[Position]:
    return (
        range(len(block))
        | select(lambda row: range(len(block[row])) | select(lambda column: Position(row, column)))
        | chain
    )


def is_block_present_at(puzzle: list[str], starting_position: Position, block: list[str]) -> bool:
    return all(
        positions_in(block)
        | select(
            lambda p: (b := block[p.row][p.column]) == " "
            or (
                0 <= (puzzle_pos := starting_position + p).row < len(puzzle)
                and 0 <= puzzle_pos.column < len(puzzle[puzzle_pos.row])
                and puzzle[puzzle_pos.row][puzzle_pos.column] == b
            )
        )
    )


def count_block(puzzle: list[str], block: list[str]) -> int:
    return positions_in(puzzle) | where(lambda p: is_block_present_at(puzzle, p, block)) | how_many


@Pipe
def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2397)
    def part_1(self) -> int:
        blocks = [
            ["XMAS"],
            ["SAMX"],
            ["X", "M", "A", "S"],
            ["S", "A", "M", "X"],
            ["X", " M", "  A", "   S"],
            ["S", " A", "  M", "   X"],
            ["   X", "  M", " A", "S"],
            ["   S", "  A", " M", "X"],
        ]

        return sum(blocks | select(lambda b: count_block(self.input, b)))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
