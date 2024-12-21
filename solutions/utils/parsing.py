from collections.abc import Iterable

from pipe import Pipe, select


@Pipe
def split_ints(seq: Iterable[str], separator: str | None = None) -> Iterable[tuple[int, ...]]:
    for s in seq:
        yield tuple(s.split(separator) | select(int))
