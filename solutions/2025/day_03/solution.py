# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from functools import cache, partial

from pipe import select

from ...base import StrSplitSolution, answer


@cache
def get_max_joltage(num_batteries: int, bank: str) -> str:
    if num_batteries == 0:
        return ""
    if len(bank) == num_batteries:
        return bank
    return max(
        bank[0] + get_max_joltage(num_batteries - 1, bank[1:]),
        get_max_joltage(num_batteries, bank[1:]),
    )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    @answer(16842)
    def part_1(self) -> int:
        return sum(self.input | select(partial(get_max_joltage, 2)) | select(int))

    @answer(167523425665348)
    def part_2(self) -> int:
        return sum(self.input | select(partial(get_max_joltage, 12)) | select(int))
