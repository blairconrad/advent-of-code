# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from collections.abc import Callable, Iterable
from functools import cmp_to_key, partial

from pipe import select, where

from ...base import TextSolution, answer

type Rule = tuple[int, int]
type Update = tuple[int, ...]


def parse_input(input_str: str) -> tuple[Iterable[Rule], Iterable[Update]]:
    rules_lines, updates_lines = input_str.strip().split("\n\n") | select(str.splitlines)
    return (
        list(rules_lines | select(int_tuple("|"))),
        updates_lines | select(int_tuple(",")),
    )


def int_tuple(separator: str) -> Callable[[str], tuple[int, ...]]:
    return lambda s: tuple(s.split(separator) | select(int))


def middle(seq: tuple[int]) -> int:
    return seq[len(seq) // 2]


def page_keyfunc(rules: Iterable[Rule]) -> Callable[[int], Any]:
    def _compare(a: int, b: int) -> int:
        for rule in rules:
            if rule[0] == a and rule[1] == b:
                return -1
            if rule[0] == b and rule[1] == a:
                return 1
        return 0

    return cmp_to_key(_compare)


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer(6034)
    def part_1(self) -> int:
        rules, updates = parse_input(self.input)
        sort_it = partial(sorted, key=page_keyfunc(rules))
        return sum(updates | where(lambda u: tuple(sort_it(u)) == u) | select(middle))

    @answer(6305)
    def part_2(self) -> int:
        rules, updates = parse_input(self.input)
        sort_it = partial(sorted, key=page_keyfunc(rules))
        return sum(updates | where(lambda u: tuple(sort_it(u)) != u) | select(sort_it) | select(middle))
