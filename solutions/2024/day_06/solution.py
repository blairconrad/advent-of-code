# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Self

from ...base import StrSplitSolution, answer


def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


@dataclass(frozen=True)
class Step:
    row_move: int
    column_move: int


@dataclass(frozen=True)
class Position:
    row: int
    column: int

    def __add__(self, other: Step) -> Self:
        return Position(self.row + other.row_move, self.column + other.column_move)


class Lab:
    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.guard_position = self._find_guard_position()
        self.guard_direction = 0

    def walk_the_guard_out(self) -> list[Position]:
        positions = set()
        while self.is_guarded():
            self.move()
            positions.add(self.guard_position)
        return positions

    def is_guarded(self) -> bool:
        return self._is_in_lab(self.guard_position)

    def move(self) -> None:
        step = steps[self.guard_direction]
        next_guard_position = self.guard_position + step
        while self._is_obstacle(next_guard_position):
            self.guard_direction = (self.guard_direction + 1) % len(steps)
            step = steps[self.guard_direction]
            next_guard_position = self.guard_position + step

        self.guard_position = next_guard_position

    def _is_obstacle(self, position: Position) -> bool:
        return self._is_in_lab(position) and self.data[position.row][position.column] == "#"

    def _is_in_lab(self, position: Position) -> bool:
        return 0 <= position.row < len(self.data) and 0 <= position.column < len(self.data[position.row])

    def _find_guard_position(self) -> Position:
        for row_number, row in enumerate(self.data):
            for column_number, cell in enumerate(row):
                if cell == "^":
                    return Position(row_number, column_number)
        msg = "Guard not found"
        raise ValueError(msg)

    def __repr__(self) -> str:
        return f"<Lab guard_position={self.guard_position} guard_direction={self.guard_direction}>"


steps = [Step(-1, 0), Step(0, 1), Step(1, 0), Step(0, -1)]


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    @answer(4580)
    def part_1(self) -> int:
        self.debug(f"{self.input=}")
        lab = Lab(self.input)
        self.debug(f"{lab=}")
        return how_many(lab.walk_the_guard_out())

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
