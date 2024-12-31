# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from collections.abc import Callable, Iterable
from operator import mul
from typing import Any

from pipe import Pipe, select
from pipe import enumerate as pipe_enumerate

from ...base import TextSolution, answer


def expand_blocks(blocks: Iterable[int]) -> Iterable[int | None]:
    expanded_blocks = []
    is_file = True
    file_number = 0
    for block in blocks:
        if is_file:
            expanded_blocks += [file_number] * block
            file_number += 1
            is_file = False
        else:
            expanded_blocks += [None] * block
            is_file = True
    return expanded_blocks


def pack(expanded_blocks: list[int | None]) -> list[int | None]:
    insert_index = 0

    while insert_index < len(expanded_blocks):
        if expanded_blocks[insert_index] is not None:
            insert_index += 1
            continue
        if expanded_blocks[-1] is None:
            expanded_blocks.pop(-1)
            continue
        expanded_blocks[insert_index] = expanded_blocks.pop(-1)
        insert_index += 1

    return expanded_blocks


@Pipe
def starmap(iterable: Iterable[tuple[Any, ...]], func: Callable[[tuple[Any, ...]], Any]) -> Iterable[int]:
    for args in iterable:
        yield func(*args)


class Solution(TextSolution):
    _year = 2024
    _day = 9

    @answer(6370402949053)
    def part_1(self) -> int:
        blocks = self.input | select(int)
        expanded_blocks = expand_blocks(blocks)
        self.debug(expanded_blocks)

        packed_blocks = pack(expanded_blocks)
        self.debug(packed_blocks)

        return sum(packed_blocks | pipe_enumerate | starmap(mul))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
