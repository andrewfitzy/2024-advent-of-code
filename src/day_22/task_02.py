# Standard Library
import math
import operator


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        sequences: dict[tuple[int, int, int, int], int] = {}
        for line in file_content:
            secret = int(line)
            ones = cls.get_pseudorandom_ones(2000, secret)

            seen = set()
            for pointer in range(4, len(ones)):
                first_transition = ones[pointer - 3] - ones[pointer - 4]
                second_transition = ones[pointer - 2] - ones[pointer - 3]
                third_transition = ones[pointer - 1] - ones[pointer - 2]
                fourth_transition = ones[pointer] - ones[pointer - 1]
                sequence = (first_transition, second_transition, third_transition, fourth_transition)
                if sequence in seen:
                    continue

                seen.add(sequence)

                total_bananas_for_sequence = sequences.get(sequence, 0)
                total_bananas_for_sequence = total_bananas_for_sequence + ones[pointer]
                sequences[sequence] = total_bananas_for_sequence

        max_bananas = 0
        for key, value in sequences.items():
            if value > max_bananas:
                max_bananas = value

        return max_bananas

    @classmethod
    def get_pseudorandom_ones(cls, iterations: int, secret: int) -> list[int]:
        pseudorandom_ones = [secret % 10]
        pseudorandom_number = secret
        for iteration in range(iterations):
            pseudorandom_number = cls.step_01_result(pseudorandom_number)
            pseudorandom_number = cls.step_02_result(pseudorandom_number)
            pseudorandom_number = cls.step_03_result(pseudorandom_number)
            pseudorandom_ones.append(pseudorandom_number % 10)
        return pseudorandom_ones

    @classmethod
    def step_01_result(cls, secret: int) -> int:
        result = secret * 64
        result = operator.xor(secret, result)
        result = result % 16777216
        return result

    @classmethod
    def step_02_result(cls, secret: int) -> int:
        result = math.floor(secret / 32)
        result = operator.xor(secret, result)
        result = result % 16777216
        return result

    @classmethod
    def step_03_result(cls, secret: int) -> int:
        result = secret * 2048
        result = operator.xor(secret, result)
        result = result % 16777216
        return result
