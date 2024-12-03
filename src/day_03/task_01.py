# Standard Library
import re


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        pattern = re.compile("(mul\\((\\d{1,3}),(\\d{1,3})\\))")

        total = 0
        for line in file_content:
            mul_instructions = pattern.findall(line)

            for instruction in mul_instructions:
                result = cls.process_instruction(instruction)
                total = total + result

        return total

    @classmethod
    def process_instruction(cls, instruction: tuple[str, str]) -> int:
        result = 0
        if len(instruction) == 3:
            result = int(instruction[1]) * int(instruction[2])
        return result
