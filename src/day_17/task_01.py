# Standard Library
import math
import operator


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> str:
        registers = {}
        program = []

        for line in file_content:
            # first skip empty lines
            if len(line.strip()) == 0:
                continue

            # Then process program as this in on one line
            if line.startswith("Program"):
                parts = line.strip().split(" ")
                program = [int(value) for value in parts[len(parts) - 1].split(",")]
                continue

            # Finally process registers
            parts = line.strip().split(" ")
            register = parts[1].replace(":", "")
            registers[register] = int(parts[len(parts) - 1])

        result, out_registers = cls.run_program(registers, program)
        return result

    @classmethod
    def get_combo_operand(cls, operand: int, registers: dict[str, int]) -> int:
        if operand >= 0 and operand <= 3:
            return operand
        if operand == 4:
            return registers["A"]
        if operand == 5:
            return registers["B"]
        if operand == 6:
            return registers["C"]
        raise ValueError("Expected operand in the range 0-6, received {operand}".format(operand=operand))

    @classmethod
    def run_program(cls, registers: dict[str, int], program: list[int]) -> tuple[str, dict[str, int]]:
        output: list[str] = []
        pointer = 0
        run_registers = registers.copy()
        while pointer < len(program):
            opcode = program[pointer]
            operand = program[pointer + 1]

            if opcode == 0:
                # adv
                numerator = run_registers["A"]
                denominator = 2 ** cls.get_combo_operand(operand, run_registers)
                run_registers["A"] = math.trunc(numerator / denominator)
            if opcode == 1:
                # bxl
                run_registers["B"] = operator.xor(operand, run_registers["B"])
            if opcode == 2:
                # bst
                run_registers["B"] = cls.get_combo_operand(operand, run_registers) % 8
            if opcode == 3:
                # jnz
                if run_registers["A"] != 0:
                    pointer = operand
                    continue
            if opcode == 4:
                # bxc
                run_registers["B"] = operator.xor(run_registers["C"], run_registers["B"])
            if opcode == 5:
                # out
                output.append(str(cls.get_combo_operand(operand, run_registers) % 8))
            if opcode == 6:
                # bdv
                numerator = run_registers["A"]
                denominator = 2 ** cls.get_combo_operand(operand, run_registers)
                run_registers["B"] = math.trunc(numerator / denominator)
            if opcode == 7:
                # cdv
                numerator = run_registers["A"]
                denominator = 2 ** cls.get_combo_operand(operand, run_registers)
                run_registers["C"] = math.trunc(numerator / denominator)

            pointer = pointer + 2

        return (",".join(output), run_registers)
