from collections.abc import Iterable
from dataclasses import dataclass
from typing import Self, overload


@dataclass(frozen=True)
class Vector:
    row_change: int
    column_change: int

    def __mul__(self, scalar: int) -> Self:
        return Vector(self.row_change * scalar, self.column_change * scalar)


@dataclass(frozen=True)
class Position:
    row: int
    column: int

    def __add__(self, pos: Vector) -> Self:
        return Position(self.row + pos.row_change, self.column + pos.column_change)

    @overload
    def __sub__(self, position: Self) -> Vector: ...

    @overload
    def __sub__(self, vector: Vector) -> Self: ...

    def __sub__(self, other):
        match other:
            case Position(row, column):
                return Vector(self.row - row, self.column - column)
            case Vector(row_change, column_change):
                return Position(self.row - row_change, self.column - column_change)


class Grid:
    def __init__(self, grid: list[str]) -> None:
        self.grid = grid

    def __getitem__(self, key: Position) -> str:
        return self.grid[key.row][key.column]

    def __setitem__(self, key: Position, value: str) -> None:
        self.grid[key.row] = self.grid[key.row][: key.column] + value + self.grid[key.row][key.column + 1 :]

    def enumerate(self) -> Iterable[tuple[Position, str]]:
        return (
            (Position(row, column), self.grid[row][column])
            for row in range(len(self.grid))
            for column in range(len(self.grid[row]))
        )

    def positions(self) -> Iterable[Position]:
        return (Position(row, column) for row in range(len(self.grid)) for column in range(len(self.grid[row])))

    def contains(self, position: Position) -> bool:
        return 0 <= position.row < len(self.grid) and 0 <= position.column < len(self.grid[position.row])

    def get(self, position: Position, default: str | None) -> str | None:
        return self[position] if self.contains(position) else default

    def __repr__(self) -> str:
        return "\n".join(self.grid)
