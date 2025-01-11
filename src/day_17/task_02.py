# Standard Library
import math
import operator


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        program = []

        for line in file_content:
            # We only care about the program this time round
            if line.startswith("Program"):
                parts = line.strip().split(" ")
                program = [int(value) for value in parts[len(parts) - 1].split(",")]
                break

        result = cls.find_quine(program)
        return result

    @classmethod
    def find_quine(cls, program: list[int]) -> int:
        """
        The output is the program itself
        https://en.wikipedia.org/wiki/Quine_(computing)

        There are no shortcuts for brute forcing this, to generate a 16 digit output means that register A needs to be in the range 35184372088832 to
        281474976710655, this means 246,290,604,621,823 possible iterations :(

        This problem would never have been done without the excellent video by Wekoslav Stefanovski: https://youtu.be/QpvAyg1RIYI?si=Adiw2hbi8DNvVE-5.
        The video provides a good explanation of the solution and it also reasonably easy to follow.
        """
        register_a = 0
        for index in reversed(range(len(program))):
            register_a <<= 3

            registers = {}
            registers["A"] = register_a
            registers["B"] = 0
            registers["C"] = 0

            output, _ = cls.run_program(registers=registers, program=program)

            while output != program[index:]:
                register_a = register_a + 1

                registers = {}
                registers["A"] = register_a
                registers["B"] = 0
                registers["C"] = 0

                output, _ = cls.run_program(registers=registers, program=program)

        return register_a

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
    def run_program(cls, registers: dict[str, int], program: list[int]) -> tuple[list[int], dict[str, int]]:
        output: list[int] = []
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
                output.append(cls.get_combo_operand(operand, run_registers) % 8)
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

        return (output, run_registers)
