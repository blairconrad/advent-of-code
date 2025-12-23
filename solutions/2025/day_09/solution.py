# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from dataclasses import dataclass
from itertools import combinations, starmap

from pipe import Pipe, select

from ...base import StrSplitSolution, answer


@dataclass(frozen=True)
class Point:
    column: int
    row: int


def parse_point(point: str) -> Point:
    return Point(*(point.split(",") | select(int)))


def area(point1: Point, point2: Point) -> int:
    return abs(1 + point1.column - point2.column) * abs(1 + point1.row - point2.row)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    @answer(4748826374)
    def part_1(self) -> int:
        return max(
            self.input | select(parse_point) | Pipe(combinations, 2) | Pipe(lambda iterable: starmap(area, iterable))
        )

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
