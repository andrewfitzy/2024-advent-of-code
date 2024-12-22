# Standard Library
import math
import operator


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        result = 0
        for line in file_content:
            secret = int(line)
            result = result + cls.get_pseudorandom_number(2000, secret)
        return result

    @classmethod
    def get_pseudorandom_number(cls, iterations: int, secret: int) -> int:
        pseudorandom_number = secret
        for iteration in range(iterations):
            pseudorandom_number = cls.step_01_result(pseudorandom_number)
            pseudorandom_number = cls.step_02_result(pseudorandom_number)
            pseudorandom_number = cls.step_03_result(pseudorandom_number)
        return pseudorandom_number

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
