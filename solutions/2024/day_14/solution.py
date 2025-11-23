# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

from dataclasses import dataclass
from functools import partial, reduce
from operator import mul
from re import match
from typing import TYPE_CHECKING

from pipe import select

from solutions.utils.grid import Position, Vector
from solutions.utils.iterables import tee

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable


@dataclass
class Robot:
    position: Position
    movement: Vector


@dataclass
class RoomSize:
    rows: int
    columns: int


def build_robot(line: str) -> Robot:
    col_pos, row_pos, col_move, row_move = match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
    return Robot(Position(int(row_pos), int(col_pos)), Vector(int(row_move), int(col_move)))


def move_robot(robot: Robot, num_steps: int, room_size: RoomSize) -> Position:
    return Position(
        (robot.position.row + robot.movement.row_change * num_steps) % room_size.rows,
        (robot.position.column + robot.movement.column_change * num_steps) % room_size.columns,
    )


def group_robots(positions: Iterable[Position], room_size: RoomSize) -> Iterable[int]:
    counts = [0] * 4

    for pos in positions:
        middle_row_index = room_size.rows // 2
        middle_column_index = room_size.columns // 2
        if pos.row == middle_row_index or pos.column == middle_column_index:
            continue
        index = 0
        if pos.row > middle_row_index:
            index += 2
        if pos.column > middle_column_index:
            index += 1
        counts[index] += 1
    return counts


class Solution(StrSplitSolution):
    _year = 2024
    _day = 14

    @answer(225552000)
    def part_1(self) -> int:
        robots = list(self.input | select(build_robot))
        room_size = RoomSize(
            max(robots | select(lambda r: r.position.row)) + 1,
            max(robots | select(lambda r: r.position.column)) + 1,
        )
        self.debug(room_size)
        final_positions = robots | select(partial(move_robot, num_steps=100, room_size=room_size)) | tee(self.debug)
        return reduce(mul, group_robots(final_positions, room_size), 1)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
