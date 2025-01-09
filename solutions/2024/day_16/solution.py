# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

import heapq
from dataclasses import dataclass
from typing import Self

from pipe import where

from solutions.utils.grid import CARDINAL_DIRECTIONS, EAST, Grid, Pose

from ...base import StrSplitSolution, answer


@dataclass
class Path:
    poses: tuple[Pose, ...]
    cost: int

    def __lt__(self, other: Self) -> bool:
        return self.cost < other.cost


def generate_paths(path: Path, maze: Grid) -> list[Path]:
    starting_position = path.poses[0].position
    starting_direction = path.poses[0].direction
    moves = [
        Path((Pose(starting_position, starting_direction.turn_left()), *path.poses), path.cost + 1000),
        Path((Pose(starting_position, starting_direction.turn_right()), *path.poses), path.cost + 1000),
    ]

    new_pose = Pose(starting_position - starting_direction, starting_direction)
    if maze[new_pose.position] != "#":
        moves.append(Path((new_pose, *path.poses), path.cost + 1))
    return moves


class Solution(StrSplitSolution):
    _year = 2024
    _day = 16

    @answer(104516)
    def part_1(self) -> int:
        maze = Grid(self.input)
        start_pose = Pose(next(maze.enumerate() | where(lambda p: p[1] == "S"))[0], EAST)
        end = next(maze.enumerate() | where(lambda p: p[1] == "E"))
        self.debug(maze)
        self.debug(start_pose)
        self.debug(end)

        fringe: list[Path] = []
        for d in CARDINAL_DIRECTIONS:
            heapq.heappush(fringe, Path((Pose(end[0], d),), 0))
        seen = {path.poses[0]: path for path in fringe}

        self.debug(fringe)
        while len(fringe) > 0:
            cheapest_path = heapq.heappop(fringe)
            if cheapest_path.poses[0] == start_pose:
                return cheapest_path.cost
            next_paths = generate_paths(cheapest_path, maze)
            for path in next_paths:
                if path.poses[0] not in seen or path.cost < seen[path.poses[0]].cost:
                    heapq.heappush(fringe, path)
                    seen[path.poses[0]] = path
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
