# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from collections.abc import Iterable
from dataclasses import dataclass

from pipe import select

from solutions.utils.grid import Grid, Position, Vector

from ...base import StrSplitSolution, answer

north = Vector(-1, 0)
east = Vector(0, 1)
south = Vector(1, 0)
west = Vector(0, -1)

directions = (north, east, south, west)


def split_into_plots(garden: Grid) -> Iterable[list[Position]]:
    seen: set[Position] = set()
    for start in garden.positions():
        if start in seen:
            continue
        plot: list[Position] = []
        fringe = {start}

        while len(fringe) > 0:
            position = fringe.pop()
            if position in plot:
                continue

            plot.append(position)
            plot_type = garden[position]
            for direction in directions:
                neighbour_position = position + direction
                if garden.contains(neighbour_position) and garden[neighbour_position] == plot_type:
                    fringe.add(neighbour_position)

        seen |= set(plot)
        yield plot


def calculate_perimeter_segments(plot: list[Position]) -> dict[Vector, list[Position]]:
    results: dict[Vector, list[Position]] = defaultdict(list)
    for direction in directions:
        for position in plot:
            if position + direction not in plot:
                results[direction].append(position)
    return results


class Solution(StrSplitSolution):
    _year = 2024
    _day = 12

    @answer(1434856)
    def part_1(self) -> int:
        garden = Grid(self.input)
        return sum(split_into_plots(garden) | select(lambda p: len(p) * calculate_perimeter(p)))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
