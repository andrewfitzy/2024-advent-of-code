# Standard Library
import types

boolean = types.SimpleNamespace()
boolean.XOR = "XOR"
boolean.AND = "AND"
boolean.OR = "OR"

register = types.SimpleNamespace()
register.X = "x"
register.Y = "y"
register.Z = "z"


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> str:
        process_inputs = True
        inputs = {}
        connections = {}
        for line in file_content:
            if len(line) == 0:
                process_inputs = False
                continue

            if process_inputs:
                input_parts = line.split(": ")
                inputs[input_parts[0]] = int(input_parts[1])
                continue

            input_parts = line.split(" ")
            operation = (input_parts[0], input_parts[1], input_parts[2])
            connections[input_parts[4]] = operation
            if input_parts[4] not in inputs:
                inputs[input_parts[4]] = -1

        output = cls.process(inputs=inputs, connections=connections)
        output.sort()
        return ",".join(output)

    @classmethod
    def process(cls, inputs: dict[str, int], connections: dict[str, tuple[str, str, str]]) -> list[str]:
        # I couldn't do this one so took inspiration from a Java solution I found and converted it into Python
        #
        # Original code is here:
        # https://github.com/ash42/adventofcode/blob/main/adventofcode2024/src/nl/michielgraat/adventofcode2024/day24/Day24.java
        #
        # Props to the author, [ash42](https://github.com/ash42) for making this available
        #
        # The Algorithm for finding the incorrect wires.
        #
        # There are 4 cases in which is faulty:
        # 1. If there is output to a z-wire, the operator should always be XOR (unless it is the final bit). If not -> faulty.
        # 2. If the output is not a z-wire and the inputs are not x and y, the operator should always be AND or OR. If not -> faulty.
        # 3. If the inputs are x and y (but not the first bit) and the operator is XOR, the output wire should be the input of another XOR-gate. If not -> faulty.
        # 4. If the inputs are x and y (but not the first bit) and the operator is AND, the output wire should be the input of an OR-gate. If not -> faulty.

        registers = list(inputs.keys())
        registers.sort()
        most_significant_z = registers[-1]

        incorrect_registers = []
        for output_register, operation in connections.items():
            left_operand, operator, right_operand = operation
            if (
                output_register.startswith(register.Z)
                and operator != boolean.XOR
                and output_register != most_significant_z
            ):
                incorrect_registers.append(output_register)
                continue

            if (
                not output_register.startswith(register.Z)
                and not (left_operand.startswith(register.X) or left_operand.startswith(register.Y))
                and not (right_operand.startswith(register.X) or right_operand.startswith(register.Y))
            ):
                if operator == boolean.XOR:
                    incorrect_registers.append(output_register)
                    continue

            if (
                operator == boolean.XOR
                and (left_operand.startswith(register.X) or left_operand.startswith(register.Y))
                and (right_operand.startswith(register.X) or right_operand.startswith(register.Y))
            ):
                if not (left_operand.endswith("00") and right_operand.endswith("00")):
                    another_found = False
                    for tmp_output_register, tmp_operation in connections.items():
                        tmp_left_operand, tmp_operator, tmp_right_operand = tmp_operation
                        if operation != tmp_operation:
                            if (
                                tmp_left_operand == output_register or tmp_right_operand == output_register
                            ) and tmp_operator == boolean.XOR:
                                another_found = True
                                break

                    if not another_found:
                        incorrect_registers.append(output_register)
                        continue

            if (
                operator == boolean.AND
                and (left_operand.startswith(register.X) or left_operand.startswith(register.Y))
                and (right_operand.startswith(register.X) or right_operand.startswith(register.Y))
            ):
                if not (left_operand.endswith("00") and right_operand.endswith("00")):
                    another_found = False
                    for tmp_output_register, tmp_operation in connections.items():
                        tmp_left_operand, tmp_operator, tmp_right_operand = tmp_operation
                        if operation != tmp_operation:
                            if (
                                tmp_left_operand == output_register or tmp_right_operand == output_register
                            ) and tmp_operator == boolean.OR:
                                another_found = True
                                break

                    if not another_found:
                        incorrect_registers.append(output_register)
                        continue

        return incorrect_registers
