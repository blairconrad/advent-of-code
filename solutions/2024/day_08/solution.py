# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from itertools import combinations
from typing import Self

from pipe import Pipe, chain, select, where

from ...base import StrSplitSolution, answer


@dataclass(frozen=True)
class Vector:
    row_change: int
    column_change: int


@dataclass(frozen=True)
class Position:
    row: int
    column: int

    def __add__(self, pos: Vector) -> Self:
        return Position(self.row + pos.row_change, self.column + pos.column_change)

    def __sub__(self, other: Self | Vector) -> Vector:
        match other:
            case Position(row, column):
                return Vector(self.row - row, self.column - column)
            case Vector(row_change, column_change):
                return Position(self.row - row_change, self.column - column_change)


class Grid:
    def __init__(self, grid: list[str]) -> None:
        self.grid = grid

    def enumerate(self) -> Iterable[tuple[Position, str]]:
        return (
            (Position(row, column), self.grid[row][column])
            for row in range(len(self.grid))
            for column in range(len(self.grid[row]))
        )

    def contains(self, position: Position) -> bool:
        return 0 <= position.row < len(self.grid) and 0 <= position.column < len(self.grid[position.row])


def find_antennae(grid: Grid) -> Iterable[list[Position]]:
    antennae = defaultdict(list)
    for position, state in grid.enumerate():
        if state != ".":
            antennae[state].append(position)
    return antennae.values()


def get_antenna_pairs(antenna_set: list[Position]) -> list[tuple[Position, Position]]:
    return list(antenna_set | Pipe(combinations, 2))


def find_antinodes(antenna_pair: tuple[Position, Position]) -> list[Position]:
    diff = antenna_pair[1] - antenna_pair[0]
    return [antenna_pair[0] - diff, antenna_pair[1] + diff]


class Solution(StrSplitSolution):  # or TextSolution, etc
    _year = 2024
    _day = 8

    @answer(351)
    def part_1(self) -> int:
        city = Grid(self.input)
        return len(
            set(
                find_antennae(city)
                | select(get_antenna_pairs)
                | chain
                | select(find_antinodes)
                | chain
                | where(city.contains)
            )
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
