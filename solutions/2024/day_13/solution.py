# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from re import DOTALL, findall
from typing import Any

from pipe import Pipe, select, where

from solutions.utils.iterables import tee

from ...base import TextSolution, answer


@Pipe
def starmap(iterable: Iterable[tuple[Any, ...]], func: Callable[[tuple[Any, ...]], Any]) -> Iterable[int]:
    for args in iterable:
        yield func(*args)


@dataclass
class ClawRound:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int

    def find_solutions(self) -> list[tuple[int, int]]:
        a = 0
        x = 0
        y = 0
        solutions = []
        while x <= self.prize_x and y <= self.prize_y:
            b_div, b_mod = divmod(self.prize_x - x, self.b_x)
            if b_mod == 0 and b_div * self.b_y == self.prize_y - y:
                solutions.append((a, b_div))

            a += 1
            x += self.a_x
            y += self.a_y
        return solutions


def cheapest_cost(solutions: list[tuple[int, int]]) -> int:
    def cost(solution: tuple[int, int]) -> int:
        return 3 * solution[0] + solution[1]

    return min(solutions | select(cost))


class Solution(TextSolution):
    _year = 2024
    _day = 13

    @answer(31897)
    def part_1(self) -> int:
        return sum(
            findall(
                r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
                self.input,
                DOTALL,
            )
            | select(lambda x: [int(i) for i in x])
            | starmap(ClawRound)
            | tee(self.debug)
            | select(ClawRound.find_solutions)
            | where(bool)
            | tee(self.debug)
            | select(cheapest_cost)
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
