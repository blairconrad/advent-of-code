# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from typing import TYPE_CHECKING

from pipe import select, where

from solutions.utils.grid import EAST, NORTH, WEST, Grid
from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable

EMPTY: int = 0
BEAM: int = 1
SPLITTER: int = -1
HIT_SPLITTER = -2

point_mapping: dict[str, int] = {
    ".": EMPTY,
    "S": BEAM,
    "^": SPLITTER,
}


def parse_point(point: str) -> int:
    return point_mapping.get(point, EMPTY)


def parse_line(line: str) -> Iterable[int]:
    return line | select(parse_point)


def fire_beam(field: Grid[int]) -> None:
    for position in field.positions():
        match field[position]:
            case value if value == SPLITTER:
                if field[position + NORTH] == BEAM:
                    field[position] = HIT_SPLITTER
                    field[position + WEST] = BEAM
                    field[position + EAST] = BEAM
            case _ if field[position + NORTH] == BEAM:
                field[position] = BEAM


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    @answer(1518)
    def part_1(self) -> int:
        field = Grid(self.input | select(parse_line))
        fire_beam(field)

        return how_many(field.enumerate() | select(lambda pv: pv[1]) | where(lambda v: v == HIT_SPLITTER))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
