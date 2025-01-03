# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from dataclasses import dataclass

from pipe import select

from ...base import TextSolution, answer


@dataclass
class File:
    id: int
    start: int
    length: int

    def weight(self) -> int:
        return int(self.id * self.length * (self.start + (self.length - 1) / 2))


@dataclass
class Space:
    start: int
    length: int


def parse_input(input_str: str) -> tuple[list[File], list[Space]]:
    files = []
    spaces = []

    block_sizes = input_str | select(int)
    is_file = True
    file_id = 0
    next_position = 0
    for block_size in block_sizes:
        if block_size > 0:
            if is_file:
                files.append(File(file_id, next_position, block_size))
                file_id += 1
            else:
                spaces.append(Space(next_position, block_size))

        next_position += block_size
        is_file = not is_file

    return (files, spaces)


def expand_files(files: list[File]) -> list[File]:
    expanded_files = []
    for file in files:
        expanded_files.extend([File(file.id, start, 1) for start in range(file.start, file.start + file.length)])
    return expanded_files


def pack(files: list[File], spaces: list[Space]) -> None:
    next_file_index = len(files) - 1
    while len(spaces) > 0 and spaces[0].start < files[next_file_index].start:
        for i in range(len(spaces)):
            if spaces[i].start > files[next_file_index].start:
                break
            if spaces[i].length == files[next_file_index].length:
                files[next_file_index].start = spaces[i].start
                spaces.pop(i)
                break
            if spaces[i].length > files[next_file_index].length:
                files[next_file_index].start = spaces[i].start
                spaces[i].start += files[next_file_index].length
                spaces[i].length -= files[next_file_index].length
                break
        next_file_index -= 1


class Solution(TextSolution):
    _year = 2024
    _day = 9

    @answer(6370402949053)
    def part_1(self) -> int:
        files, spaces = parse_input(self.input)
        self.debug(files)
        self.debug(spaces)
        files = expand_files(files)
        self.debug(files)
        pack(files, spaces)
        self.debug(files)
        return sum(files | select(File.weight))

    @answer(6398096697992)
    def part_2(self) -> int:
        files, spaces = parse_input(self.input)
        self.debug(files)
        self.debug(spaces)
        pack(files, spaces)
        self.debug(files)
        return sum(files | select(File.weight))
