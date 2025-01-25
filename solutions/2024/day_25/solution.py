# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/25

from dataclasses import dataclass

from pipe import select, where

from solutions.utils.iterables import how_many

from ...base import TextSolution, answer


@dataclass
class Lock:
    height: int
    pins: list[int]


@dataclass
class Key:
    pins: list[int]

    def might_fit(self, lock: Lock) -> bool:
        return all(self.pins[i] + lock.pins[i] <= lock.height for i in range(5))


def parse_input(input_str: str) -> tuple[list[Key], list[Lock]]:
    keys = []
    locks = []
    blocks = input_str.split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        height = len(lines) - 2
        pin_heights = [0] * 5
        for line in lines[1:-1]:
            for i, char in enumerate(line):
                if char == "#":
                    pin_heights[i] += 1

        if lines[0] == ".....":
            keys.append(Key(pin_heights))
        else:
            locks.append(Lock(height, pin_heights))
    return keys, locks


class Solution(TextSolution):
    _year = 2024
    _day = 25

    @answer(3127)
    def part_1(self) -> int:
        keys, locks = parse_input(self.input)
        self.debug(keys)
        self.debug(locks)

        return sum(keys | select(lambda key: how_many(locks | where(key.might_fit))))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
