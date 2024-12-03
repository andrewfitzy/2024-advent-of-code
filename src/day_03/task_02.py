# Standard Library
import re


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        pattern = re.compile("(mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\)|don't\\(\\))")

        perform_operation = True
        total = 0
        for line in file_content:
            mul_instructions = pattern.findall(line)

            for instruction in mul_instructions:
                if instruction[0].startswith("don't"):
                    perform_operation = False
                elif instruction[0].startswith("do"):
                    perform_operation = True
                else:
                    if perform_operation:
                        result = cls.process_instruction(instruction)
                        total = total + result

        return total

    @classmethod
    def process_instruction(cls, instruction: tuple[str]) -> int:
        result = 0
        if len(instruction) == 3:
            result = int(instruction[1]) * int(instruction[2])
        return result
