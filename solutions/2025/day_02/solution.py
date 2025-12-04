# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from pipe import select, traverse, where

from ...base import StrSplitSolution, answer


def is_repeated_chunk(candidate: str) -> bool:
    chunk_length, leftover = divmod(len(candidate), 2)
    return leftover == 0 and candidate == 2 * candidate[:chunk_length]


def is_invalid(candidate: int) -> bool:
    return is_repeated_chunk(str(candidate))


def parse_range(string_range: str) -> range:
    start, end = string_range.split("-")
    return range(int(start), int(end) + 1)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2

    separator = ","

    @answer(38310256125)
    def part_1(self) -> int:
        return sum(self.input | select(parse_range) | traverse | where(is_invalid))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
