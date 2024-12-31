# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from collections.abc import Iterable

from pipe import select, where

from solutions.utils.grid import Grid, Position, Vector
from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

directions = (Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0))


def find_neighbours_with_value(park: Grid, start: Position, value: str) -> Iterable[Position]:
    for direction in directions:
        neighbour = start + direction
        if park.get(neighbour, None) == value:
            yield neighbour


def find_reachable(park: Grid, start: Position, height_progression: str) -> Iterable[Position]:
    starts = {start}
    for height in height_progression:
        next_starts = set()
        for this_start in starts:
            next_starts |= set(find_neighbours_with_value(park, this_start, height))
        starts = next_starts
    return starts


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10

    @answer(538)
    def part_1(self) -> int:
        park = Grid(self.input)
        trail_heads = park.enumerate() | where(lambda state: state[1] == "0") | select(lambda state: state[0])
        return sum(trail_heads | select(lambda pos: how_many(find_reachable(park, pos, "123456789"))))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
