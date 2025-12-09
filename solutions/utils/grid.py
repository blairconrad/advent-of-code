from dataclasses import dataclass
from typing import TYPE_CHECKING, Self, overload

if TYPE_CHECKING:
    from collections.abc import Iterable


@dataclass(frozen=True)
class Vector:
    row_change: int
    column_change: int

    def turn_left(self) -> Self:
        return Vector(-self.column_change, self.row_change)

    def turn_right(self) -> Self:
        return Vector(self.column_change, -self.row_change)

    def turn_around(self) -> Self:
        return self * -1

    def __add__(self, other: Self) -> Self:
        return Vector(self.row_change + other.row_change, self.column_change + other.column_change)

    def __mul__(self, scalar: int) -> Self:
        return Vector(self.row_change * scalar, self.column_change * scalar)


NORTH = Vector(-1, 0)
EAST = Vector(0, 1)
SOUTH = Vector(1, 0)
WEST = Vector(0, -1)

CARDINAL_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)


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


@dataclass(frozen=True)
class Pose:
    position: Position
    direction: Vector


class Grid:
    def __init__(self, grid: list[str]) -> None:
        self.grid = grid[:]

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

    def find(self, target: str) -> Position:
        for position, value in self.enumerate():
            if value == target:
                return position
        message = f"{target} not found in grid"
        raise ValueError(message)

    def __repr__(self) -> str:
        return "\n".join(self.grid)


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a.row - b.row) + abs(a.column - b.column)
