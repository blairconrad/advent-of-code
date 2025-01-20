# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/22


from pipe import select

from ...base import IntSplitSolution, answer


def advance(secret: int) -> int:
    for _ in range(2000):
        secret = calculate_next_secret(secret)
    return secret


def calculate_next_secret(secret: int) -> int:
    secret = (secret << 6) ^ secret
    secret = secret & 0xFFFFFF
    secret = (secret >> 5) ^ secret
    secret = secret & 0xFFFFFF
    secret = (secret << 11) ^ secret
    return secret & 0xFFFFFF


class Solution(IntSplitSolution):
    _year = 2024
    _day = 22

    @answer(15613157363)
    def part_1(self) -> int:
        self.debug(self.input)
        return sum(self.input | select(advance))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
