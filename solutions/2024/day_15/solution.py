# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

from collections.abc import Iterable

from pipe import select, where

from solutions.utils.grid import Grid, Position, Vector

from ...base import StrSplitSolution, answer

directions = {
    "^": Vector(-1, 0),
    "v": Vector(1, 0),
    "<": Vector(0, -1),
    ">": Vector(0, 1),
}

LEFT_BOX = "["
RIGHT_BOX = "]"
SKINNY_BOX = "O"
BOX = SKINNY_BOX + LEFT_BOX + RIGHT_BOX
EMPTY = "."
ROBOT = "@"
WALL = "#"


def coordinates(position: Position, tile: str) -> int:
    return position.row * 100 + position.column if tile in (SKINNY_BOX, LEFT_BOX) else 0


def find_robot(warehouse: Grid) -> Position:
    return next(warehouse.enumerate() | where(lambda tile: tile[1] == ROBOT) | select(lambda tile: tile[0]))


def augment_boxes(warehouse: Grid, box_positions: set[Position]) -> set[Position]:
    new_positions = set()
    for box_position in box_positions:
        if warehouse[box_position] == LEFT_BOX:
            new_positions.add(box_position + directions[">"])
        elif warehouse[box_position] == RIGHT_BOX:
            new_positions.add(box_position + directions["<"])
    return box_positions | new_positions


def empty_out(warehouse: Grid, positions: Iterable[Position]) -> None:
    for position in positions:
        warehouse[position] = EMPTY


def push_boxes(warehouse: Grid, box_positions: set[Position], direction: Vector) -> bool:
    if direction.row_change != 0:
        box_positions = augment_boxes(warehouse, box_positions)
    new_box_positions = []
    for box_position in box_positions:
        new_box_position = box_position + direction
        if warehouse[new_box_position] == WALL:
            return False
        new_box_positions.append((new_box_position, warehouse[box_position]))

    box_positions_to_push = {box[0] for box in new_box_positions if warehouse[box[0]] in BOX}
    if len(box_positions) > 0 and not push_boxes(warehouse, box_positions_to_push, direction):
        return False
    for box_position, box in new_box_positions:
        warehouse[box_position] = box
    empty_out(warehouse, box_positions)
    return True


def move_robot(warehouse: Grid, robot: Position, direction_name: str) -> Position:
    direction = directions[direction_name]
    new_robot_position = robot + direction
    if warehouse[new_robot_position] == WALL:
        return robot
    if warehouse[new_robot_position] == EMPTY or push_boxes(warehouse, {new_robot_position}, direction):
        warehouse[new_robot_position] = ROBOT
        warehouse[robot] = EMPTY
        return new_robot_position
    return robot


def stretch_warehouse(warehouse: list[str]) -> list[str]:
    def double_it(c: str) -> str:
        if c == SKINNY_BOX:
            return LEFT_BOX + RIGHT_BOX
        if c == ROBOT:
            return ROBOT + EMPTY
        return c + c

    return ["".join(double_it(c) for c in line) for line in warehouse]


class Solution(StrSplitSolution):
    _year = 2024
    _day = 15

    def do_it(self, warehouse: Grid, instructions: str) -> int:
        robot = find_robot(warehouse)

        self.debug(warehouse)
        while instructions:
            direction = instructions[0]
            instructions = instructions[1:]
            robot = move_robot(warehouse, robot, direction)
            self.debug(warehouse)
        return sum(coordinates(position, tile) for position, tile in warehouse.enumerate())

    @answer(1371036)
    def part_1(self) -> int:
        blank_row_index = self.input.index("")
        warehouse = Grid(self.input[:blank_row_index])
        instructions = "".join(self.input[blank_row_index + 1 :])
        return self.do_it(warehouse, instructions)

    @answer(1392847)
    def part_2(self) -> int:
        blank_row_index = self.input.index("")
        warehouse = Grid(stretch_warehouse(self.input[:blank_row_index]))
        instructions = "".join(self.input[blank_row_index + 1 :])
        return self.do_it(warehouse, instructions)
