# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/17

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 17

    def print_state(self) -> None:
        self.debug((self.register_a, self.register_b, self.register_c))
        self.debug(self.format_instructions())
        self.debug(self.output_values)

    def format_instructions(self) -> str:
        steps = [str(i) for i in self.instructions]
        if self.next_instruction < len(steps):
            steps[self.next_instruction] = f"[{steps[self.next_instruction]}]"
        return " ".join(steps)

    def combo_value(self) -> int:
        literal_value = self.instructions[self.next_instruction + 1]
        match literal_value:
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
            case _:
                return literal_value

    def literal_value(self) -> int:
        return self.instructions[self.next_instruction + 1]

    def output(self, value: int) -> None:
        self.output_values.append(value)

    def do(self) -> None:
        match self.instructions[self.next_instruction]:
            case 0:  # adv
                self.register_a = self.register_a // 2 ** self.combo_value()
            case 1:  # bxl
                self.register_b ^= self.literal_value()
            case 2:  # bst
                self.register_b = self.combo_value() % 8
            case 3:  # jnz
                if self.register_a != 0:
                    self.next_instruction = self.literal_value() - 2  # to offset the usual jump
            case 4:  # bxc
                self.register_b ^= self.register_c
            case 5:  # out
                self.output(self.combo_value() % 8)
            case 6:  # bdv
                self.register_b = self.register_a // 2 ** self.combo_value()
            case _:  # cdv
                self.register_c = self.register_a // 2 ** self.combo_value()
        self.next_instruction += 2

    @answer("7,4,2,5,1,4,6,0,4")
    def part_1(self) -> str:
        self.register_a: int = int(self.input[0].split(":")[-1].strip())
        self.register_b: int = int(self.input[1].split(":")[-1].strip())
        self.register_c: int = int(self.input[2].split(":")[-1].strip())
        self.instructions = list(map(int, self.input[4].split(":")[-1].strip().split(",")))
        self.next_instruction = 0
        self.output_values: list[int] = []
        self.print_state()
        while self.next_instruction < len(self.instructions):
            self.do()
            self.print_state()
        return ",".join(map(str, self.output_values))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
