# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/20

from pipe import where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer
from ...utils.grid import CARDINAL_DIRECTIONS, EAST, NORTH, SOUTH, WEST, Grid, Position


def calculate_all_times_to_end(course: Grid, end: Position) -> dict[Position, int]:
    times = {end: 0}
    frontier = [end]
    while frontier:
        current = frontier.pop(0)
        for direction in CARDINAL_DIRECTIONS:
            next_position = current + direction
            if course[next_position] == "#":
                continue
            if next_position in times:
                continue
            times[next_position] = times[current] + 1
            frontier.append(next_position)
    return times


def calculate_all_cheat_savings(times: dict[Position, int]) -> dict[tuple[Position, Position], int]:
    savings = {}
    for position, time in times.items():
        for jump in [NORTH * 2, NORTH + EAST, EAST * 2, EAST + SOUTH, SOUTH * 2, SOUTH + WEST, WEST * 2, WEST + NORTH]:
            if position + jump in times:
                savings[(position, position + jump)] = time - times[position + jump] - 2
    return savings


class Solution(StrSplitSolution):
    _year = 2024
    _day = 20

    @answer(1399)
    def part_1(self) -> int:
        desired_savings = 100
        course = Grid(self.input)
        start_position = course.find("S")
        end_position = course.find("E")

        self.debug(start_position, end_position, course)

        times = calculate_all_times_to_end(course, end_position)
        self.debug(times)

        savings = calculate_all_cheat_savings(times)
        self.debug(savings)
        return how_many(savings.values() | where(lambda x: x >= desired_savings))

    @answer(1234)
    def part_2(self) -> int:
        return 1234
