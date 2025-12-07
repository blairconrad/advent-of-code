# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from functools import partial
from itertools import repeat
from operator import itemgetter
from typing import TYPE_CHECKING

from pipe import select, take_while, where

from solutions.utils.grid import CARDINAL_DIRECTIONS, EAST, NORTH, SOUTH, WEST, Grid, Position
from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable

POSITION = 0
CONTENT = 1

PAPER_ROLL = "@"
TOO_MANY_ADJACENT_ROLLS = 4


PRINCIPAL_DIRECTIONS = (*CARDINAL_DIRECTIONS, NORTH + EAST, EAST + SOUTH, SOUTH + WEST, WEST + NORTH)


def can_move_roll(grid: Grid, position: Position) -> bool:
    return (
        how_many(direction for direction in PRINCIPAL_DIRECTIONS if grid.get(position + direction, None) == PAPER_ROLL)
        < TOO_MANY_ADJACENT_ROLLS
    )


def find_movable_rolls(warehouse: Grid) -> Iterable[Position]:
    return (
        warehouse.enumerate()
        | where(lambda tile: tile[CONTENT] == PAPER_ROLL)
        | select(itemgetter(POSITION))
        | where(partial(can_move_roll, warehouse))
    )


def move_roll(warehouse: Grid, roll: Position) -> None:
    warehouse[roll] = "x"


def move_rolls(warehouse: Grid) -> int:
    return how_many(list(find_movable_rolls(warehouse)) | select(partial(move_roll, warehouse)))


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    @answer(1508)
    def part_1(self) -> int:
        warehouse = Grid(self.input[:])
        return move_rolls(warehouse)

    @answer(8538)
    def part_2(self) -> int:
        warehouse = Grid(self.input)
        return sum(repeat(warehouse) | select(move_rolls) | take_while(lambda moved: moved > 0))
