# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/20


from pipe import where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer
from ...utils.grid import CARDINAL_DIRECTIONS, Grid, Position, Vector


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


def calculate_all_cheat_savings(distance: int, times: dict[Position, int]) -> dict[tuple[Position, Position], int]:
    savings = {}
    jumps = set()
    for r in range(distance):
        base_jump = Vector(r, distance - r)
        jumps.add(base_jump)
        jumps.add(base_jump.turn_left())
        jumps.add(base_jump.turn_right())
        jumps.add(base_jump.turn_around())

        flip_jump = Vector(r, r - distance)
        jumps.add(flip_jump)
        jumps.add(flip_jump.turn_left())
        jumps.add(flip_jump.turn_right())
        jumps.add(flip_jump.turn_around())

    for jump in jumps:
        for position, time in times.items():
            next_position = position + jump
            if next_position in times:
                savings[(position, next_position)] = times[next_position] - time - distance
    return savings


class Solution(StrSplitSolution):
    _year = 2024
    _day = 20

    @answer(1399)
    def part_1(self) -> int:
        desired_savings = 64 if self.use_test_data else 100
        course = Grid(self.input)
        end_position = course.find("E")

        times = calculate_all_times_to_end(course, end_position)
        self.debug(times)

        savings = calculate_all_cheat_savings(2, times)
        self.debug(savings)
        return how_many(savings.values() | where(lambda x: x >= desired_savings))

    @answer(994807)
    def part_2(self) -> int:
        desired_savings = 50 if self.use_test_data else 100
        course = Grid(self.input)
        end_position = course.find("E")

        times = calculate_all_times_to_end(course, end_position)
        self.debug(times)

        num_jumps_that_save_enough = 0
        for r in range(2, 20 + 1):
            num_jumps_that_save_enough += how_many(
                calculate_all_cheat_savings(r, times).values() | where(lambda x: x >= desired_savings)
            )
        return num_jumps_that_save_enough
