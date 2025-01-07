# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from dataclasses import dataclass

from solutions.utils.grid import NORTH, Position, Vector

from ...base import StrSplitSolution, answer
from ...utils.iterables import how_many


@dataclass(frozen=True)
class Pose:
    position: Position
    direction: Vector

    def __repr__(self) -> str:
        return f"<Pose position={self.position} direction={self.direction}>"


class Lab:
    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.original_guard_pose = Pose(self._find_original_guard_position(), NORTH)
        self.guard_pose = self.original_guard_pose

    def calculate_guard_path(self) -> list[Position]:
        poses = set()
        while self._is_guarded():
            poses.add(self.guard_pose)
            self._move()
            if self.guard_pose in poses:
                return poses
        return {p.position for p in poses}

    def find_new_obstacles_that_cause_guard_to_loop(self) -> list[Position]:
        original_path_positions = self.calculate_guard_path()
        new_obstacles = []
        for position in original_path_positions:
            cell = self.data[position.row][position.column]
            if cell == ".":
                self.guard_pose = self.original_guard_pose
                self.data[position.row] = (
                    self.data[position.row][: position.column] + "#" + self.data[position.row][position.column + 1 :]
                )
                self.calculate_guard_path()
                if self._is_guarded():
                    # looping!
                    new_obstacles.append(Position(position.row, position.column))
                self.data[position.row] = (
                    self.data[position.row][: position.column] + "." + self.data[position.row][position.column + 1 :]
                )
        return new_obstacles

    def _is_guarded(self) -> bool:
        return self._is_in_lab(self.guard_pose.position)

    def _move(self) -> None:
        step = self.guard_pose.direction
        next_guard_position = self.guard_pose.position + step
        while self._is_obstacle(next_guard_position):
            step = step.turn_right()
            next_guard_position = self.guard_pose.position + step

        self.guard_pose = Pose(next_guard_position, step)

    def _is_obstacle(self, position: Position) -> bool:
        return self._is_in_lab(position) and self.data[position.row][position.column] == "#"

    def _is_in_lab(self, position: Position) -> bool:
        return 0 <= position.row < len(self.data) and 0 <= position.column < len(self.data[position.row])

    def _find_original_guard_position(self) -> Position:
        for row_number, row in enumerate(self.data):
            for column_number, cell in enumerate(row):
                if cell == "^":
                    return Position(row_number, column_number)
        msg = "Guard not found"
        raise ValueError(msg)

    def __repr__(self) -> str:
        return f"<Lab guard_pose={self.guard_pose}>"


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    @answer(4580)
    def part_1(self) -> int:
        self.debug(f"{self.input=}")
        lab = Lab(self.input)
        self.debug(f"{lab=}")
        return how_many(lab.calculate_guard_path())

    # @answer(1234)
    def part_2(self) -> int:
        self.debug(f"{self.input=}")
        lab = Lab(self.input)
        self.debug(f"{lab=}")
        return how_many(lab.find_new_obstacles_that_cause_guard_to_loop())

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
