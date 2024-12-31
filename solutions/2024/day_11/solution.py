# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from ...base import IntSplitSolution, answer


def split_int(n: int) -> list[int] | None:
    digits = str(n)
    if len(digits) % 2 == 1:
        return None
    first_half = digits[: len(digits) // 2]
    second_half = digits[len(digits) // 2 :].lstrip("0")
    if second_half == "":
        second_half = "0"
    return [int(first_half), int(second_half)]


def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif (parts := split_int(stone)) is not None:
            new_stones.extend(parts)
        else:
            new_stones.append(stone * 2024)
    return new_stones


class Solution(IntSplitSolution):
    _year = 2024
    _day = 11

    separator = " "

    @answer(216996)
    def part_1(self) -> int:
        stones = self.input
        self.debug(stones)
        for _ in range(25):
            stones = blink(stones)
            self.debug(stones)
        return len(stones)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
