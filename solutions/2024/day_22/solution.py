# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/22


from collections import defaultdict

from pipe import select

from ...base import IntSplitSolution, answer

FINGERPRINT_LENGTH = 4
Fingerprint = tuple[int, int, int, int]


def calculate_yields(secret: int) -> dict[Fingerprint, int]:
    fingerprint: tuple[int, ...] = ()

    yields: dict[fingerprint, int] = {}
    for _ in range(2000):
        price = secret % 10
        next_secret = calculate_next_secret(secret)
        next_price = next_secret % 10
        difference = next_price - price
        fingerprint = (*fingerprint[-(FINGERPRINT_LENGTH - 1) :], difference)
        if len(fingerprint) == FINGERPRINT_LENGTH:
            yields.setdefault(fingerprint, next_price)
        secret = next_secret

    return yields


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

    @answer(1784)
    def part_2(self) -> int:
        yields: dict[Fingerprint, int] = defaultdict(int)
        for secret in self.input:
            yields_for_buyer = calculate_yields(secret)
            for fingerprint, price in yields_for_buyer.items():
                yields[fingerprint] += price
        self.debug(len(yields), yields)
        return max(yields.values())
