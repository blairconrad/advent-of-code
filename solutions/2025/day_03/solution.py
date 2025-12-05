# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from pipe import select

from ...base import StrSplitSolution, answer


def get_max_joltage(bank: str) -> int:
    j1 = "0"
    j1_index = -1
    for index1 in range(len(bank) - 1):
        if bank[index1] > j1:
            j1 = bank[index1]
            j1_index = index1
    j2 = max(bank[j1_index + 1 :])
    return 10 * int(j1) + int(j2)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    @answer(16842)
    def part_1(self) -> int:
        return sum(self.input | select(get_max_joltage))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
