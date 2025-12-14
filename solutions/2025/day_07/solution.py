# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from functools import Placeholder, partial
from itertools import accumulate
from typing import TYPE_CHECKING, TypeVar

from pipe import Pipe, select

from ...base import StrSplitSolution, answer

if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterable

SPLIT: str = "*"
BEAM: str = "S"
A_SPLIT_BEAM = BEAM + SPLIT + BEAM

count_splits = partial(str.count, Placeholder, SPLIT)


def advance(this_line: str, next_line: str) -> str:
    new_next_line = next_line
    for i in range(len(this_line)):
        if this_line[i] == BEAM:
            if next_line[i] == "^":
                new_next_line = new_next_line[: i - 1] + A_SPLIT_BEAM + new_next_line[i + 2 :]
            else:
                new_next_line = new_next_line[:i] + BEAM + new_next_line[i + 1 :]
    return new_next_line


T = TypeVar("T")


@Pipe
def tee(iterable: Iterable[T], printer: Callable[[T], None]) -> Generator[T]:
    for item in iterable:
        printer(item)
        yield item


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    @answer(1518)
    def part_1(self) -> int:
        return sum(accumulate(self.input, advance) | tee(self.debug) | select(count_splits))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
