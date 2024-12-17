# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from collections.abc import Iterable

from pipe import select, where

from ...base import TextSolution, answer

type Rule = tuple[int, int]
type Update = tuple[int, ...]


def parse_input(input_str: str) -> tuple[Iterable[Rule], Iterable[Update]]:
    rules_lines, updates_lines = input_str.strip().split("\n\n") | select(str.splitlines)
    return (
        list(rules_lines | select(lambda s: tuple(s.split("|") | select(int)))),
        updates_lines | select(lambda s: tuple(s.split(",") | select(int))),
    )


def find_valid(rules: Rule, updates: Iterable[Update]) -> Iterable[tuple[int, ...]]:
    return updates | where(lambda u: is_valid(u, rules))


def is_valid(update: Update, rules: Rule) -> bool:
    if len(update) == 0:
        return True
    for rule in rules:
        if contravenes(update, rule):
            return False
    return is_valid(update[1:], rules)


def contravenes(update: Update, rule: Rule) -> bool:
    return rule[1] == update[0] and rule[0] in update


def middle(seq: Iterable[int]) -> int:
    return seq[len(seq) // 2]


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer(6034)
    def part_1(self) -> int:
        rules, updates = parse_input(self.input)
        return sum(find_valid(rules, updates) | select(middle))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
