# Standard Library
import itertools


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        total_calibration_result = 0
        invalid_inputs = []
        for line in file_content:
            parts = line.split(":")
            answer = int(parts[0])

            txt_operands = parts[1].strip().split(" ")
            operands = [int(part) for part in txt_operands]

            combos = cls.get_operator_combinations(["+", "*"], operands)

            if not cls.is_valid_input(answer, operands, combos):
                invalid_inputs.append((answer, operands))
            else:
                total_calibration_result = total_calibration_result + answer

        for invalid_input in invalid_inputs:
            combos = cls.get_operator_combinations(["+", "*", "||"], invalid_input[1])

            if cls.is_valid_input(invalid_input[0], invalid_input[1], combos):
                total_calibration_result = total_calibration_result + invalid_input[0]

        return total_calibration_result

    @classmethod
    def get_operator_combinations(cls, possible_operators: list[str], operands: list[int]) -> list[tuple[str, ...]]:
        operators = []

        number_of_positions = len(operands) - 1
        for combination in itertools.product(possible_operators, repeat=number_of_positions):
            operators.append(combination)
        return operators

    @classmethod
    def is_valid_input(cls, expected_answer: int, operands: list[int], operator_combos: list[tuple[str, ...]]) -> bool:
        # for each combo
        for operator_combo in operator_combos:
            calculated_answer = operands[0]

            position_range = range(1, len(operands))
            for position in position_range:
                current_number = operands[position]

                if operator_combo[position - 1] == "+":
                    calculated_answer = calculated_answer + current_number
                elif operator_combo[position - 1] == "*":
                    calculated_answer = calculated_answer * current_number
                else:
                    calculated_answer = int(str(calculated_answer) + str(current_number))

                if calculated_answer > expected_answer:
                    break

            if expected_answer == calculated_answer:
                return True

        return False
