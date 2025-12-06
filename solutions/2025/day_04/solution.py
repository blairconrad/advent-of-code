# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from functools import partial
from operator import itemgetter

from pipe import select, where

from solutions.utils.grid import CARDINAL_DIRECTIONS, EAST, NORTH, SOUTH, WEST, Grid, Position
from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

POSITION = 0
CONTENT = 1

PAPER_ROLL = "@"
TOO_MANY_ADJACENT_ROLLS = 4


PRINCIPAL_DIRECTIONS = (*CARDINAL_DIRECTIONS, NORTH + EAST, EAST + SOUTH, SOUTH + WEST, WEST + NORTH)


def count_adjacent_rolls(grid: Grid, position: Position) -> int:
    return how_many(
        direction for direction in PRINCIPAL_DIRECTIONS if grid.get(position + direction, None) == PAPER_ROLL
    )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    @answer(1508)
    def part_1(self) -> int:
        warehouse = Grid(self.input)
        return how_many(
            warehouse.enumerate()
            | where(lambda tile: tile[CONTENT] == PAPER_ROLL)
            | select(itemgetter(POSITION))
            | select(partial(count_adjacent_rolls, warehouse))
            | where(lambda count: count < TOO_MANY_ADJACENT_ROLLS)
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
