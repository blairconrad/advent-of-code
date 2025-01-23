# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/24

import operator
import re
from collections.abc import Callable

from ...base import StrSplitSolution, answer

operators = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

value_funcs = {"0": lambda: 0, "1": lambda: 1}


class Operation:
    def __init__(self, computer: dict[str, Callable], in_register1: str, operator: str, in_register2: str) -> None:
        self.computer = computer
        self.in_register1 = in_register1
        self.operator = operator
        self.in_register2 = in_register2

    def __call__(self) -> int:
        return operators[self.operator](self.computer[self.in_register1](), self.computer[self.in_register2]())


class Solution(StrSplitSolution):
    _year = 2024
    _day = 24

    @answer(53755311654662)
    def part_1(self) -> int:
        computer = {}
        for line in self.input:
            if match := re.match(r"^(?P<register>\S+): (?P<value>[01])$", line):
                value = computer[match.group("register")] = value_funcs[match.group("value")]
            elif match := re.match(
                r"^(?P<in_register1>\S+) (?P<operator>[A-Z]+) (?P<in_register2>\S+)" " -> " r"(?P<out_register>\S+)$",
                line,
            ):
                self.debug(match.groupdict())
                computer[match.group("out_register")] = Operation(
                    computer,
                    match.group("in_register1"),
                    match.group("operator"),
                    match.group("in_register2"),
                )
        self.debug(computer)

        total = 0
        for key, value in computer.items():
            if key.startswith("z"):
                total += value() << int(key[1:])

        return total

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
