# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from pipe import select, traverse, where

from ...base import StrSplitSolution, answer

EXACTLY_TWO_CHUNKS = 2


def is_x_repeated_chunks(x: int, candidate: str) -> bool:
    chunk_length, leftover = divmod(len(candidate), x)
    return leftover == 0 and candidate == candidate[:chunk_length] * x


def repeated_chunk_count(candidate: int) -> int:
    candidate_str = str(candidate)
    try:
        return next(range(2, len(candidate_str) + 1) | where(lambda x: is_x_repeated_chunks(x, candidate_str)))
    except StopIteration:
        return 1


def parse_range(string_range: str) -> range:
    start, end = string_range.split("-")
    return range(int(start), int(end) + 1)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2

    separator = ","

    @answer(38310256125)
    def part_1(self) -> int:
        return sum(
            self.input | select(parse_range) | traverse | where(lambda s: repeated_chunk_count(s) == EXACTLY_TWO_CHUNKS)
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
