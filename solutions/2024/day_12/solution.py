# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from collections import defaultdict
from collections.abc import Iterable

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
        count_sides(segments_map[north], west, east)
        + count_sides(segments_map[south], west, east)
        + count_sides(segments_map[west], north, south)
        + count_sides(segments_map[east], north, south)
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
