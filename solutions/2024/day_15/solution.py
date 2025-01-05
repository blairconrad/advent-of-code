# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

from solutions.utils.grid import Grid, Position, Vector
from ...base import StrSplitSolution, answer
from pipe import select, where

directions = {
    "^": Vector(-1, 0),
    "v": Vector(1, 0),
    "<": Vector(0, -1),
    ">": Vector(0, 1),
}

BOX = "O"
EMPTY = "."
ROBOT = "@"
WALL = "#"


def coordinates(position: Position) -> int:
    return position.row * 100 + position.column


def find_robot(warehouse: Grid) -> Position:
    return next(warehouse.enumerate() | where(lambda tile: tile[1] == ROBOT) | select(lambda tile: tile[0]))


def push_boxes(warehouse: Grid, box_position: Position, direction: Vector) -> bool:
    new_box_position = box_position + direction
    if warehouse[new_box_position] == WALL:
        return False
    if warehouse[new_box_position] == EMPTY or (
        warehouse[new_box_position] == BOX and push_boxes(warehouse, new_box_position, direction)
    ):
        warehouse[new_box_position] = warehouse[box_position]
        return True
    return False


def move_robot(warehouse: Grid, robot: Position, direction_name: str) -> Position:
    direction = directions[direction_name]
    new_robot_position = robot + direction
    if warehouse[new_robot_position] == WALL:
        return robot
    if warehouse[new_robot_position] == EMPTY or push_boxes(warehouse, new_robot_position, direction):
        warehouse[new_robot_position] = ROBOT
        warehouse[robot] = EMPTY
        return new_robot_position
    return robot


class Solution(StrSplitSolution):
    _year = 2024
    _day = 15

    @answer(1371036)
    def part_1(self) -> int:
        blank_row_index = self.input.index("")

        warehouse = Grid(self.input[:blank_row_index])
        instructions = "".join(self.input[blank_row_index + 1 :])
        robot = find_robot(warehouse)

        self.debug(warehouse)
        self.debug(instructions)
        self.debug(robot)

        while instructions:
            direction = instructions[0]
            instructions = instructions[1:]
            robot = move_robot(warehouse, robot, direction)
        return sum(coordinates(position) for position, tile in warehouse.enumerate() if tile == BOX)

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
