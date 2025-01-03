# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

from collections.abc import Callable
from dataclasses import dataclass
from re import DOTALL, findall

from pipe import select, where

from solutions.utils.iterables import tee

from ...base import TextSolution, answer
from ...utils.iterables import starmap


@dataclass
class ClawRound:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int

    def find_solutions(self) -> list[tuple[int, int]]:
        a, remainder = divmod(
            self.b_y * self.prize_x - self.b_x * self.prize_y, self.a_x * self.b_y - self.a_y * self.b_x
        )
        if remainder != 0:
            return []
        b = (self.prize_x - a * self.a_x) // self.b_x
        return [(a, b)]


def cheapest_cost(solutions: list[tuple[int, int]]) -> int:
    def cost(solution: tuple[int, int]) -> int:
        return 3 * solution[0] + solution[1]

    return min(solutions | select(cost))


def shift_it(claw_round: ClawRound) -> ClawRound:
    claw_round.prize_x += 10000000000000
    claw_round.prize_y += 10000000000000
    return claw_round


class Solution(TextSolution):
    _year = 2024
    _day = 13

    def find_cheapest(self, round_transform: Callable[[ClawRound], ClawRound]) -> int:
        return sum(
            findall(
                r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
                self.input,
                DOTALL,
            )
            | select(lambda x: [int(i) for i in x])
            | starmap(ClawRound)
            | select(round_transform)
            | tee(self.debug)
            | select(ClawRound.find_solutions)
            | where(bool)
            | tee(self.debug)
            | select(cheapest_cost)
        )

    @answer(31897)
    def part_1(self) -> int:
        return self.find_cheapest(lambda x: x)

    @answer(87596249540359)
    def part_2(self) -> int:
        return self.find_cheapest(shift_it)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
