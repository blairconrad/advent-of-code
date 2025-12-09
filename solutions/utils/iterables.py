from typing import TYPE_CHECKING, Any

from pipe import Pipe

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def how_many(iterable: Iterable[Any]) -> int:
    return sum(1 for i in iterable)


@Pipe
def starmap(iterable: Iterable[tuple[Any, ...]], func: Callable[[tuple[Any, ...]], Any]) -> Iterable[int]:
    for args in iterable:
        yield func(*args)


@Pipe
def tee(iterable: Iterable, output: Callable[[Any], None]) -> Iterable:
    """Pass each item in the iterable to the output function and yield the item."""
    for item in iterable:
        output(item)
        yield item
