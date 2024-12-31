# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from collections.abc import Iterable

from pipe import Pipe, select, where

from solutions.utils.grid import Grid, Position

from ...base import StrSplitSolution, answer


def is_block_present_at(puzzle: Grid, starting_position: Position, block: Grid) -> bool:
    origin = Position(0, 0)
    return all(
        block.enumerate()
        | select(
            lambda b: (b[1] == " " or (puzzle.contains(p := starting_position + (b[0] - origin)) and puzzle[p] == b[1]))
        )
    )


def count_block(puzzle: Grid, block: Grid) -> int:
    return puzzle.positions() | where(lambda p: is_block_present_at(puzzle, p, block)) | how_many


@Pipe
def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2397)
    def part_1(self) -> int:
        puzzle = Grid(self.input)
        blocks = [
            ["XMAS"],
            ["SAMX"],
            ["X", "M", "A", "S"],
            ["S", "A", "M", "X"],
            ["X", " M", "  A", "   S"],
            ["S", " A", "  M", "   X"],
            ["   X", "  M", " A", "S"],
            ["   S", "  A", " M", "X"],
        ] | select(Grid)

        return sum(blocks | select(lambda b: count_block(puzzle, b)))

    @answer(1824)
    def part_2(self) -> int:
        puzzle = Grid(self.input)
        blocks = [
            ["M M", " A", "S S"],
            ["S S", " A", "M M"],
            ["M S", " A", "M S"],
            ["S M", " A", "S M"],
        ] | select(Grid)
        return sum(blocks | select(lambda b: count_block(puzzle, b)))
