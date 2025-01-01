# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from collections.abc import Iterable
from dataclasses import dataclass

from pipe import select

from solutions.utils.grid import Grid, Position, Vector

from ...base import StrSplitSolution, answer


@dataclass
class PlotStats:
    area: int
    perimeter: int


directions: tuple[Vector, Vector, Vector, Vector] = (Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0))


def survey_plot(seen: set[Position], start: Position, grid: Grid) -> PlotStats:
    plot: set[Position] = set()
    fringe = {start}
    perimeter = 0

    while len(fringe) > 0:
        position = fringe.pop()
        if position in plot:
            continue

        plot.add(position)
        plot_type = grid[position]
        for direction in directions:
            neighbour_position = position + direction
            neighbour_type = grid.get(neighbour_position, None)

            if neighbour_type is None or neighbour_type != plot_type:
                perimeter += 1
                continue

            fringe.add(neighbour_position)

    seen |= plot
    return PlotStats(len(plot), perimeter=perimeter)


def describe_plots(grid: Grid) -> Iterable[PlotStats]:
    seen: set[Position] = set()
    plot_stats = []
    for position in grid.positions():
        if position in seen:
            continue
        plot_stats.append(survey_plot(seen, position, grid))
    return plot_stats


class Solution(StrSplitSolution):
    _year = 2024
    _day = 12

    @answer(1434856)
    def part_1(self) -> int:
        garden = Grid(self.input)
        return sum(describe_plots(garden) | select(lambda plot: plot.area * plot.perimeter))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
