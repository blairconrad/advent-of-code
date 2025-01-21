# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/23

import itertools
from collections import defaultdict
from functools import partial

from pipe import Pipe, select, where

from solutions.utils.iterables import how_many, tee

from ...base import StrSplitSolution, answer

pairs = Pipe(itertools.combinations, 2)


def might_have_chief(thruple: tuple[str, str, str]) -> bool:
    return any(thruple | select(lambda n: n.startswith("t")))


class Solution(StrSplitSolution):
    _year = 2024
    _day = 23

    @answer(1218)
    def part_1(self) -> int:
        connections = defaultdict(list)
        self.debug(self.input)
        links = sorted(self.input | select(partial(str.split, sep="-")) | select(sorted))
        for start, end in links:
            connections[start].append(end)
        self.debug(connections)
        thruples = []
        for start, ends in connections.items():
            for mid, end in ends | pairs | tee(self.debug):
                if end in connections.get(mid, []):
                    thruples.append((start, mid, end))
        self.debug(thruples)
        return how_many(thruples | where(might_have_chief))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
