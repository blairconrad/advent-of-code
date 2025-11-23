# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/21

from functools import cache
from typing import TYPE_CHECKING

from pipe import select

from solutions.utils.grid import Grid, Position

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Iterable

ACTIVATE = "A"
number_pad = Grid(["789", "456", "123", " 0A"])
arrow_pad = Grid([" ^A", "<v>"])


def column_move(change: int) -> str:
    return ">" * change if change > 0 else "<" * -change


def row_move(change: int) -> str:
    return "v" * change if change > 0 else "^" * -change


def find_paths_between(pad: Grid, start: Position, end: Position) -> list[str]:
    if start == end:
        return ["A"]

    diff = end - start
    row_path = row_move(diff.row_change)
    col_path = column_move(diff.column_change)
    if not col_path:
        return [row_path + "A"]

    if not row_path:
        return [col_path + "A"]

    paths = []
    if pad[Position(end.row, start.column)] != " ":
        paths.append(row_path + col_path + "A")
    if pad[Position(start.row, end.column)] != " ":
        paths.append(col_path + row_path + "A")
    return paths


def find_all_paths(pad: Grid, keys: str) -> list[str]:
    start_key = ACTIVATE
    start_position = pad.find(start_key)
    paths = [""]
    for next_key in keys:
        next_position = pad.find(next_key)
        new_paths = find_paths_between(pad, start_position, next_position)
        paths = [path + new_path for path in paths for new_path in new_paths]
        start_key = next_key
        start_position = next_position
    return paths


def segmentize(path: str) -> Iterable[str]:
    start = 0
    while start < len(path):
        a_index = path.find("A", start)
        yield path[start : a_index + 1]
        start = a_index + 1


def find_shortest_length_for_path(path: str, depth: int) -> int:
    return sum(segmentize(path) | select(lambda segment: find_shortest_length_for_segment(segment, depth)))


@cache
def find_shortest_length_for_segment(segment: str, depth: int) -> int:
    if depth == 0:
        return len(segment)

    expanded_paths = find_all_paths(arrow_pad, segment)
    return min(expanded_paths | select(lambda path: find_shortest_length_for_path(path, depth - 1)))


class Solution(StrSplitSolution):
    _year = 2024
    _day = 21

    def find_min_steps_to_save_human(self, number_of_robots: int) -> int:
        total = 0
        for line in self.input:
            value = int(line[:-1], 10)
            cost = min(
                find_all_paths(number_pad, line)
                | select(lambda path: find_shortest_length_for_path(path, number_of_robots))
            )
            total += value * cost
        return total

    @answer(128962)
    def part_1(self) -> int:
        return self.find_min_steps_to_save_human(2)

    @answer(159684145150108)
    def part_2(self) -> int:
        return self.find_min_steps_to_save_human(25)
