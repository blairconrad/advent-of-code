# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

import heapq
from dataclasses import dataclass
from operator import attrgetter
from typing import Self

from pipe import chain, select, where

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

    @answer((104516, 545))
    def solve(self) -> tuple[int, int]:
        maze = Grid(self.input)
        start_pose = Pose(next(maze.enumerate() | where(lambda p: p[1] == "S"))[0], EAST)
        end = next(maze.enumerate() | where(lambda p: p[1] == "E"))
        self.debug(maze)
        self.debug(start_pose)
        self.debug(end)

        fringe: list[Path] = []
        for d in CARDINAL_DIRECTIONS:
            heapq.heappush(fringe, Path((Pose(end[0], d),), 0))
        min_costs = {path.poses[0]: 0 for path in fringe}

        self.debug(fringe)
        paths_from_start: list[Path] = []
        while len(fringe) > 0:
            cheapest_path = heapq.heappop(fringe)
            if len(paths_from_start) > 0 and cheapest_path.cost > paths_from_start[0].cost:
                break
            if cheapest_path.poses[0] == start_pose:
                paths_from_start.append(cheapest_path)
                continue

            next_paths = generate_paths(cheapest_path, maze)
            for path in next_paths:
                if path.poses[0] not in min_costs or path.cost < min_costs[path.poses[0]]:
                    min_costs[path.poses[0]] = path.cost
                if min_costs[path.poses[0]] == path.cost:
                    heapq.heappush(fringe, path)
        return (
            paths_from_start[0].cost,
            len(set(paths_from_start | select(attrgetter("poses")) | chain | select(attrgetter("position")))),
        )
