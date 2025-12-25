# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from dataclasses import dataclass
from itertools import combinations, pairwise, starmap
from typing import TYPE_CHECKING

from pipe import Pipe, select, where

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from solutions.utils.grid import Vector


@dataclass(frozen=True)
class Point:
    column: int
    row: int


def parse_point(point: str) -> Point:
    return Point(*(point.split(",") | select(int)))


@dataclass
class Rectangle:
    west: int
    east: int
    north: int
    south: int

    def __init__(self, corners: tuple[Point, Point]) -> None:
        self.west = min(corners[0].column, corners[1].column)
        self.east = max(corners[0].column, corners[1].column)
        self.north = min(corners[0].row, corners[1].row)
        self.south = max(corners[0].row, corners[1].row)

    def area(self) -> int:
        return (1 + self.east - self.west) * (1 + self.south - self.north)


@dataclass
class Edge:
    point1: Point
    point2: Point
    direction: Vector

    def __init__(self, p1: Point, p2: Point) -> None:
        if p1.column < p2.column or p1.row < p2.row:
            self.point1, self.point2 = p1, p2
        else:
            self.point1, self.point2 = p2, p1

    def pierces_rectangle(self, rectangle: Rectangle) -> bool:
        return (
            self.point1.row < rectangle.south
            and self.point2.row > rectangle.north
            and self.point1.column < rectangle.east
            and self.point2.column > rectangle.west
        )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    @answer(4748826374)
    def part_1(self) -> int:
        return max(
            self.input | select(parse_point) | Pipe(combinations, 2) | select(Rectangle) | select(Rectangle.area)
        )

    @answer(1554370486)
    def part_2(self) -> int:
        points = list(self.input | select(parse_point))
        edges = list(starmap(Edge, pairwise(points + points[0:1])))
        rectangles = sorted(combinations(points, 2) | select(Rectangle), reverse=True, key=Rectangle.area)

        return next(
            rectangles
            | where(lambda rect: all(not edge.pierces_rectangle(rect) for edge in edges))
            | select(Rectangle.area)
        )
