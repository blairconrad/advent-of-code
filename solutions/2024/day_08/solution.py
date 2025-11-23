# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from collections import defaultdict
from functools import partial
from itertools import combinations
from typing import TYPE_CHECKING

from pipe import Pipe, chain, select, skip, take

from solutions.utils.grid import Grid, Position
from solutions.utils.iterables import tee

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable


def find_antennae(grid: Grid) -> Iterable[list[Position]]:
    antennae = defaultdict(list)
    for position, state in grid.enumerate():
        if state != ".":
            antennae[state].append(position)
    return antennae.values()


def get_antenna_pairs(antenna_set: list[Position]) -> list[tuple[Position, Position]]:
    return list(antenna_set | Pipe(combinations, 2))


def find_antinode_pairs(city: Grid, antenna_pair: tuple[Position, Position]) -> Iterable[Position]:
    diff = antenna_pair[1] - antenna_pair[0]
    step_length = 0

    antinodes = [None]  # dummy value to get in loop
    while len(antinodes) > 0:
        step = diff * step_length

        antinodes = []
        antinode = antenna_pair[0] - step
        if city.contains(antinode):
            antinodes.append(antinode)

        antinode = antenna_pair[1] + step
        if city.contains(antinode):
            antinodes.append(antinode)

        if len(antinodes) > 0:
            yield antinodes

        step_length += 1


def find_primary_antinode_pairs(city: Grid, antenna_pair: tuple[Position, Position]) -> Iterable[Position]:
    yield from find_antinode_pairs(city, antenna_pair) | skip(1) | take(1)


class Solution(StrSplitSolution):  # or TextSolution, etc
    _year = 2024
    _day = 8

    @answer(351)
    def part_1(self) -> int:
        city = Grid(self.input)
        return len(
            set(
                find_antennae(city)
                | select(get_antenna_pairs)
                | chain
                | select(partial(find_primary_antinode_pairs, city))
                | chain  # unpack results from pair of towers
                | chain  # unpack possible pairs of antinodes
                | tee(self.debug)
            )
        )

    @answer(1259)
    def part_2(self) -> int:
        city = Grid(self.input)
        return len(
            set(
                find_antennae(city)
                | select(get_antenna_pairs)
                | chain
                | select(partial(find_antinode_pairs, city))
                | chain  # unpack results from pair of towers
                | chain  # unpack possible pairs of antinodes
            )
        )
