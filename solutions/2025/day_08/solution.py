# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

import heapq
import operator
from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from typing import TYPE_CHECKING

from pipe import select, sort, take

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable


type Point = tuple[int, int, int]


@dataclass(order=True)
class Segment:
    distance: int
    point1: Point
    point2: Point


def read_points(input_lines: Iterable[str]) -> list[Point]:
    return list(input_lines | select(lambda line: tuple(line.split(",") | select(int))))


def euclidean_distance(p1: Point, p2: Point) -> int:
    return sum((a - b) ** 2 for a, b in zip(p1, p2, strict=True))


def merge_circuits(circuits: dict[Point, tuple[Point, ...]], p1: Point, p2: Point) -> None:
    circuit1 = circuits[p1]
    circuit2 = circuits[p2]
    if circuit1 is circuit2:
        return
    new_circuit = circuit1 + circuit2
    for point in new_circuit:
        circuits[point] = new_circuit
    return


class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    @answer(117000)
    def part_1(self) -> int:
        points = read_points(self.input)
        circuits: dict[Point, tuple[Point, ...]] = {point: (point,) for point in points}
        segments = list(
            combinations(points, 2) | select(lambda pair: Segment(euclidean_distance(pair[0], pair[1]), *pair))
        )
        heapq.heapify(segments)

        number_of_strings = (self.use_test_data and 10) or 1000

        for _ in range(number_of_strings):
            segment = heapq.heappop(segments)
            merge_circuits(circuits, segment.point1, segment.point2)

        return reduce(operator.mul, set(circuits.values()) | sort(key=len, reverse=True) | take(3) | select(len))

        return 0

    @answer(8368033065)
    def part_2(self) -> int:
        points = read_points(self.input)
        circuits: dict[Point, tuple[Point, ...]] = {point: (point,) for point in points}
        segments = list(
            combinations(points, 2) | select(lambda pair: Segment(euclidean_distance(pair[0], pair[1]), *pair))
        )
        heapq.heapify(segments)

        while True:
            segment = heapq.heappop(segments)
            merge_circuits(circuits, segment.point1, segment.point2)
            if len(circuits[segment.point1]) == len(points):
                break
        return segment.point1[0] * segment.point2[0]
