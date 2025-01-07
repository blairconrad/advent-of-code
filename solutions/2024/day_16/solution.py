# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

import heapq
from dataclasses import dataclass

from pipe import where

from solutions.utils.grid import Grid, Position, Vector

from ...base import StrSplitSolution, answer

north = Vector(-1, 0)
east = Vector(0, 1)
south = Vector(1, 0)
west = Vector(0, -1)

directions = (north, east, south, west)


def turn_left(v: Vector) -> Vector:
    return Vector(-v.column_change, v.row_change)


def turn_right(v: Vector) -> Vector:
    return Vector(v.column_change, -v.row_change)


@dataclass(frozen=True)
class Pose:
    position: Position
    direction: Vector


@dataclass(frozen=True, eq=True)
class State:
    pose: Pose
    cost: int

    def __lt__(self, other: "State") -> bool:
        return self.cost < other.cost


def generate_states(state: State, maze: Grid) -> list[State]:
    moves = [
        State(Pose(state.pose.position, turn_left(state.pose.direction)), state.cost + 1000),
        State(Pose(state.pose.position, turn_right(state.pose.direction)), state.cost + 1000),
    ]

    new_pose = Pose(state.pose.position - state.pose.direction, state.pose.direction)
    if maze[new_pose.position] != "#":
        moves.append(State(new_pose, state.cost + 1))
    return moves


class Solution(StrSplitSolution):
    _year = 2024
    _day = 16

    @answer(104516)
    def part_1(self) -> int:
        maze = Grid(self.input)
        start_pose = Pose(next(maze.enumerate() | where(lambda p: p[1] == "S"))[0], east)
        end = next(maze.enumerate() | where(lambda p: p[1] == "E"))
        self.debug(maze)
        self.debug(start_pose)
        self.debug(end)

        fringe: list[State] = []
        for d in directions:
            heapq.heappush(fringe, State(Pose(end[0], d), 0))
        seen = {s.pose: s.cost for s in fringe}

        self.debug(fringe)
        while len(fringe) > 0:
            cheapest_state = heapq.heappop(fringe)
            if cheapest_state.pose == start_pose:
                return cheapest_state.cost
            next_states = generate_states(cheapest_state, maze)
            for state in next_states:
                if state.pose not in seen or state.cost < seen[state.pose]:
                    heapq.heappush(fringe, state)
                    seen[state.pose] = state.cost
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
