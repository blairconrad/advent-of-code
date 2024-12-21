from collections.abc import Iterable


def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)
