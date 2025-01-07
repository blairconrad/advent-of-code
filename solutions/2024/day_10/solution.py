# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from collections.abc import Iterable

from pipe import select, where

from solutions.utils.grid import CARDINAL_DIRECTIONS, Grid, Position
from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer


def find_neighbours_with_value(park: Grid, start: Position, value: str) -> Iterable[Position]:
    for direction in CARDINAL_DIRECTIONS:
        neighbour = start + direction
        if park.get(neighbour, None) == value:
            yield neighbour


def find_reachable(park: Grid, start: Position, height_progression: str) -> Iterable[Position]:
    if height_progression == "":
        return [start]
    results: list[Position] = []
    for neighbour in find_neighbours_with_value(park, start, height_progression[0]):
        results.extend(find_reachable(park, neighbour, height_progression[1:]))
    return results


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10

    @answer(538)
    def part_1(self) -> int:
        park = Grid(self.input)
        trail_heads = park.enumerate() | where(lambda state: state[1] == "0") | select(lambda state: state[0])
        return sum(trail_heads | select(lambda pos: how_many(set(find_reachable(park, pos, "123456789")))))

    @answer(1110)
    def part_2(self) -> int:
        park = Grid(self.input)
        trail_heads = park.enumerate() | where(lambda state: state[1] == "0") | select(lambda state: state[0])
        return sum(trail_heads | select(lambda pos: how_many(find_reachable(park, pos, "123456789"))))
