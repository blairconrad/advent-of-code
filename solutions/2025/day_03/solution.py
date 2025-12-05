# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from functools import partial

from pipe import select

from ...base import StrSplitSolution, answer


def get_max_joltage(num_batteries: int, bank: str) -> int:
    if num_batteries == 1:
        return int(max(bank))

    j = "0"
    j_index = -1
    for index in range(len(bank) - num_batteries + 1):
        if bank[index] > j:
            j = bank[index]
            j_index = index
    return 10 ** (num_batteries - 1) * int(j) + get_max_joltage(
        num_batteries=num_batteries - 1, bank=bank[j_index + 1 :]
    )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    @answer(16842)
    def part_1(self) -> int:
        return sum(self.input | select(partial(get_max_joltage, 2)))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
