from collections.abc import Callable, Iterable
from typing import Any

from pipe import Pipe


def how_many(iterable: Iterable[int]) -> int:
    return sum(1 for i in iterable)


@Pipe
def tee(iterable: Iterable, output: Callable[[Any], None]) -> Iterable:
    """Pass each item in the iterable to the output function and yield the item."""
    for item in iterable:
        output(item)
        yield item
