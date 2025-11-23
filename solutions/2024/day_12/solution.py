# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from collections import defaultdict
from typing import TYPE_CHECKING

from pipe import select

from solutions.utils.grid import CARDINAL_DIRECTIONS, EAST, NORTH, SOUTH, WEST, Grid, Position, Vector

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable


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
            for direction in CARDINAL_DIRECTIONS:
                neighbour_position = position + direction
                if garden.contains(neighbour_position) and garden[neighbour_position] == plot_type:
                    fringe.add(neighbour_position)

        seen |= set(plot)
        yield plot


def calculate_perimeter_segments(plot: list[Position]) -> dict[Vector, list[Position]]:
    results: dict[Vector, list[Position]] = defaultdict(list)
    for direction in CARDINAL_DIRECTIONS:
        for position in plot:
            if position + direction not in plot:
                results[direction].append(position)
    return results


def calculate_perimeter(plot: list[Position]) -> int:
    return sum(calculate_perimeter_segments(plot).values() | select(len))


def calculate_number_of_sides(plot: list[Position]) -> int:
    segments_map = calculate_perimeter_segments(plot)

    def count_sides(segments: list[Position], start_direction: Vector, end_direction: Vector) -> int:
        count = 0
        while len(segments) > 0:
            first_segment = last_segment = segments.pop()
            count += 1
            while (first_segment := first_segment + start_direction) in segments:
                segments.remove(first_segment)
            while (last_segment := last_segment + end_direction) in segments:
                segments.remove(last_segment)
        return count

    return (
        count_sides(segments_map[NORTH], WEST, EAST)
        + count_sides(segments_map[SOUTH], WEST, EAST)
        + count_sides(segments_map[WEST], NORTH, SOUTH)
        + count_sides(segments_map[EAST], NORTH, SOUTH)
    )


class Solution(StrSplitSolution):
    _year = 2024
    _day = 12

    @answer(1434856)
    def part_1(self) -> int:
        garden = Grid(self.input)
        return sum(split_into_plots(garden) | select(lambda p: len(p) * calculate_perimeter(p)))

    @answer(891106)
    def part_2(self) -> int:
        garden = Grid(self.input)
        for plot in split_into_plots(garden):
            self.debug(plot)
        return sum(split_into_plots(garden) | select(lambda p: len(p) * calculate_number_of_sides(p)))
