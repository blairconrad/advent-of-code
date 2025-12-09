
from typing import TYPE_CHECKING

from pipe import Pipe, select

if TYPE_CHECKING:
    from collections.abc import Iterable


@Pipe
def split_ints(seq: Iterable[str], separator: str | None = None) -> Iterable[tuple[int, ...]]:
    for s in seq:
        yield tuple(s.split(separator) | select(int))
