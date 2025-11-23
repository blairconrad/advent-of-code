# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from dataclasses import dataclass
from heapq import heappop, heappush

from pipe import take

from solutions.utils.grid import CARDINAL_DIRECTIONS, Position, manhattan_distance
from solutions.utils.iterables import starmap
from solutions.utils.parsing import split_ints

from ...base import StrSplitSolution, answer


@dataclass()
class Path:
    cost: int
    positions: tuple[Position, ...]

    def __lt__(self, other: Path) -> bool:
        return self.cost < other.cost


class Solution(StrSplitSolution):
    _year = 2024
    _day = 18

    def find_shortest_path_length(self, grid_size: int, falling_bytes: set[Position]) -> int:
        start_position = Position(0, 0)
        end_position = Position(grid_size - 1, grid_size - 1)

        fringe = [Path(manhattan_distance(start_position, end_position), (start_position,))]
        seen = {start_position: fringe[0].cost}
        while fringe:
            current_path = heappop(fringe)
            self.debug(f"{len(fringe)},   {current_path.cost}")
            current_position = current_path.positions[-1]
            if current_position == end_position:
                self.debug(current_path)
                return current_path.cost

            for direction in CARDINAL_DIRECTIONS:
                next_position = current_position + direction
                next_cost = len(current_path.positions) + manhattan_distance(next_position, end_position)
                if (
                    0 <= next_position.row < grid_size
                    and 0 <= next_position.column < grid_size
                    and next_position not in falling_bytes
                    and (next_position not in seen or seen[next_position] > next_cost)
                ):
                    seen[next_position] = next_cost
                    heappush(fringe, Path(next_cost, (*current_path.positions, next_position)))
        return -1

    @answer(506)
    def part_1(self) -> int:
        grid_size = (6 if self.use_test_data else 70) + 1
        max_number_of_bytes = 12 if self.use_test_data else 1024
        falling_bytes = set(self.input | split_ints(",") | take(max_number_of_bytes) | starmap(Position))
        self.debug(falling_bytes)

        return self.find_shortest_path_length(grid_size, falling_bytes)

    @answer("62,6")
    def part_2(self) -> str:
        grid_size = (6 if self.use_test_data else 70) + 1
        all_falling_bytes = list(self.input | split_ints(",") | starmap(Position))
        self.debug(all_falling_bytes)

        highest_working = 0
        lowest_failing = len(all_falling_bytes) - 1
        while highest_working < lowest_failing - 1:
            try_num_bytes = (lowest_failing + highest_working) // 2
            self.debug(f"{highest_working, try_num_bytes, lowest_failing}")

            if self.find_shortest_path_length(grid_size, set(all_falling_bytes[:try_num_bytes])) == -1:
                lowest_failing = try_num_bytes
            else:
                highest_working = try_num_bytes
        return f"{all_falling_bytes[highest_working].row},{all_falling_bytes[highest_working].column}"
